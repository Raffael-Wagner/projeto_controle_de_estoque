from PySide2.QtWidgets import QFileDialog, QMessageBox
from PySide2.QtWidgets import QTreeWidgetItem
import openpyxl
import pandas as pd

#***Função para selecionar um arquivo
#   Abre uma caixa de diálogo para que o usuário possa selecionar o arquivo que deseja importar.
#   "options = QFileDialog.Options()"é criado um objeto do QFileDialog que reune as configurações da janela de diálogo, como por exemplo, pode-se colocar uma configuração que a caixa de diálogo tenha a aparência e as funções do Qt e não do sistema operacional.
#   "QFileDialog.getOpenFileName" abre uma janela para que o usuário selecione o arquivo desejado. O "main_window" é a instância da classe atual e "Abrir Arquivo Exvel" é o título da janela aberta. Nas aspas "" temos o diretório inicial, mas por estar vazia significa que será o diretório padrão. "Excel Files (*.xlsx);; All Files (*)" se refere a definição dos arquivos que o usuário pode selecionar. E por fim, "options=options" aplica as configurações que foram definidas.
#   Assim, a função nos retorna uma tupla, onde o primeiro elemento é o caminho completo do arquivo selecionado e o segundo elemento é um espaço reservado para uma variável que não utilizaremos.
#   "if fileName:" é a verificação se "fileName" não está vazio, isto é, se o usuário de fato selecionou um arquivo. Caso isso ocorra, o caminho completo do arquivo é definido como o texto do widget "txt_file"(nome definido no Qt Designer). Dessa maneira, no "QLineEdit" teremos a exibição do caminho do arquivo.
def open_file_dialog(main_window):
    options = QFileDialog.Options()
    fileName, _ = QFileDialog.getOpenFileName(main_window, "Abrir Arquivo Excel", "", "Excel Files (*.xlsx);; All Files (*)", options=options)
    if fileName:
        main_window.txt_file.setText(fileName)  

#***Função para iniciar a importação do arquivo Excel***
#   Inicialmente, obtemos o caminho do arquivo a partir de "main_window.txt_file.text()" um campo de texto. Caso o caminho não for vazio, então é chamada a função "read_excel" com o caminho do arquivo.
def import_excel(main_window):
    file_path = main_window.txt_file.text()  
    if file_path:
        main_window.excel_file_path = file_path
        read_excel(main_window, file_path)
        QMessageBox.information(main_window, "Importação Concluída", "Importação realizada com sucesso.")

def read_excel(main_window, file_path):
    pasta_de_trabalho = openpyxl.load_workbook(file_path)
    folha = pasta_de_trabalho.active

    linhas = folha.max_row
    colunas = folha.max_column

    for linha in range(2, linhas + 1):
        item = QTreeWidgetItem()

        for coluna in range(1, colunas + 1):
            valor_celula = folha.cell(row=linha, column=coluna).value
            item.setText(coluna - 1, str(valor_celula))
        main_window.tw_estoque.addTopLevelItem(item)
#***Função gerar excel do estoque criado de maneira manual***
def gerar_excel_estoque_manual(main_window):
    headers = []
    for column in range(main_window.tw_estoque.columnCount()):
        headers.append(main_window.tw_estoque.headerItem().text(column))
        
    data = []
    for row in range(main_window.tw_estoque.topLevelItemCount()):
        item_data = []
        for column in range(main_window.tw_estoque.columnCount()):
            item_data.append(main_window.tw_estoque.topLevelItem(row).text(column))
        data.append(item_data)

    df = pd.DataFrame(data, columns=headers)

    options = QFileDialog.Options()
    file_path, _ = QFileDialog.getSaveFileName(main_window, "Salvar arquivo Excel", "", "Excel Files (*.xlsx)", options=options)
    if file_path:
        df.to_excel(file_path, index=False)
        QMessageBox.information(main_window, "Operação concluída", f"O arquivo foi salvo com sucesso!")

def update_excel(main_window):
    if not main_window.excel_file_path:
        return

    workbook = openpyxl.load_workbook(main_window.excel_file_path)
    sheet = workbook.active

    sheet.delete_rows(2, sheet.max_row)

    for indice_linha_atual in range(main_window.tw_estoque.topLevelItemCount()):
        item = main_window.tw_estoque.topLevelItem(indice_linha_atual)
        for indice_coluna_atual in range(item.columnCount()):
            sheet.cell(row=indice_linha_atual + 2, column=indice_coluna_atual + 1).value = item.text(indice_coluna_atual)

    workbook.save(main_window.excel_file_path)