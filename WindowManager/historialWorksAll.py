from PySide6.QtWidgets import QWidget, QHeaderView
from views.workView import historialWorksUI
from PySide6.QtGui import QIcon
from utils.Factory import Factory

class historialWorksWindow(QWidget, historialWorksUI.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('./assets/icono-windows.png'))
        self.setWindowTitle("DualD - Lista de Trabajos")
        
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

        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        
        def _add_works_to_table(self, works):
