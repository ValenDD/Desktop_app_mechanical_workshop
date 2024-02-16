import sys
from dotenv import load_dotenv
import os
from PySide6.QtWidgets import QApplication, QMainWindow
from views import mainSceneUI
from WindowManager.Client.newClient import newClientWindow
from views.clientView import *
from WindowManager.Client.clientList import clientListWindow
from WindowManager.Client.update_search_client import updateSearchClient
from WindowManager.Client.findDeleteClient import findDeleteClientWindow
from WindowManager.Works.newWork import newWorkWindow
from WindowManager.Works.historialWorksAll import historialWorksWindow
from WindowManager.Works.deleteWork import deleteWorkWindow
from WindowManager.Works.update_works import updateWorkWindow
from utils import client_table_creation
from utils import work_table_creation
from utils import dbconection
from PySide6.QtGui import QIcon, QPixmap

class MainWindow(QMainWindow, mainSceneUI.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('./assets/icono-windows.png'))
        self.setWindowTitle("DualD - Sistema de gestión de clientes")
        self.label.setPixmap(QPixmap(u"./assets/fondo-MainScene.png"))
        load_dotenv()
        # Configura tu DSN de PostgreSQL aquí
        dbname = os.getenv('DB_NAME')
        user = os.getenv('DB_USER')
        password = os.getenv('DB_PASSWORD')
        host = os.getenv('DB_HOST') 
        port = os.getenv('DB_PORT') 
        dbconection.create_database_if_not_exists(dbname, user, password, host, port)
        client_table_creation.create_tables_if_not_exist()
        work_table_creation.create_tables_if_not_exist()

        self.actionNuevo_Cliente.triggered.connect(self._show_new_client_windows)
        self.actionListar_todos_los_Clientes.triggered.connect(self._show_client_list)
        self.actionActualizar_informacion.triggered.connect(self._show_find_client_window)
        self.actionEliminar_Cliente.triggered.connect(self._show_delete_client_window)
        
        self.actionNuevo_Trabajo.triggered.connect(self._show_new_work_window)
        self.actionHistorial_de_trabajos.triggered.connect(self._show_work_list)
        self.actionActualizar_informacion_2.triggered.connect(self._show_update_work_window)
        self.actionEliminar_Trabajo.triggered.connect(self._show_delete_work_window)
        
    # Work
    def _show_update_work_window(self):
        self.update_work = updateWorkWindow()
        self.update_work.show()
        
    def _show_work_list(self):
        self.historial_works = historialWorksWindow()
        self.historial_works.show()

    def _show_new_work_window(self):
        self.new_work = newWorkWindow()
        self.new_work.show()
    
    def _show_delete_work_window(self):
        self.delete_work = deleteWorkWindow()
        self.delete_work.show()
    
    # Client
    def _show_delete_client_window(self):
        self.findDelete_client = findDeleteClientWindow()
        self.findDelete_client.show()
                
    def _show_find_client_window(self):
        from utils.Factory import Factory
        self.client_controller = Factory().get_controller('clientController')
        self.find_client = updateSearchClient(self.client_controller.list_client_only_name())
        self.find_client.show()

    def _show_new_client_windows(self):
        self.new_client = newClientWindow()
        self.new_client.show()
        
    def _show_client_list(self):
        self.client_list = clientListWindow()
        self.client_list.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())