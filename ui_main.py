# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(941, 587)
        MainWindow.setStyleSheet(u"background-color:#e8f1f2;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_8 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(True)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_inicio = QPushButton(self.frame)
        self.btn_inicio.setObjectName(u"btn_inicio")
        self.btn_inicio.setMinimumSize(QSize(0, 35))
        self.btn_inicio.setStyleSheet(u"QPushButton{\n"
"   color: rgb(255, 255, 255);\n"
"   border-radius: 3px;\n"
"   font-size: 16px;\n"
"   background-color:#247BA0;\n"
"}\n"
"\n"
"QPushButton:hover{background-color: rgb(170,255,255); color:black}\n"
",\n"
"")

        self.horizontalLayout.addWidget(self.btn_inicio)

        self.btn_estoque = QPushButton(self.frame)
        self.btn_estoque.setObjectName(u"btn_estoque")
        self.btn_estoque.setMinimumSize(QSize(0, 35))
        self.btn_estoque.setStyleSheet(u"QPushButton{\n"
"   color: rgb(255, 255, 255);\n"
"   border-radius: 3px;\n"
"   font-size: 16px;\n"
"   background-color:#247BA0;\n"
"}\n"
"\n"
"QPushButton:hover{background-color: rgb(170,255,255); color:black}\n"
",\n"
"")

        self.horizontalLayout.addWidget(self.btn_estoque)

        self.btn_excel = QPushButton(self.frame)
        self.btn_excel.setObjectName(u"btn_excel")
        self.btn_excel.setMinimumSize(QSize(0, 35))
        self.btn_excel.setStyleSheet(u"QPushButton{\n"
"   color: rgb(255, 255, 255);\n"
"   border-radius: 3px;\n"
"   font-size: 16px;\n"
"   background-color:#247BA0;\n"
"}\n"
"\n"
"QPushButton:hover{background-color: rgb(170,255,255); color:black}\n"
",\n"
"")

        self.horizontalLayout.addWidget(self.btn_excel)


        self.verticalLayout_8.addWidget(self.frame)

        self.Pages = QStackedWidget(self.centralwidget)
        self.Pages.setObjectName(u"Pages")
        self.pg_table = QWidget()
        self.pg_table.setObjectName(u"pg_table")
        self.verticalLayout_7 = QVBoxLayout(self.pg_table)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.tabWidget = QTabWidget(self.pg_table)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"")
        self.tables = QWidget()
        self.tables.setObjectName(u"tables")
        self.verticalLayout = QVBoxLayout(self.tables)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_3 = QLabel(self.tables)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"background-color: #247ba0;\n"
"color: #fff;")

        self.verticalLayout_5.addWidget(self.label_3)

        self.tw_estoque = QTreeWidget(self.tables)
        self.tw_estoque.setObjectName(u"tw_estoque")
        self.tw_estoque.setStyleSheet(u"color: black;\n"
"background-color: #E8F1F2;")

        self.verticalLayout_5.addWidget(self.tw_estoque)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.tables)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"background-color: #247ba0;\n"
"color: #fff;")

        self.verticalLayout_4.addWidget(self.label_2)

        self.tw_saida = QTreeWidget(self.tables)
        self.tw_saida.setObjectName(u"tw_saida")
        self.tw_saida.setStyleSheet(u"color: black;\n"
"background-color: #E8F1F2;")

        self.verticalLayout_4.addWidget(self.tw_saida)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)


        self.horizontalLayout_2.addLayout(self.verticalLayout_6)

        self.frame_2 = QFrame(self.tables)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet(u"background-color: #247ba0;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_add = QPushButton(self.frame_2)
        self.btn_add.setObjectName(u"btn_add")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_add.sizePolicy().hasHeightForWidth())
        self.btn_add.setSizePolicy(sizePolicy1)
        self.btn_add.setMinimumSize(QSize(0, 0))
        self.btn_add.setStyleSheet(u"QPushButton{\n"
"   color: black;\n"
"   border-radius: 8px;\n"
"   font-size: 16px;\n"
"   background-color: #FFF;\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{background-color: rgb(170,255,255); color:black}\n"
",")

        self.verticalLayout_3.addWidget(self.btn_add)

        self.btn_remove = QPushButton(self.frame_2)
        self.btn_remove.setObjectName(u"btn_remove")
        self.btn_remove.setStyleSheet(u"QPushButton{\n"
"   color: black;\n"
"   border-radius: 5px;\n"
"   font-size: 16px;\n"
"   background-color: #FFF;\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{background-color: rgb(170,255,255); color:black}\n"
",")

        self.verticalLayout_3.addWidget(self.btn_remove)

        self.btn_refresh = QPushButton(self.frame_2)
        self.btn_refresh.setObjectName(u"btn_refresh")
        self.btn_refresh.setStyleSheet(u"QPushButton{\n"
"   color: black;\n"
"   border-radius: 5px;\n"
"   font-size: 16px;\n"
"   background-color: #FFF;\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{background-color: rgb(170,255,255); color:black}\n"
",")

        self.verticalLayout_3.addWidget(self.btn_refresh)

        self.btn_saida = QPushButton(self.frame_2)
        self.btn_saida.setObjectName(u"btn_saida")
        self.btn_saida.setStyleSheet(u"QPushButton{\n"
"   color: black;\n"
"   border-radius: 5px;\n"
"   font-size: 16px;\n"
"   background-color: #FFF;\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{background-color: rgb(170,255,255); color:black}\n"
",")

        self.verticalLayout_3.addWidget(self.btn_saida)

        self.btn_limpar = QPushButton(self.frame_2)
        self.btn_limpar.setObjectName(u"btn_limpar")
        self.btn_limpar.setStyleSheet(u"QPushButton{\n"
"   color: black;\n"
"   border-radius: 5px;\n"
"   font-size: 16px;\n"
"   background-color: #FFF;\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{background-color: rgb(170,255,255); color:black}\n"
",")

        self.verticalLayout_3.addWidget(self.btn_limpar)

        self.btn_grafico = QPushButton(self.frame_2)
        self.btn_grafico.setObjectName(u"btn_grafico")
        self.btn_grafico.setMinimumSize(QSize(0, 0))
        font = QFont()
        self.btn_grafico.setFont(font)
        self.btn_grafico.setStyleSheet(u"QPushButton{\n"
"   color: black;\n"
"   border-radius: 5px;\n"
"   font-size: 16px;\n"
"   background-color: #FFF;\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{background-color: rgb(170,255,255); color:black}\n"
",")

        self.verticalLayout_3.addWidget(self.btn_grafico)

        self.btn_gerar_excel = QPushButton(self.frame_2)
        self.btn_gerar_excel.setObjectName(u"btn_gerar_excel")
        self.btn_gerar_excel.setMinimumSize(QSize(0, 0))
        self.btn_gerar_excel.setFont(font)
        self.btn_gerar_excel.setStyleSheet(u"QPushButton{\n"
"   color: black;\n"
"   border-radius: 5px;\n"
"   font-size: 16px;\n"
"   background-color: #FFF;\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{background-color: rgb(170,255,255); color:black}\n"
",")

        self.verticalLayout_3.addWidget(self.btn_gerar_excel)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addWidget(self.frame_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.tabWidget.addTab(self.tables, "")

        self.verticalLayout_7.addWidget(self.tabWidget)

        self.Pages.addWidget(self.pg_table)
        self.pg_excel = QWidget()
        self.pg_excel.setObjectName(u"pg_excel")
        self.verticalLayout_9 = QVBoxLayout(self.pg_excel)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_5 = QLabel(self.pg_excel)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font: 75 36pt \"MS Shell Dlg 2\";\n"
"color: #13293d;")

        self.verticalLayout_9.addWidget(self.label_5, 0, Qt.AlignHCenter)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.txt_file = QLineEdit(self.pg_excel)
        self.txt_file.setObjectName(u"txt_file")
        self.txt_file.setMinimumSize(QSize(0, 20))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setWeight(75)
        self.txt_file.setFont(font1)
        self.txt_file.setStyleSheet(u"color: #fff;\n"
"background-color:#247BA0;\n"
"height: 35px;\n"
"border-top-left-radius: 15px;\n"
"")
        self.txt_file.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.txt_file)

        self.btn_open = QPushButton(self.pg_excel)
        self.btn_open.setObjectName(u"btn_open")
        self.btn_open.setMinimumSize(QSize(120, 36))
        self.btn_open.setStyleSheet(u"QPushButton{\n"
"   color:#FFF;\n"
"   border-top-right-radius: 15px;\n"
"   font-size: 16px;\n"
"   background-color:#247BA0;\n"
"}\n"
"\n"
"QPushButton:hover{background-color: rgb(170,255,255); color:black}")

        self.horizontalLayout_4.addWidget(self.btn_open)


        self.verticalLayout_9.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.pg_excel)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.btn_import = QPushButton(self.pg_excel)
        self.btn_import.setObjectName(u"btn_import")
        self.btn_import.setMinimumSize(QSize(0, 37))
        self.btn_import.setFont(font)
        self.btn_import.setStyleSheet(u"QPushButton{\n"
"   color: rgb(255, 255, 255);\n"
"   border-radius: 3px;\n"
"   font-size: 22px;\n"
"   background-color:#247BA0;\n"
"}\n"
"\n"
"QPushButton:hover{background-color: rgb(170,255,255); color:black}")

        self.horizontalLayout_5.addWidget(self.btn_import)

        self.label_6 = QLabel(self.pg_excel)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_5.addWidget(self.label_6)


        self.verticalLayout_9.addLayout(self.horizontalLayout_5)

        self.Pages.addWidget(self.pg_excel)
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout_2 = QVBoxLayout(self.pg_home)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.pg_home)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(905, 0))
        self.label.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.label)

        self.Pages.addWidget(self.pg_home)

        self.verticalLayout_8.addWidget(self.Pages)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Pages.setCurrentIndex(2)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_inicio.setText(QCoreApplication.translate("MainWindow", u"IN\u00cdCIO", None))
        self.btn_estoque.setText(QCoreApplication.translate("MainWindow", u"ESTOQUE", None))
        self.btn_excel.setText(QCoreApplication.translate("MainWindow", u"EXCEL", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">ESTOQUE</span></p></body></html>", None))
        ___qtreewidgetitem = self.tw_estoque.headerItem()
        ___qtreewidgetitem.setText(8, QCoreApplication.translate("MainWindow", u"Fornecedor", None));
        ___qtreewidgetitem.setText(7, QCoreApplication.translate("MainWindow", u"Setor", None));
        ___qtreewidgetitem.setText(6, QCoreApplication.translate("MainWindow", u"Quantidade_min", None));
        ___qtreewidgetitem.setText(5, QCoreApplication.translate("MainWindow", u"Quantidade", None));
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"Pre\u00e7o_venda", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"Pre\u00e7o_custo", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"Validade", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"C\u00f3digo", None));
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">SA\u00cdDA</span></p></body></html>", None))
        ___qtreewidgetitem1 = self.tw_saida.headerItem()
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("MainWindow", u"Data e Hora", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("MainWindow", u"Quantidade", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"Nome do Produto", None));
        self.btn_add.setText(QCoreApplication.translate("MainWindow", u"Adicionar", None))
        self.btn_remove.setText(QCoreApplication.translate("MainWindow", u"Remover", None))
        self.btn_refresh.setText(QCoreApplication.translate("MainWindow", u"Atualizar", None))
        self.btn_saida.setText(QCoreApplication.translate("MainWindow", u"Sa\u00edda", None))
        self.btn_limpar.setText(QCoreApplication.translate("MainWindow", u"Limpar", None))
        self.btn_grafico.setText(QCoreApplication.translate("MainWindow", u"Gerar Gr\u00e1fico", None))
        self.btn_gerar_excel.setText(QCoreApplication.translate("MainWindow", u"Salvar Excel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tables), QCoreApplication.translate("MainWindow", u"BASE", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"IMPORTAR TABELA", None))
        self.txt_file.setText("")
        self.txt_file.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecione a pasta com os arquivos XML --->", None))
        self.btn_open.setText(QCoreApplication.translate("MainWindow", u"ABRIR", None))
        self.label_4.setText("")
        self.btn_import.setText(QCoreApplication.translate("MainWindow", u"IMPORTAR", None))
        self.label_6.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; color:#13293d;\">PROJETO</span></p><p align=\"center\"><span style=\" font-size:36pt; color:#006494;\">Controle de Estoque</span></p><p align=\"center\"><img src=\":/images/img/home-icon.png\"/></p></body></html>", None))
    # retranslateUi

