# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainScene.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QGridLayout, QHeaderView,
    QMainWindow, QMenu, QMenuBar, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionNuevo_Cliente = QAction(MainWindow)
        self.actionNuevo_Cliente.setObjectName(u"actionNuevo_Cliente")
        self.actionEliminar_Cliente = QAction(MainWindow)
        self.actionEliminar_Cliente.setObjectName(u"actionEliminar_Cliente")
        self.actionActualizar_informacion = QAction(MainWindow)
        self.actionActualizar_informacion.setObjectName(u"actionActualizar_informacion")
        self.actionBuscar_Cliente = QAction(MainWindow)
        self.actionBuscar_Cliente.setObjectName(u"actionBuscar_Cliente")
        self.actionListar_todos_los_Clientes = QAction(MainWindow)
        self.actionListar_todos_los_Clientes.setObjectName(u"actionListar_todos_los_Clientes")
        self.actionNuevo_Trabajo = QAction(MainWindow)
        self.actionNuevo_Trabajo.setObjectName(u"actionNuevo_Trabajo")
        self.actionActualizar_informacion_2 = QAction(MainWindow)
        self.actionActualizar_informacion_2.setObjectName(u"actionActualizar_informacion_2")
        self.actionEliminar_Trabajo = QAction(MainWindow)
        self.actionEliminar_Trabajo.setObjectName(u"actionEliminar_Trabajo")
        self.actionHistorial_de_trabajos = QAction(MainWindow)
        self.actionHistorial_de_trabajos.setObjectName(u"actionHistorial_de_trabajos")
        self.actionBuscar_Trabajo = QAction(MainWindow)
        self.actionBuscar_Trabajo.setObjectName(u"actionBuscar_Trabajo")
        self.actionHistorial_de_Gastos = QAction(MainWindow)
        self.actionHistorial_de_Gastos.setObjectName(u"actionHistorial_de_Gastos")
        self.actionCalcular_ganancias = QAction(MainWindow)
        self.actionCalcular_ganancias.setObjectName(u"actionCalcular_ganancias")
        self.actionCalcular_gastos = QAction(MainWindow)
        self.actionCalcular_gastos.setObjectName(u"actionCalcular_gastos")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEnabled(False)
        self.tableWidget.setMinimumSize(QSize(782, 539))
        self.tableWidget.setAcceptDrops(False)
        self.tableWidget.setAutoFillBackground(True)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(100)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(260)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuMenu_Clientes = QMenu(self.menubar)
        self.menuMenu_Clientes.setObjectName(u"menuMenu_Clientes")
        self.menuMenu_Gastos_Ganancias = QMenu(self.menubar)
        self.menuMenu_Gastos_Ganancias.setObjectName(u"menuMenu_Gastos_Ganancias")
        self.menuMenu_Trabajos = QMenu(self.menubar)
        self.menuMenu_Trabajos.setObjectName(u"menuMenu_Trabajos")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMenu_Clientes.menuAction())
        self.menubar.addAction(self.menuMenu_Trabajos.menuAction())
        self.menubar.addAction(self.menuMenu_Gastos_Ganancias.menuAction())
        self.menuMenu_Clientes.addAction(self.actionNuevo_Cliente)
        self.menuMenu_Clientes.addSeparator()
        self.menuMenu_Clientes.addAction(self.actionEliminar_Cliente)
        self.menuMenu_Clientes.addSeparator()
        self.menuMenu_Clientes.addAction(self.actionActualizar_informacion)
        self.menuMenu_Clientes.addSeparator()
        self.menuMenu_Clientes.addAction(self.actionBuscar_Cliente)
        self.menuMenu_Clientes.addSeparator()
        self.menuMenu_Clientes.addAction(self.actionListar_todos_los_Clientes)
        self.menuMenu_Clientes.addSeparator()
        self.menuMenu_Gastos_Ganancias.addAction(self.actionHistorial_de_Gastos)
        self.menuMenu_Gastos_Ganancias.addSeparator()
        self.menuMenu_Gastos_Ganancias.addAction(self.actionCalcular_ganancias)
        self.menuMenu_Gastos_Ganancias.addSeparator()
        self.menuMenu_Gastos_Ganancias.addAction(self.actionCalcular_gastos)
        self.menuMenu_Gastos_Ganancias.addSeparator()
        self.menuMenu_Trabajos.addAction(self.actionNuevo_Trabajo)
        self.menuMenu_Trabajos.addSeparator()
        self.menuMenu_Trabajos.addAction(self.actionActualizar_informacion_2)
        self.menuMenu_Trabajos.addSeparator()
        self.menuMenu_Trabajos.addAction(self.actionEliminar_Trabajo)
        self.menuMenu_Trabajos.addSeparator()
        self.menuMenu_Trabajos.addAction(self.actionHistorial_de_trabajos)
        self.menuMenu_Trabajos.addSeparator()
        self.menuMenu_Trabajos.addAction(self.actionBuscar_Trabajo)
        self.menuMenu_Trabajos.addSeparator()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionNuevo_Cliente.setText(QCoreApplication.translate("MainWindow", u"Nuevo Cliente", None))
        self.actionEliminar_Cliente.setText(QCoreApplication.translate("MainWindow", u"Eliminar Cliente", None))
        self.actionActualizar_informacion.setText(QCoreApplication.translate("MainWindow", u"Actualizar informacion", None))
        self.actionBuscar_Cliente.setText(QCoreApplication.translate("MainWindow", u"Buscar Cliente", None))
        self.actionListar_todos_los_Clientes.setText(QCoreApplication.translate("MainWindow", u"Listar todos los Clientes", None))
        self.actionNuevo_Trabajo.setText(QCoreApplication.translate("MainWindow", u"Nuevo Trabajo", None))
        self.actionActualizar_informacion_2.setText(QCoreApplication.translate("MainWindow", u"Actualizar informacion", None))
        self.actionEliminar_Trabajo.setText(QCoreApplication.translate("MainWindow", u"Eliminar Trabajo", None))
        self.actionHistorial_de_trabajos.setText(QCoreApplication.translate("MainWindow", u"Historial de trabajos", None))
        self.actionBuscar_Trabajo.setText(QCoreApplication.translate("MainWindow", u"Buscar Trabajo", None))
        self.actionHistorial_de_Gastos.setText(QCoreApplication.translate("MainWindow", u"Historial de gastos", None))
        self.actionCalcular_ganancias.setText(QCoreApplication.translate("MainWindow", u"Calcular ganancias", None))
        self.actionCalcular_gastos.setText(QCoreApplication.translate("MainWindow", u"Calcular gastos", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Id Cliente", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nombre Completo", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Telefono", None));
        self.menuMenu_Clientes.setTitle(QCoreApplication.translate("MainWindow", u"Menu Clientes", None))
        self.menuMenu_Gastos_Ganancias.setTitle(QCoreApplication.translate("MainWindow", u"Menu Gastos/Ganancias", None))
        self.menuMenu_Trabajos.setTitle(QCoreApplication.translate("MainWindow", u"Menu Trabajos", None))
    # retranslateUi

