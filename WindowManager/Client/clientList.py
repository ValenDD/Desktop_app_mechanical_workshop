from PySide6.QtWidgets import QWidget, QHeaderView
from views.clientView import clientListWindowUI
from PySide6.QtGui import QIcon
from utils.Factory import Factory
from PySide6.QtCore import Qt
import sys
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class clientListWindow(QWidget, clientListWindowUI.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon(resource_path(os.path.join('assets', 'icono-windows.ico'))))
        self.setWindowTitle("DualD - Lista de Clientes")
        
        self.Table.horizontalHeader().setStyleSheet("""
        QHeaderView::section {
            background-color: lightgray;
            padding: 4px;
            border: none;
            border-bottom: 2px solid black;
            font-weight: bold;
        }
        """)
        for column in range(3):
            self.Table.resizeColumnToContents(column)

        self.factory = Factory()
        self.client_controller = self.factory.get_controller('clientController')
        clients = self.client_controller.list_clients()
        self.add_client_table(clients)
        header = self.Table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)

    def add_client_table(self, data):
        self.Table.setRowCount(len(data))
        for i in range(len(data)):
            self.Table.setItem(i, 0, clientListWindowUI.QTableWidgetItem(data[i][1]))
            self.Table.setItem(i, 1, clientListWindowUI.QTableWidgetItem(data[i][2]))
        
    def _close_window(self):
        self.close()
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self._close_window()
        super().keyPressEvent(event)