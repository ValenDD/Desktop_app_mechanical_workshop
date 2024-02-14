from PySide6.QtWidgets import QWidget
from views.clientView import ClientesEntontradosUI
from PySide6.QtGui import QIcon
from utils.Factory import Factory

class findedClientWindow(QWidget, ClientesEntontradosUI.Ui_Form):
    def __init__(self, name):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('./assets/icono-windows.png'))
        self.setWindowTitle("DualD - Clientes Encontrados")
        self.name = name

        self.Table_Clientes_encontrados.horizontalHeader().setStyleSheet("""
            QHeaderView::section {
                background-color: lightgray;
                padding: 4px;
                border: none;
                border-bottom: 2px solid black;
                font-weight: bold;
            }
            """)

        self.factory = Factory()
        self.client_controller = self.factory.get_controller('clientController')
        clients = self.client_controller.find_users(self.name)
        self.add_client_table(clients)


    def add_client_table(self, data):
        self.Table_Clientes_encontrados.setRowCount(len(data))
        for i in range(len(data)):
            self.Table_Clientes_encontrados.setItem(i, 0, ClientesEntontradosUI.QTableWidgetItem(data[i][1]))
            self.Table_Clientes_encontrados.setItem(i, 1, ClientesEntontradosUI.QTableWidgetItem(data[i][2]))
            
