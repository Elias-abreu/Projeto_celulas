# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pagesUWTqHX.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class Ui_application_pages(object):
    def setupUi(self, application_pages):
        if not application_pages.objectName():
            application_pages.setObjectName(u"application_pages")
        application_pages.resize(1209, 780)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.verticalLayout = QVBoxLayout(self.page_1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.page_1)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(500, 70))
        self.frame.setMaximumSize(QSize(500, 70))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setSpacing(4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_4.addWidget(self.label_3)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 36))
        self.lineEdit.setMaximumSize(QSize(16777215, 36))
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(68, 71, 90);\n"
"	padding: 8px;\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.btn_change_text = QPushButton(self.frame)
        self.btn_change_text.setObjectName(u"btn_change_text")
        self.btn_change_text.setMinimumSize(QSize(120, 36))
        self.btn_change_text.setMaximumSize(QSize(16777215, 36))
        self.btn_change_text.setCursor(QCursor(Qt.CrossCursor))
        self.btn_change_text.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(67, 133, 200);\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 0, 127);\n"
"}")

        self.gridLayout.addWidget(self.btn_change_text, 0, 1, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout)


        self.verticalLayout.addWidget(self.frame, 0, Qt.AlignHCenter)

        application_pages.addWidget(self.page_1)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_5 = QVBoxLayout(self.page_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_2 = QFrame(self.page_4)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(150, 300, 161, 51))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(67, 133, 200);\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"")
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(330, 300, 581, 61))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.pushButton_4 = QPushButton(self.frame_3)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(460, 0, 121, 51))
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(68, 71, 90);\n"
"	padding: 8px;\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}")
        self.pushButton_2 = QPushButton(self.frame_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(330, 0, 121, 51))
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(68, 71, 90);\n"
"	padding: 8px;\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}")
        self.pushButton_5 = QPushButton(self.frame_3)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(10, 0, 181, 51))
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(68, 71, 90);\n"
"	padding: 8px;\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}")
        self.pushButton_3 = QPushButton(self.frame_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(200, 0, 121, 51))
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(68, 71, 90);\n"
"	padding: 8px;\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}")

        self.verticalLayout_5.addWidget(self.frame_2)

        application_pages.addWidget(self.page_4)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_2 = QVBoxLayout(self.page_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.page_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        application_pages.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.pushButton_6 = QPushButton(self.page_3)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(190, 690, 121, 61))
        self.pushButton_6.setStyleSheet(u"background-color: rgb(255, 111, 224);\n"
"border-radius: 10px;\n"
"")
        self.pushButton_7 = QPushButton(self.page_3)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(440, 690, 121, 61))
        self.pushButton_7.setStyleSheet(u"background-color: rgb(110, 255, 238);\n"
"border-radius: 10px;\n"
"")
        self.frame_4 = QFrame(self.page_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(300, 150, 201, 501))
        self.frame_4.setStyleSheet(u"background-image: url(:/random/Imagem1.png);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        application_pages.addWidget(self.page_3)

        self.retranslateUi(application_pages)

        QMetaObject.connectSlotsByName(application_pages)
    # setupUi

    def retranslateUi(self, application_pages):
        application_pages.setWindowTitle(QCoreApplication.translate("application_pages", u"StackedWidget", None))
        self.label_3.setText(QCoreApplication.translate("application_pages", u"Ol\u00e1...", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("application_pages", u"Escreva o seu nome", None))
        self.btn_change_text.setText(QCoreApplication.translate("application_pages", u"Alterar Texto", None))
        self.pushButton.setText(QCoreApplication.translate("application_pages", u"CLASSIFICAR", None))
        self.pushButton_4.setText(QCoreApplication.translate("application_pages", u"EDITAR", None))
        self.pushButton_2.setText(QCoreApplication.translate("application_pages", u"EXCLUIR", None))
        self.pushButton_5.setText(QCoreApplication.translate("application_pages", u"SELECIONAR IMAGENS", None))
        self.pushButton_3.setText(QCoreApplication.translate("application_pages", u"SALVAR", None))
        self.label_2.setText(QCoreApplication.translate("application_pages", u"P\u00e1gina 2", None))
        self.pushButton_6.setText(QCoreApplication.translate("application_pages", u"CELECINORAR", None))
        self.pushButton_7.setText(QCoreApplication.translate("application_pages", u"CELECINORAR", None))
    # retranslateUi

