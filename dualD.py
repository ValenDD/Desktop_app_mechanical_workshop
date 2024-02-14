import sys
from dotenv import load_dotenv
import os
from PySide6.QtWidgets import QApplication, QMainWindow
from views import mainSceneUI
from WindowManager.newClient import newClientWindow
from views.clientView import *
from WindowManager.clientList import clientListWindow
from utils import table_creation
from utils import dbconection
from PySide6.QtGui import QIcon

class MainWindow(QMainWindow, mainSceneUI.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('./assets/icono-windows.png'))
        self.setWindowTitle("DualD - Sistema de gestión de clientes")
        load_dotenv()
        # Configura tu DSN de PostgreSQL aquí
        dbname = os.getenv('DB_NAME')
        user = os.getenv('DB_USER')
        password = os.getenv('DB_PASSWORD')
        host = os.getenv('DB_HOST') 
        port = os.getenv('DB_PORT') 
        dbconection.create_database_if_not_exists(dbname, user, password, host, port)
        table_creation.create_tables_if_not_exist()

        #Action Connect
        self.actionNuevo_Cliente.triggered.connect(self.show_new_client_windows)
        self.actionListar_todos_los_Clientes.triggered.connect(self.show_client_list)
        # Aquí puedes conectar botones o acciones para crear usuarios, etc.

    def show_new_client_windows(self):
        self.new_client = newClientWindow()
        self.new_client.show()
        
    def show_client_list(self):
        self.client_list = clientListWindow()
        self.client_list.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())