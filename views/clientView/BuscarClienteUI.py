# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BuscarClienteUI.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(450, 217)
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.Nombre_line_edit = QLineEdit(Form)
        self.Nombre_line_edit.setObjectName(u"Nombre_line_edit")

        self.gridLayout_2.addWidget(self.Nombre_line_edit, 0, 1, 1, 1)

        

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.Apellido_line_edit = QLineEdit(Form)
        self.Apellido_line_edit.setObjectName(u"Apellido_line_edit")

        self.gridLayout_2.addWidget(self.Apellido_line_edit, 1, 1, 1, 1)

        self.Buscar_Usuarios = QPushButton(Form)
        self.Buscar_Usuarios.setObjectName(u"Buscar_Usuarios")

        self.gridLayout_2.addWidget(self.Buscar_Usuarios, 2, 1, 1, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.Buscar_Usuarios.setText(QCoreApplication.translate("Form", u"Buscar", None))
        self.label.setText(QCoreApplication.translate("Form", u"Nombre", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Apellidos", None))
    # retranslateUi

