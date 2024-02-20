import sys
from dotenv import load_dotenv
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QInputDialog
from views import mainSceneUI
from PySide6.QtCore import Qt
from WindowManager.Client.newClient import newClientWindow
from views.clientView import *
from WindowManager.Client.clientList import clientListWindow
from WindowManager.Client.update_search_client import updateSearchClient
from WindowManager.Client.findDeleteClient import findDeleteClientWindow
from WindowManager.Works.newWork import newWorkWindow
from WindowManager.Works.historialWorksAll import historialWorksWindow
from WindowManager.Works.deleteWork import deleteWorkWindow
from WindowManager.Works.update_works import updateWorkWindow
from WindowManager.Works.worksPerMonth import worksPerMonthWindow
from WindowManager.Expenses.historyPayment import historyPaymentWindow
from WindowManager.Expenses.calculateGains import calculateGainsWindow
from WindowManager.Expenses.newExpense import newExpenseWindow
from utils import client_table_creation
from utils import work_table_creation
from utils import expenses_table_creation
from utils import dbconection
from PySide6.QtGui import QIcon, QPixmap
from utils import backup_database

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
class MainWindow(QMainWindow, mainSceneUI.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.db_name = None
        self.db_user = None
        self.db_password = None
        self.db_host = None
        self.db_port = None
        self.setWindowIcon(QIcon(resource_path(os.path.join('assets', 'icono-windows.ico'))))
        self.setWindowTitle("DualD - Sistema de gestión de clientes")
        self.label.setPixmap(QPixmap(resource_path(os.path.join('assets', 'fondo-MainScene.png'))))

        self.load_configuration() 
        self.environment_variables()
        self.get_configuration()
        
        self.actionNuevo_Cliente.triggered.connect(self._show_new_client_windows)
        self.actionListar_todos_los_Clientes.triggered.connect(self._show_client_list)
        self.actionActualizar_informacion.triggered.connect(self._show_find_client_window)
        self.actionEliminar_Cliente.triggered.connect(self._show_delete_client_window)
        
        self.actionNuevo_Trabajo.triggered.connect(self._show_new_work_window)
        self.actionHistorial_de_trabajos.triggered.connect(self._show_work_list)
        self.actionActualizar_informacion_2.triggered.connect(self._show_update_work_window)
        self.actionEliminar_Trabajo.triggered.connect(self._show_delete_work_window)
        self.actionHistorial_de_trabajos_mensuales.triggered.connect(self._show_work_list_per_month)
        
        self.actionHistorial_de_pagos.triggered.connect(self._show_history_payment)
        self.actionCalcular_ganancias.triggered.connect(self._show_calculate_gains)
        self.actionIngresar_pago.triggered.connect(self._show_new_expense)
        
        self.actionRespaldar.triggered.connect(self._backup)
    
    # Backup
    def _backup(self):
        backup_database.do_backup(self.db_name, self.db_user, self.db_password, self.db_host, self.db_port)
        
    # Expeses
    def _show_history_payment(self):
        self.history_payment = historyPaymentWindow()
        self.history_payment.show()
        
    def _show_calculate_gains(self):
        self.calculate_gains = calculateGainsWindow()
        self.calculate_gains.show()
    
    def _show_new_expense(self):
        self.new_expense = newExpenseWindow()
        self.new_expense.show()
        
    # Works
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
    
    def _show_work_list_per_month(self):
        self.works_per_month = worksPerMonthWindow()
        self.works_per_month.show()
        
    # Client
    def _show_delete_client_window(self):
        self.findDelete_client = findDeleteClientWindow()
        self.findDelete_client.show()
                
    def _show_find_client_window(self):
        self.find_client = updateSearchClient()
        self.find_client.show()

    def _show_new_client_windows(self):
        self.new_client = newClientWindow()
        self.new_client.show()
        
    def _show_client_list(self):
        self.client_list = clientListWindow()
        self.client_list.show()

    def _close_window(self):
        self.close()
    
    def keyPressEvent(self, event):        
        if event.key() in (Qt.Key_Return, Qt.Key_Escape):
            self._close_window()
        super().keyPressEvent(event)

    def environment_variables(self):
        load_dotenv()

    def get_configuration(self):
        self.db_name = os.getenv('DB_NAME')
        self.db_user = os.getenv('DB_USER')
        self.db_password = os.getenv('DB_PASSWORD')
        self.db_host = os.getenv('DB_HOST')
        self.db_port = os.getenv('DB_PORT')
        
        dbconection.create_database_if_not_exists(self.db_name, self.db_user, self.db_password, self.db_host, self.db_port)
        client_table_creation.create_tables_if_not_exist(self.db_name, self.db_user, self.db_password, self.db_host, self.db_port)
        work_table_creation.create_tables_if_not_exist(self.db_name, self.db_user, self.db_password, self.db_host, self.db_port)
        expenses_table_creation.create_tables_if_not_exist(self.db_name, self.db_user, self.db_password, self.db_host, self.db_port)

    def set_config(self):
        
        print("Configurando la aplicación por primera vez...")
    
        db_name, ok = QInputDialog.getText(self, "Configuración", "Ingrese el nombre de la base de datos:")
        if ok and db_name:
            db_user, ok = QInputDialog.getText(self, "Configuración", "Ingrese el usuario de la base de datos:")
        if ok and db_user:
            db_password, ok = QInputDialog.getText(self, "Configuración", "Ingrese la contraseña de la base de datos:")
        if ok and db_password:
            db_host, ok = QInputDialog.getText(self, "Configuración", "Ingrese el host de la base de datos:")
        if ok and db_host:
            db_port, ok = QInputDialog.getText(self, "Configuración", "Ingrese el puerto de la base de datos:")
        if ok and db_port:
            
            with open('.env', 'w') as f:
                f.write(f"DB_NAME={db_name}\n")
                f.write(f"DB_USER={db_user}\n")
                f.write(f"DB_PASSWORD={db_password}\n")
                f.write(f"DB_HOST={db_host}\n")
                f.write(f"DB_PORT={db_port}\n")

    def load_configuration(self):
        if not os.path.exists('.env'):
            self.set_config()
        load_dotenv()


        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())