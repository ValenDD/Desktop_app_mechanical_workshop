import sys
from dotenv import load_dotenv
import os
from PySide6.QtWidgets import QApplication, QMainWindow
from views import mainScene
from utils.Factory import Factory
from utils import table_creation
from utils import dbconection

class MainWindow(QMainWindow, mainScene.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        load_dotenv()
        # Configura tu DSN de PostgreSQL aquí
        dbname = os.getenv('DB_NAME')
        user = os.getenv('DB_USER')
        password = os.getenv('DB_PASSWORD')
        host = os.getenv('DB_HOST') 
        port = os.getenv('DB_PORT') 
        dbconection.create_database_if_not_exists(dbname, user, password, host, port)
        table_creation.create_tables_if_not_exist()

        #Test
        self.factory = Factory()
        self.client_controller = self.factory.get_controller('clientController')
        self.client_controller.create_user('Pepe', '1234567890')

        
        # Aquí puedes conectar botones o acciones para crear usuarios, etc.
        # Por ejemplo:
        # self.miBotonCrearUsuario.clicked.connect(self.crear_usuario)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec())