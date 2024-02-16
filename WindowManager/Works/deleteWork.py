from PySide6.QtWidgets import QWidget, QHeaderView, QCheckBox, QHBoxLayout, QTableWidgetItem, QWidget
from views.workView import deleteWorkUI
from PySide6.QtCore import Qt, QDate
from PySide6.QtGui import QIcon
from WindowManager.notice import noticeWindow
from WindowManager.error import errorWindow
from exceptions import WorksExceptions
from utils.Factory import Factory

class deleteWorkWindow(QWidget, deleteWorkUI.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('./assets/icono-windows.png'))
        self.setWindowTitle("DualD - Eliminar Trabajo")
        self.factory = Factory()
        self.currentCheckBox = None
        self.work_id = None
        self.originalTexts = {}
        self.client_name = None
        self.hasChanged = False
        
        self.tableWidget.horizontalHeader().setStyleSheet("""
        QHeaderView::section {
            background-color: lightgray;
            padding: 4px;
            border: none;
            border-bottom: 2px solid black;
            font-weight: bold;
        }
        """)
        
        self.Aceptar_button.setVisible(False)
        self.Cancelar_button.setVisible(False)
        self.tableWidget.setVisible(False)
        
        self.pushButton.clicked.connect(self._search_work)
        self.Aceptar_button.clicked.connect(self._delete_work)
        self.Cancelar_button.clicked.connect(self._close_window)
        
    def _search_work(self):
        if(self.lineEdit_6.text().strip() == ""):
            self.error = errorWindow()
            self.error.ErrorLabel.setText("Ingrese un nombre")
            self.error.show()
            return
        else:
            self.client_name = self.lineEdit_6.text().strip()
            works = self.factory.get_controller('workController').search_client_works(self.client_name)
            
            self.tableWidget.setRowCount(len(works))
            
            for i in range(len(works)):
                checkBox = QCheckBox()
                widget = QWidget()
                layout = QHBoxLayout(widget)
                layout.addWidget(checkBox)
                layout.setAlignment(Qt.AlignCenter)
                layout.setContentsMargins(0, 0, 0, 0)
                widget.setLayout(layout)
                
                checkBox.stateChanged.connect(lambda checked, checkBox=checkBox, row=i: self._onCheckBoxChanged(checkBox, row))
            
                self.tableWidget.setCellWidget(i, 0, widget)
                self.tableWidget.setCellWidget(i, 0, widget)
                self.tableWidget.setItem(i, 1, deleteWorkUI.QTableWidgetItem(works[i][5]))
                self.tableWidget.setItem(i, 2, deleteWorkUI.QTableWidgetItem(str(works[i][2])))
                self.tableWidget.setItem(i, 3, deleteWorkUI.QTableWidgetItem(str(works[i][3])))
                self.tableWidget.setItem(i, 4, deleteWorkUI.QTableWidgetItem(works[i][6]))
                self.tableWidget.setItem(i, 5, deleteWorkUI.QTableWidgetItem(works[i][7]))
                self.tableWidget.setItem(i, 6, deleteWorkUI.QTableWidgetItem(str(works[i][8])))
                self.tableWidget.setItem(i, 7, deleteWorkUI.QTableWidgetItem(str(works[i][9])))
                self.tableWidget.setItem(i, 8, deleteWorkUI.QTableWidgetItem(str(works[i][10])))
                self.tableWidget.setItem(i, 9, deleteWorkUI.QTableWidgetItem(str(works[i][11])))
                self.tableWidget.setItem(i, 10, deleteWorkUI.QTableWidgetItem(str(works[i][12])))
            
            header = self.tableWidget.horizontalHeader() 
            header.setMinimumSectionSize(117)
            header.setSectionResizeMode(QHeaderView.Stretch)
            self.tableWidget.setVisible(True)
            self.Aceptar_button.setVisible(True)
            self.Cancelar_button.setVisible(True)
            
            self.lineEdit_6.textChanged.connect(self._resetUI)
        
    def _onCheckBoxChanged(self, checkBox, row):
        if checkBox.isChecked():

            if self.currentCheckBox and self.currentCheckBox != checkBox:
                self.currentCheckBox.setChecked(False)
            self.currentCheckBox = checkBox

            self._displayRowData(row)
        else:
            if self.currentCheckBox == checkBox:
                self.currentCheckBox = None
                
    def _displayRowData(self, row):
        values = []
            
        for column in range(1, self.tableWidget.columnCount()):
            item = self.tableWidget.item(row, column)
            if item is not None:
                values.append(item.text())
            else:
                values.append("")
                
    def _resetUI(self):
        if self.currentCheckBox:
            self.currentCheckBox.setChecked(False)
            self.currentCheckBox = None

        self.tableWidget.setRowCount(0)
        self.tableWidget.setVisible(False)
        
    def _delete_work(self):
        try:
            self.work_controller = self.factory.get_controller('workController')
            self.work_id = self.work_controller.work_id(self.client_name)
            self.factory.get_controller('workController').delete_work(self.work_id[0])
            self._resetUI()
            self.error = noticeWindow()
            self.error.ErrorLabel.setText("El trabajo ha sido eliminado")
            self.error.show()
            self._close_window()
        except WorksExceptions.WorkNotExistException as e:
            self.error = errorWindow()
            self.error.ErrorLabel.setText(str(e))
            self.error.show()
        except Exception as e:
            self.error = errorWindow()
            self.error.ErrorLabel.setText("Seleccione un trabajo")
            self.error.show()
            
    def _close_window(self):
        self.close()
        