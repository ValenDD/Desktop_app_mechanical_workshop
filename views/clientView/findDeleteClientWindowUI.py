# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'findDeleteClientWindowUI.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(515, 208)
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lista_clientes = QComboBox(Form)
        self.lista_clientes.setObjectName(u"lista_clientes")

        self.gridLayout.addWidget(self.lista_clientes, 0, 1, 1, 1)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.Eliminar_cliente = QPushButton(Form)
        self.Eliminar_cliente.setObjectName(u"Eliminar_cliente")

        self.gridLayout.addWidget(self.Eliminar_cliente, 1, 1, 1, 1)

        self.Cancelar = QPushButton(Form)
        self.Cancelar.setObjectName(u"Cancelar")

        self.gridLayout.addWidget(self.Cancelar, 1, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Seleccione el cliente a ELIMINAR", None))
        self.Eliminar_cliente.setText(QCoreApplication.translate("Form", u"Eliminar", None))
        self.Cancelar.setText(QCoreApplication.translate("Form", u"Cancelar", None))
    # retranslateUi

