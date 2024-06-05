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

        # Botões que estão na aba do Excel
        self.btn_open.clicked.connect(self.open_file_dialog)


    #***Função para adicionar algum item***
#   Quando o usuário clicka no botão "ADICIONAR", abre uma caixa de diálogo solicitando que ele informe o código do produto que deseja adicionar o estoque. Nela é mostrada uma tabela com os setores relacionados aos últimos dois dígitos do código.
#   A função "QInputDialog.getText" retorna uma tupla com os seguintes valores: o texto que o usuário digitou e o booleano ok. Esse booleano indica se o usuário clickou no "OK" para confirmar a entrada do texto digitado ou "CANCELAR" para cancelar a operação.
#   A entrada é validada apenas se a quantidade de dígitos do código for maior ou igual a 2 e se conter apenas números. Caso isso seja atendido e o usuário clickar em "OK", o código realizará a análise dos últimos dígitos e a partir deles atribuir o setor e fornecedor. Se os últimos dígitos forem diferentes da tabela, aparecerá uma mensagem dizendo que este setor é desconhecido.
#   Em seguida, o código solicita que o usuário informe o nome do produto que deseja cadastrar. Para a validade do produto, ele fará a validação para saber se está no formato (dd/mm/aaaa), caso não esteja aparecerá uma mensagem solicitando que o usuário informe uma data no formato pedido. Realizando isso, pede-se o preço de custo, preço de venda, quantidade e quantidade mínima.
#   Com todos os dados, agora é criado um novo item que deve ser adicionado na QTreeWidget. Ela representa a tabela de estoque que chamamos de "tw_estoque". Assim, ele vai definindo o texto de cada coluna.
#   Em "for col in range(9)", temos o loop que vai iterar pelas colunas de 0 a 8. Como "new_item.setForeground(col, QColor(Qt.black))" está dentro do loop, faz com que a cor de cada coluna seja preta.
#   " self.tw_estoque.addTopLevelItem(new_item)" faz com que o novo item seja adicionado na QTreeWidget, ou seja, o novo item aparece na tabela como uma nova linha em tw_estoque.
#   Por fim, ele faz a verificação se a quantidade de produto é menor ou igual a quantidade mínima, caso isso ocorra ele adiciona no estoque e chama a função de enviar e-mail.

    def add_item_to_estoque(self):
        codigo, ok = QInputDialog.getText(self, "Código", "O último digito é referente ao setor\n01 - Limpeza\n02 - Bebidas\n03 - Hortifruti\n04 - Condimentos\n05 - Padaria\n06 - Biscoitos\n07 - Doces\n08 - Açougue\n09 - Congelados\n10 - Frios\n11 - Limpeza\n12 - Higiene\nDigite o código do produto:\n")
        if ok and codigo.isdigit():
            if len(codigo) < 2:
                QMessageBox.warning(self, "Aviso", "O código deve ter pelo menos dois dígitos.")
                return

            dois_ultimos_digitos = codigo[-2:]

            if dois_ultimos_digitos == '01':
                setor = "Limpeza"
                fornecedor = "fornecedor1@gmail.com"
            elif dois_ultimos_digitos == '02':
                setor = "Bebidas"
                fornecedor = "fornecedor2@gmail.com"
            elif dois_ultimos_digitos == '03':
                setor = "Hortifruti"
                fornecedor = "fornecedor3@gmail.com"
            elif dois_ultimos_digitos == '04':
                setor = "Condimentos"
                fornecedor = "fornecedor4@gmail.com"
            elif dois_ultimos_digitos == '05':
                setor = "Padaria"
                fornecedor = "fornecedor5@gmail.com"
            elif dois_ultimos_digitos == '06':
                setor = "Biscoitos"
                fornecedor = "fornecedor6@gmail.com"
            elif dois_ultimos_digitos == '07':
                setor = "Doces"
                fornecedor = "fornecedor7@gmail.com"
            elif dois_ultimos_digitos == '08':
                setor = "Açougue"
                fornecedor = "fornecedor8@gmail.com"
            elif dois_ultimos_digitos == '09':
                setor = "Congelados"
                fornecedor = "fornecedor9@gmail.com"
            elif dois_ultimos_digitos == '10':
                setor = "Frios"
                fornecedor = "fornecedor10@gmail.com"
            elif dois_ultimos_digitos == '11':
                setor = "Limpeza"
                fornecedor = "fornecedor11@gmail.com"
            elif dois_ultimos_digitos == '12':
                setor = "Higiene"
                fornecedor = "fornecedor12@gmail.com"
            else:
                QMessageBox.warning(self, "Aviso", "Setor não reconhecido.")
                return
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
    
    #***Função para remover algum item***
#   Quando o usuário clica no botão "REMOVER", abre uma caixa de diálogo solicitando que ele informe o nome do produto que deseja remover do estoque.
#   O usuário digita o nome do produto que deseja remover. A entrada é validada apenas se ele clickar em "OK". Ao clickar em "OK", o código irá procurar pelo nome do produto na QTreeWidget que chamamos de "tw_estoque". Inicializamos com a variável found como sendo "False", é ela que indicará se o produto for encontrado.
#   Assim, "for i in range(self.tw_estoque.topLevelItemCount()):" é o loop responsável por iterar sobre todas as linhas de 'tw_estoque'. "item = self.tw_estoque.topLevelItem(i)" é referente ao item atual da iteração do loop.
#   Em "if item.text(1) == nome:", temos a comparação do texto do índice 1 com o nome do produto que o usuário informou. Se os nomes forem iguais, então temos que o produto que queremos remover foi encontrado.
#   Se o nome do produto for encontrado, ele é removido de "tw_estoque" através de "self.tw_estoque.takeTopLevelItem(i)". Assim, a variável found passa a ser "True" para indicar que foi encontrado. O "break" é utilizado para que possamos sair do loop, visto que o produto já foi encontrado e removido.
#   Já se o produto não for encontrado, uma mensagem de aviso será exibida. E caso o usuário clicke em "CANCELAR", a operação é cancelada e uma mensagem de aviso é exibida.
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

    #***Função para selecionar um arquivo
#   Abre uma caixa de diálogo para que o usuário possa selecionar o arquivo que deseja importar.
#   "options = QFileDialog.Options()"é criado um objeto do QFileDialog que reune as configurações da janela de diálogo, como por exemplo, pode-se colocar uma configuração que a caixa de diálogo tenha a aparência e as funções do Qt e não do sistema operacional.
#   "QFileDialog.getOpenFileName" abre uma janela para que o usuário selecione o arquivo desejado. O "self" é a instância da classe atual e "Abrir Arquivo Exvel" é o título da janela aberta. Nas aspas "" temos o diretório inicial, mas por estar vazia significa que será o diretório padrão. "Excel Files (*.xlsx);; All Files (*)" se refere a definição dos arquivos que o usuário pode selecionar. E por fim, "options=options" aplica as configurações que foram definidas.
#   Assim, a função nos retorna uma tupla, onde o primeiro elemento é o caminho completo do arquivo selecionado e o segundo elemento é um espaço reservado para uma variável que não utilizaremos.
#   "if fileName:" é a verificação se "fileName" não está vazio, isto é, se o usuário de fato selecionou um arquivo. Caso isso ocorra, o caminho completo do arquivo é definido como o texto do widget "txt_file"(nome definido no Qt Designer). Dessa maneira, no "QLineEdit" teremos a exibição do caminho do arquivo.
    def open_file_dialog(self):
        options = QFileDialog.Options()

        fileName, _ = QFileDialog.getOpenFileName(self, "Abrir Arquivo Excel", "", "Excel Files (*.xlsx);;  All Files (*)", options=options)
        if fileName:
            self.txt_file.setText(fileName)  



if __name__ == "__main__":
    # Configurar o nível de registro para DEBUG
    logging.basicConfig(level=logging.DEBUG)

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
