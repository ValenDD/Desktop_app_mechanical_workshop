import sys
from dotenv import load_dotenv
import os
from PySide6.QtWidgets import QApplication, QMainWindow
from views import mainScene
from views.clientView import newClient
from newClient import newClientWindow
from utils import table_creation
from utils import dbconection
from PySide6.QtGui import QIcon

class MainWindow(QMainWindow, mainScene.Ui_MainWindow):
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

        # Aquí puedes conectar botones o acciones para crear usuarios, etc.
        # Por ejemplo:
        # self.miBotonCrearUsuario.clicked.connect(self.crear_usuario)

    def show_new_client_windows(self):
        self.new_client = newClientWindow()
        self.new_client.show()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())