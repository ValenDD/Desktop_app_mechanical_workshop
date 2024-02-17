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
from WindowManager.Works.worksPerMonth import worksPerMonthWindow
from WindowManager.Expenses.historyPayment import historyPaymentWindow
from WindowManager.Expenses.calculateGains import calculateGainsWindow
from WindowManager.Expenses.newExpense import newExpenseWindow
from utils import client_table_creation
from utils import work_table_creation
from utils import expenses_table_creation
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
        expenses_table_creation.create_tables_if_not_exist()
        

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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())