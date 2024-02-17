from PySide6.QtWidgets import QWidget, QHeaderView
from views.workView import historialWorksUI
from PySide6.QtGui import QIcon, Qt
from utils.Factory import Factory
import sys
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class historialWorksWindow(QWidget, historialWorksUI.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon(resource_path(os.path.join('assets', 'icono-windows.ico'))))
        self.setWindowTitle("DualD - Historico de Trabajos")
        
        self.tableWidget.horizontalHeader().setStyleSheet("""
        QHeaderView::section {
            background-color: lightgray;
            padding: 4px;
            border: none;
            border-bottom: 2px solid black;
            font-weight: bold;
        }
        """)
        
        for column in range(3):
            self.tableWidget.resizeColumnToContents(column)
            
        self.factory = Factory()
        self.work_controller = self.factory.get_controller('workController')
        works = self.work_controller.list_works()
        self._add_works_to_table(works)

    def _add_works_to_table(self, works):
        self.tableWidget.setRowCount(len(works))
        for i in range(len(works)):
            self.tableWidget.setItem(i, 0, historialWorksUI.QTableWidgetItem(works[i][4]))
            self.tableWidget.setItem(i, 1, historialWorksUI.QTableWidgetItem(works[i][5]))
            self.tableWidget.setItem(i, 2, historialWorksUI.QTableWidgetItem(str(works[i][2])))
            self.tableWidget.setItem(i, 3, historialWorksUI.QTableWidgetItem(str(works[i][3])))
            self.tableWidget.setItem(i, 4, historialWorksUI.QTableWidgetItem(works[i][6]))
            self.tableWidget.setItem(i, 5, historialWorksUI.QTableWidgetItem(works[i][7]))
            self.tableWidget.setItem(i, 6, historialWorksUI.QTableWidgetItem(str(works[i][8])))
            self.tableWidget.setItem(i, 7, historialWorksUI.QTableWidgetItem(str(works[i][9])))
            self.tableWidget.setItem(i, 8, historialWorksUI.QTableWidgetItem(str(works[i][10])))
            self.tableWidget.setItem(i, 9, historialWorksUI.QTableWidgetItem(str(works[i][11])))
            self.tableWidget.setItem(i, 10, historialWorksUI.QTableWidgetItem(str(works[i][12])))
            
        header = self.tableWidget.horizontalHeader() 
        header.setMinimumSectionSize(117)
        header.setSectionResizeMode(QHeaderView.Stretch)
            
    def _close_window(self):
        self.close()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self._close_window()
        super().keyPressEvent(event)