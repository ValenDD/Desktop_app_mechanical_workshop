# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NewClient.ui'
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
        Form.resize(627, 435)
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.Nombre_line_edit = QLineEdit(Form)
        self.Nombre_line_edit.setObjectName(u"Nombre_line_edit")

        self.gridLayout.addWidget(self.Nombre_line_edit, 2, 5, 1, 1)

        self.Apellido_line_edit = QLineEdit(Form)
        self.Apellido_line_edit.setObjectName(u"Apellido_line_edit")

        self.gridLayout.addWidget(self.Apellido_line_edit, 4, 5, 1, 1)

        self.Telefonos_line_edit = QLineEdit(Form)
        self.Telefonos_line_edit.setObjectName(u"Telefonos_line_edit")

        self.gridLayout.addWidget(self.Telefonos_line_edit, 6, 5, 1, 1)
        
        self.Cancelar_button = QPushButton(Form)
        self.Cancelar_button.setObjectName(u"Cancelar_button")

        self.gridLayout.addWidget(self.Cancelar_button, 7, 3, 1, 1)

        self.Aceptar_button = QPushButton(Form)
        self.Aceptar_button.setObjectName(u"Aceptar_button")

        self.gridLayout.addWidget(self.Aceptar_button, 7, 4, 1, 1)

        self.Telefono_label = QLabel(Form)
        self.Telefono_label.setObjectName(u"Telefono_label")

        self.gridLayout.addWidget(self.Telefono_label, 6, 3, 1, 1)

        self.Apellido_label = QLabel(Form)
        self.Apellido_label.setObjectName(u"Apellido_label")

        self.gridLayout.addWidget(self.Apellido_label, 4, 3, 1, 1)

        self.Nombre_label = QLabel(Form)
        self.Nombre_label.setObjectName(u"Nombre_label")

        self.gridLayout.addWidget(self.Nombre_label, 2, 3, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.Cancelar_button.setText(QCoreApplication.translate("Form", u"Cancelar", None))
        self.Aceptar_button.setText(QCoreApplication.translate("Form", u"Aceptar", None))
        self.Telefono_label.setText(QCoreApplication.translate("Form", u"Telefonos   ", None))
        self.Apellido_label.setText(QCoreApplication.translate("Form", u"Apellidos", None))
        self.Nombre_label.setText(QCoreApplication.translate("Form", u"Nombres", None))
    # retranslateUi

