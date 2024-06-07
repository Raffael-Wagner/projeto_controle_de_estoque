from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog, QInputDialog, QMessageBox, QTreeWidgetItem
from excel import open_file_dialog, import_excel, gerar_excel_estoque_manual, read_excel, update_excel
from utilitarios import enviar_email, mostrar_grafico, credenciais_email, codigo_existente, nome_existente
from ui_main import Ui_MainWindow
from PySide2.QtGui import QColor
from PySide2.QtCore import Qt
import matplotlib.pyplot as plt
import email.message
import pandas as pd
import datetime
import logging
import smtplib
import json
import sys

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.excel_file_path = None
        self.setWindowTitle("Sistema EstoKI")

        #Inicializar dicionário de saídas dos produtos
        self.saidas = {}

        #Inicializar o DataFrame - ele vai ajudar no processo de modificar o arquivo Excel
        self.df_estoque = pd.DataFrame()

        #Botões de cada aba na barra de cima (basicamente é pra navegar naquelas 'abas')
        self.btn_inicio.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_home))
        self.btn_estoque.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_table))
        self.btn_excel.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_excel))

        #Botões que estão dentro da aba do estoque
        self.btn_add.clicked.connect(self.add_item_to_estoque)
        self.btn_remove.clicked.connect(self.remove_item_from_estoque)
        self.btn_refresh.clicked.connect(self.update_item_from_estoque)
        self.btn_saida.clicked.connect(self.saida_item_from_estoque)
        self.btn_limpar.clicked.connect(self.limpar_estoque)
        self.btn_grafico.clicked.connect(lambda: mostrar_grafico(self.saidas))
        self.btn_gerar_excel.clicked.connect(lambda: gerar_excel_estoque_manual(self))

        # Botões que estão na aba do Excel
        self.btn_open.clicked.connect(lambda: open_file_dialog(self))
        self.btn_import.clicked.connect(lambda: import_excel(self))        

        self.update_excel()

    def add_item_to_estoque(self):
        setores_fornecedores = {
        '01': ("Limpeza", "milorrengaw@gmail.com"),
        '02': ("Bebidas", "fornecedor2@gmail.com"),
        '03': ("Hortifruti", "fornecedor3@gmail.com"),
        '04': ("Condimentos", "fornecedor4@gmail.com"),
        '05': ("Padaria", "fornecedor5@gmail.com"),
        '06': ("Biscoitos", "fornecedor6@gmail.com"),
        '07': ("Doces", "fornecedor7@gmail.com"),
        '08': ("Açougue", "fornecedor8@gmail.com"),
        '09': ("Congelados", "fornecedor9@gmail.com"),
        '10': ("Frios", "fornecedor10@gmail.com"),
        '11': ("Limpeza", "fornecedor11@gmail.com"),
        '12': ("Higiene", "fornecedor12@gmail.com")
    }
        codigo, ok = QInputDialog.getText(self, "Código", "O último digito é referente ao setor\n01 - Limpeza\n02 - Bebidas\n03 - Hortifruti\n04 - Condimentos\n05 - Padaria\n06 - Biscoitos\n07 - Doces\n08 - Açougue\n09 - Congelados\n10 - Frios\n11 - Limpeza\n12 - Higiene\nDigite o código do produto:\n")

        if ok and codigo.isdigit():
            if len(codigo) < 2:
                QMessageBox.warning(self, "Aviso", "O código deve ter pelo menos dois dígitos.")
                return
            
            if codigo_existente(self.tw_estoque, codigo):
                QMessageBox.warning(self, "Aviso", "O código informado já está em uso.")
                return
        
            dois_ultimos_digitos = codigo[-2:]
            if dois_ultimos_digitos in setores_fornecedores:
                setor, fornecedor = setores_fornecedores[dois_ultimos_digitos]
            else:
                QMessageBox.warning(self, "Aviso", "Não reconhecemos este setor.")
                return
        else:
            QMessageBox.warning(self, "Aviso", "Insira um código válido contendo apenas números.")
            return

        nome, ok = QInputDialog.getText(self, "Produto", "Nome do produto:")
        if not ok:
            QMessageBox.warning(self, "Aviso", "Operação cancelada pelo usuário.")
            return
        
        if nome_existente(self.tw_estoque, nome):
            QMessageBox.warning(self, "Aviso", "Este produto já está em nosso estoque. Por favor, insira um outro produto ou atualize-o.")
            return

        validade, ok = QInputDialog.getText(self, "Validade", "Validade(dd/mm/aaaa):")
        if not ok:
            QMessageBox.warning(self, "Aviso", "Operação cancelada pelo usuário.")
            return

        try:
            validade_date = datetime.datetime.strptime(validade, '%d/%m/%Y')
            if validade_date <= datetime.datetime.now():
                QMessageBox.warning(self, "Aviso", "Nosso sistema não aceita produtos vencidos.")
                return
        except ValueError:
            QMessageBox.warning(self, "Aviso", "Informe uma data de validade válida no formato dd/mm/aaaa.")
            return

        preco_custo, ok = QInputDialog.getText(self, "Preço de Custo", "Preço de Custo:")
        if not ok or float(preco_custo) <= 0:
            QMessageBox.warning(self, "Aviso", "Operação cancelada pelo usuário.")
            return

        preco_venda, ok = QInputDialog.getText(self, "Preço de Venda", "Preço de Venda:")
        if not ok or float(preco_venda) <= 0:
            QMessageBox.warning(self, "Aviso", "Operação cancelada pelo usuário.")
            return

        quantidade, ok = QInputDialog.getText(self, "Quantidade", "Quantidade:")
        if not ok or int(quantidade) <=0 :
            QMessageBox.warning(self, "Aviso", "Operação cancelada pelo usuário.")
            return

        quantidade_min, ok = QInputDialog.getText(self, "Quantidade Mínima", "Quantidade Mínima:")
        if not ok or int(quantidade_min) <=0 :
            QMessageBox.warning(self, "Aviso", "Operação cancelada pelo usuário.")
            return

        preco_custo = "{:.2f}".format(float(preco_custo))
        preco_venda = "{:.2f}".format(float(preco_venda))
        
        new_item = QTreeWidgetItem()
        new_item.setText(0, codigo)
        new_item.setText(1, nome)
        new_item.setText(2, validade)
        new_item.setText(3, preco_custo)
        new_item.setText(4, preco_venda)
        new_item.setText(5, quantidade)
        new_item.setText(6, quantidade_min)
        new_item.setText(7, setor)
        new_item.setText(8, fornecedor)
        for col in range(9):
            new_item.setForeground(col, QColor(Qt.black))

        self.tw_estoque.addTopLevelItem(new_item)

        if int(quantidade) <= int(quantidade_min):
            enviar_email(nome, quantidade, quantidade_min, fornecedor)

        if self.excel_file_path:
            self.update_excel()

    def remove_item_from_estoque(self):
            nome, ok = QInputDialog.getText(self, "Remover Item", "Informe o nome do produto que deseja remover:")
            if ok:
                encontrar = False
                for i in range(self.tw_estoque.topLevelItemCount()):
                    item = self.tw_estoque.topLevelItem(i)
                    if item.text(1) == nome:
                        self.tw_estoque.takeTopLevelItem(i)
                        encontrar = True
                        break
                if not encontrar:
                    QMessageBox.warning(self, "Aviso", "Produto não encontrado no estoque.")
            else:
                QMessageBox.warning(self, "Aviso", "Operação cancelada pelo usuário.")

            if self.excel_file_path:
                self.update_excel()

    def update_item_from_estoque(self):
        nome, ok = QInputDialog.getText(self, "Atualizar Item", "Nome do produto para atualizar:")
        if ok:
            encontrar = False
            for i in range(self.tw_estoque.topLevelItemCount()):
                item = self.tw_estoque.topLevelItem(i)
                if item.text(1) == nome:
                    encontrar = True
                    codigo, ok = QInputDialog.getText(self, "Atualizar Item", "Código:", text=item.text(0))
                    if ok:
                        validade, ok = QInputDialog.getText(self, "Atualizar Item", "Validade:", text=item.text(2))
                        if ok:
                            preco_custo, ok = QInputDialog.getText(self, "Atualizar Item", "Preço de Custo:", text=item.text(3))
                            if ok:
                                preco_venda, ok = QInputDialog.getText(self, "Atualizar Item", "Preço de Venda:", text=item.text(4))
                                if ok:
                                    quantidade, ok = QInputDialog.getText(self, "Atualizar Item", "Quantidade:", text=item.text(5))
                                    if ok:
                                        quantidade_min, ok = QInputDialog.getText(self, "Atualizar Item", "Quantidade Mínima:", text=item.text(6))
                                        if ok:
                                            fornecedor, ok = QInputDialog.getText(self, "Atualizar Item", "Fornecedor:", text=item.text(7))
                                            if ok:
                                                item.setText(0, codigo)
                                                item.setText(2, validade)
                                                item.setText(3, preco_custo)
                                                item.setText(4, preco_venda)
                                                item.setText(5, quantidade)
                                                item.setText(6, quantidade_min)
                                                item.setText(7, fornecedor)
                    break
            if not encontrar:
                QMessageBox.warning(self, "Aviso", "Produto não encontrado no estoque.")
        else:
            QMessageBox.warning(self, "Aviso", "Operação cancelada pelo usuário.")
    
        if self.excel_file_path:
            self.update_excel()

    def saida_item_from_estoque(self):
        nome, ok = QInputDialog.getText(self, "Saída de Item", "Informe o nome do produto:")
        if ok:
            quantidade_saida, ok = QInputDialog.getInt(self, "Saída de Item", "Quantidade a ser retirada:")
            if ok:
                if quantidade_saida <= 0:
                    QMessageBox.warning(self, "Aviso", "A quantidade a ser retirada deve ser um número válido (positivo).")
                    return
            
                encontrar = False
                for i in range(self.tw_estoque.topLevelItemCount()):
                    item = self.tw_estoque.topLevelItem(i)
                    if item.text(1) == nome:
                        quantidade_atual = int(item.text(5))
                        quantidade_min = int(item.text(6))
                        fornecedor = item.text(8)

                        if quantidade_saida > quantidade_atual:
                            QMessageBox.warning(self, "Aviso", "Quantidade a ser retirada maior do que a quantidade disponível.")
                            return

                        nova_quantidade = quantidade_atual - quantidade_saida
                        item.setText(5, str(nova_quantidade))
                        encontrar = True

                        if nome in self.saidas:
                            self.saidas[nome] += quantidade_saida
                        else:
                            self.saidas[nome] = quantidade_saida

                        if nova_quantidade <= quantidade_min:
                            enviar_email(item.text(1), nova_quantidade, quantidade_min, fornecedor)
                        saida_item = QTreeWidgetItem()
                        saida_item.setText(0, nome.upper())
                        saida_item.setText(1, str(quantidade_saida))
                        saida_item.setText(2, datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S'))

                        for column in range(saida_item.columnCount()):
                            saida_item.setForeground(column, QColor(Qt.red))
                        self.tw_saida.addTopLevelItem(saida_item)

                        break

                if not encontrar:
                    QMessageBox.warning(self, "Aviso", "Produto não encontrado no estoque.")
            else:
                QMessageBox.warning(self, "Aviso", "Operação cancelada pelo usuário.")
        else:
            QMessageBox.warning(self, "Aviso", "Operação cancelada pelo usuário.")

        if self.excel_file_path:
            self.update_excel()

    def limpar_estoque(self):
        self.tw_estoque.clear()
        self.tw_saida.clear()
        if self.excel_file_path:
            self.update_excel()

    def update_excel(self):
        update_excel(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
