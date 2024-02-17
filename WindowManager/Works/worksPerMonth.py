from PySide6.QtWidgets import QWidget, QHeaderView, QCheckBox, QHBoxLayout, QTableWidgetItem, QWidget
from views.workView import worksPerMonthUI
from PySide6.QtCore import Qt, QDate
from PySide6.QtGui import QIcon
from WindowManager.notice import noticeWindow
from WindowManager.error import errorWindow
from exceptions import WorksExceptions
from utils.Factory import Factory
import sys
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class worksPerMonthWindow(QWidget, worksPerMonthUI.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon(resource_path(os.path.join('assets', 'icono-windows.ico'))))
        self.setWindowTitle("DualD - Trabajos del mes")
        self.factory = Factory()
        self.originalTexts = {}
        self.month = None
        self.year = None
        self.tableWidget.setVisible(False)
        self.tableWidget.horizontalHeader().setStyleSheet("""
        QHeaderView::section {
            background-color: lightgray;
            padding: 4px;
            border: none;
            border-bottom: 2px solid black;
            font-weight: bold;
        }
        """)
        self.pushButton.clicked.connect(self._show_work_list_per_month)
       
    def _show_work_list_per_month(self):
        self.fecha_ingreso = self.dateEdit.date()
        self.month = self.fecha_ingreso.month()
        self.year = self.fecha_ingreso.year()
        works = self.factory.get_controller('workController').list_works_per_month(self.month, self.year)
        
        self.tableWidget.setRowCount(len(works))
        for index in range(len(works)):
            self.tableWidget.setItem(index, 0, worksPerMonthUI.QTableWidgetItem(works[index][4]))
            self.tableWidget.setItem(index, 1, worksPerMonthUI.QTableWidgetItem(works[index][5]))
            self.tableWidget.setItem(index, 2, worksPerMonthUI.QTableWidgetItem(str(works[index][2])))
            self.tableWidget.setItem(index, 3, worksPerMonthUI.QTableWidgetItem(str(works[index][3])))
            self.tableWidget.setItem(index, 4, worksPerMonthUI.QTableWidgetItem(works[index][6]))
            self.tableWidget.setItem(index, 5, worksPerMonthUI.QTableWidgetItem(works[index][7]))
        
        header = self.tableWidget.horizontalHeader() 
        header.setMinimumSectionSize(117)
        header.setSectionResizeMode(QHeaderView.Stretch)
        
        self.tableWidget.setVisible(True)
    
    def _close_window(self):
        self.close()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self._close_window()
        if event.key() in (Qt.Key_Return, Qt.Key_Enter):
            self._show_work_list_per_month()
        super().keyPressEvent(event)