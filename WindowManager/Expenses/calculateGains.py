from views.expensesView import calculateGainsUI
from PySide6.QtGui import QIcon, Qt
from PySide6.QtWidgets import QWidget, QHeaderView, QWidget
from utils.Factory import Factory
import sys
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class calculateGainsWindow(QWidget, calculateGainsUI.Ui_Form):
    def __init__(self):
            super().__init__()
            self.setupUi(self)
            self.setWindowIcon(QIcon(resource_path(os.path.join('assets', 'icono-windows.ico'))))
            self.setWindowTitle("DualD - Calculo de Ganancias")
            self.factory = Factory()
            self.month = None
            self.year = None
            self.lineEdit.setVisible(False)
            self.lineEdit.setVisible(False)
            self.lineEdit.setVisible(False)
            self.pushButton.setVisible(False)
            self.pushButton_3.clicked.connect(self._calculate_gains)
            self.pushButton.clicked.connect(self._close_window)
            self.dateEdit.dateChanged.connect(self._clear_fields)
            
    def _calculate_gains(self):
        self.fecha_ingreso = self.dateEdit.date()
        self.month = self.fecha_ingreso.month()
        self.year = self.fecha_ingreso.year()
        expenses = self.factory.get_controller('expensesController').calcualte_gains(self.month, self.year)
        
        self.lineEdit.setText(str(expenses))
        self.lineEdit_2.setText(str(expenses / 2))
        self.lineEdit_3.setText(str(expenses / 2))
        self.lineEdit.setVisible(True)
        self.lineEdit_2.setVisible(True)
        self.lineEdit_3.setVisible(True)
        self.pushButton.setVisible(True)
        
    def _clear_fields(self):
        self.lineEdit.setVisible(False)
        self.lineEdit_2.setVisible(False)
        self.lineEdit_3.setVisible(False)
        self.pushButton.setVisible(False)
    
    def _close_window(self):
        self.close()
    
    def keyPressEvent(self, event):
        if event.key() in (Qt.Key_Return, Qt.Key_Enter):
            self._calculate_gains()
        
        if event.key() == Qt.Key_Escape:
            self._close_window()
        super().keyPressEvent(event)