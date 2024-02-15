# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'clientListWindowUI.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QGridLayout, QHeaderView,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(496, 255)
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.Table = QTableWidget(Form)
        if (self.Table.columnCount() < 2):
            self.Table.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.Table.setObjectName(u"Table")
        self.Table.setMouseTracking(True)
        self.Table.setAutoFillBackground(True)
        self.Table.setLineWidth(2)
        self.Table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.Table.setAlternatingRowColors(True)
        self.Table.setGridStyle(Qt.SolidLine)
        self.Table.setSortingEnabled(True)
        self.Table.setColumnCount(2)
        self.Table.horizontalHeader().setDefaultSectionSize(237)
        self.Table.horizontalHeader().setStretchLastSection(False)

        self.gridLayout.addWidget(self.Table, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        ___qtablewidgetitem = self.Table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"NOMBRE Y APELLIDO", None));
        ___qtablewidgetitem1 = self.Table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"TELEFONO", None));
    # retranslateUi

