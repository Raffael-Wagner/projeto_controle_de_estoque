from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide2.QtWidgets import QTreeWidgetItem
from PySide2.QtWidgets import QInputDialog, QMessageBox
from ui_main import Ui_MainWindow
from PySide2.QtGui import QColor
from PySide2.QtCore import Qt
import sys
import openpyxl
import logging
import datetime
import smtplib
import email.message

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Sistema de Gerenciamento")

        #Botões de cada aba na barra de cima (basicamente é pra navegar naquelas 'abas')
        #Esses nomes pg_home, pg_table e pg_excel, eu coloquei no aplicativo QT Designer. Foi seguindo o vídeo que Laryssa mandou.
        self.btn_inicio.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_home))
        self.btn_estoque.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_table))
        self.btn_excel.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_excel))

        #Botões que estão dentro da aba do estoque
        self.btn_add.clicked.connect(self.add_item_to_estoque)
        self.btn_remove.clicked.connect(self.remove_item_from_estoque)
        self.btn_refresh.clicked.connect(self.update_item_from_estoque)
        self.btn_saida.clicked.connect(self.saida_item_from_estoque)


    #Função para adicionar algum item
    def add_item_to_estoque(self):
        codigo, ok = QInputDialog.getText(self, "Código", "O último digito é referente ao setor\n1 - Limpeza\n2 - Bebidas\n3 - Hortifruti\n4 - Condimentos\n5 - Padaria\n6 - Biscoitos\n7 - Doces\n8 - Açougue\n9 - Congelados\n10 - Frios\n11 - Limpeza\n12 - Higiene\nDigite o código do produto:\n")
        if ok and codigo.isdigit():
            ultimo_digito = codigo[-1]

            if ultimo_digito == '1':
                setor = "Limpeza"
            elif ultimo_digito == '2':
                setor = "Bebidas"
            elif ultimo_digito == '3':
                setor = "Hortifruti"
            elif ultimo_digito == '4':
                setor = "Condimentos"
            elif ultimo_digito == '5':
                setor = "Padaria"
            elif ultimo_digito == '6':
                setor = "Biscoitos"
            elif ultimo_digito == '7':
                setor = "Doces"
            elif ultimo_digito == '8':
                setor = "Açougue"
            elif ultimo_digito == '9':
                setor = "Congelados"
            elif ultimo_digito == '10':
                setor = "Frios"
            elif ultimo_digito == '11':
                setor = "Limpeza"
            elif ultimo_digito == '12':
                setor = "Higiene"
        else:
            QMessageBox.warning(self, "Aviso", "Insira um código válido contendo apenas números.")
            return

        nome, ok = QInputDialog.getText(self, "Produto", "Nome do produto:")
        if ok:
            validade, ok = QInputDialog.getText(self, "Validade", "Validade(dd/mm/aaaa):")
            try:
                validade_date = datetime.datetime.strptime(validade, '%d/%m/%Y')
                        
            except ValueError:
                QMessageBox.warning(self, "Aviso", "Informe uma data de validade válida no formato dd/mm/aaaa.")
                return
            
            preco_custo, ok = QInputDialog.getText(self, "Preço de Custo", "Preço de Custo:")
            if ok:
                preco_venda, ok = QInputDialog.getText(self, "Preço de Venda", "Preço de Venda:")
                if ok:
                    quantidade, ok = QInputDialog.getText(self, "Quantidade", "Quantidade:")
                    if ok:
                        quantidade_min, ok = QInputDialog.getText(self, "Quantidade Mínima", "Quantidade Mínima:")
                        if ok:
                            fornecedor, ok = QInputDialog.getText(self, "Fornecedor", "Fornecedor:")
                            if ok:
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
                                    self.enviar_email()
        else:
            QMessageBox.warning(self, "Aviso", "Operação cancelada pelo usuário.")
    
    #Função para remover algum item
    def remove_item_from_estoque(self):
            nome, ok = QInputDialog.getText(self, "Remover Item", "Informe o nome do produto que deseja remover:")
            if ok:
                found = False
                for i in range(self.tw_estoque.topLevelItemCount()):
                    item = self.tw_estoque.topLevelItem(i)
                    if item.text(1) == nome:
                        self.tw_estoque.takeTopLevelItem(i)
                        found = True
                        break
                if not found:
                    QMessageBox.warning(self, "Aviso", "Produto não encontrado no estoque.")
            else:
                QMessageBox.warning(self, "Aviso", "Operação cancelada pelo usuário.")

    #Função para atualizar algum item
    def update_item_from_estoque(self):
        nome, ok = QInputDialog.getText(self, "Atualizar Item", "Nome do produto para atualizar:")
        if ok:
            found = False
            for i in range(self.tw_estoque.topLevelItemCount()):
                item = self.tw_estoque.topLevelItem(i)
                if item.text(1) == nome:
                    found = True
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
                                                # Atualizar os valores do item
                                                item.setText(0, codigo)
                                                item.setText(2, validade)
                                                item.setText(3, preco_custo)
                                                item.setText(4, preco_venda)
                                                item.setText(5, quantidade)
                                                item.setText(6, quantidade_min)
                                                item.setText(7, fornecedor)
                    break
            if not found:
                QMessageBox.warning(self, "Aviso", "Produto não encontrado no estoque.")
        else:
            QMessageBox.warning(self, "Aviso", "Operação cancelada pelo usuário.")
    
    #Função para a realização da saída
    def saida_item_from_estoque(self):
        nome, ok = QInputDialog.getText(self, "Saída de Item", "Informe o nome do produto:")
        if ok:
            quantidade_saida, ok = QInputDialog.getInt(self, "Saída de Item", "Quantidade a ser retirada:")
            if ok:
                if quantidade_saida <= 0:
                    QMessageBox.warning(self, "Aviso", "A quantidade a ser retirada deve ser um número válido (positivo).")
                    return
            
                found = False
                for i in range(self.tw_estoque.topLevelItemCount()):
                    item = self.tw_estoque.topLevelItem(i)
                    if item.text(1) == nome:
                        quantidade_atual = int(item.text(5))
                        quantidade_min = int(item.text(6))

                        if quantidade_saida > quantidade_atual:
                            QMessageBox.warning(self, "Aviso", "Quantidade a ser retirada maior do que a quantidade disponível.")
                            return

                        nova_quantidade = quantidade_atual - quantidade_saida
                        item.setText(5, str(nova_quantidade))
                        found = True

                        # Verifica se a quantidade está abaixo do mínimo e envia e-mail
                        if nova_quantidade <= quantidade_min:
                            self.enviar_email(item.text(1), nova_quantidade, quantidade_min)
                        saida_item = QTreeWidgetItem()
                        saida_item.setText(0, nome.upper())
                        saida_item.setText(1, str(quantidade_saida))
                        saida_item.setText(2, datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
                        self.tw_saida.addTopLevelItem(saida_item)

                        break

                if not found:
                    QMessageBox.warning(self, "Aviso", "Produto não encontrado no estoque.")
            else:
                QMessageBox.warning(self, "Aviso", "Operação cancelada pelo usuário.")
        else:
            QMessageBox.warning(self, "Aviso", "Operação cancelada pelo usuário.")

    # Função do envio do e-mail
    def enviar_email(self, nome_produto, quantidade_atual, quantidade_min):
        corpo_email = f"""
        <p>Olá, caro(a) fornecedor(a)</p>
        <hr>
        <p>A Equipe EstoKI vem, por meio desta, informar que nosso estoque do produto {nome_produto} está ficando baixo. Atualmente, nos restam apenas {quantidade_atual} unidades em nosso estoque, sendo insuficiente para atender à demanda que espera-se para o próximo mês.</p>
        <p>Sabendo que o produto tem uma certa popularidade e vem mostrando rapidez em vendas, gostaríamos de realizar a solicitação do reabastecimento de {quantidade_min * 3} unidades o mais rápido possível. Agradecemos sua atenção. </p>
        <p>Atenciosamente,</p>
        <p>EstoKI</p>
        """

        msg = email.message.Message()
        msg['Subject'] = "Reposição de Estoque"
        msg['From'] = 'raffaelwagner@gmail.com'
        msg['To'] = 'milorrengaw@gmail.com'
        password = ''
        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(corpo_email)

        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))


    #Funções que envolvem o Excel    

if __name__ == "__main__":
    # Configurar o nível de registro para DEBUG
    logging.basicConfig(level=logging.DEBUG)

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
