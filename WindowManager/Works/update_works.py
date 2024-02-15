from PySide6.QtWidgets import QWidget, QHeaderView, QCheckBox, QHBoxLayout, QTableWidgetItem, QWidget
from views.workView import updateWorkUI
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from WindowManager.error import errorWindow
from exceptions import exceptions
from utils.Factory import Factory

class updateWorkWindow(QWidget, updateWorkUI.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('./assets/icono-windows.png'))
        self.setWindowTitle("DualD - Actualizar Trabajo")
        self.factory = Factory()
        self.tableWidget.horizontalHeader().setStyleSheet("""
        QHeaderView::section {
            background-color: lightgray;
            padding: 4px;
            border: none;
            border-bottom: 2px solid black;
            font-weight: bold;
        }
        """)
        self.tableWidget.setVisible(False)
        self.Aceptar_button.setVisible(False)
        self.Cancelar_button.setVisible(False)
        self.checkBox.setVisible(False)
        self.dateEdit.setVisible(False)
        self.dateEdit_2.setVisible(False)
        self.label.setVisible(False)
        self.label_10.setVisible(False)
        self.label_5.setVisible(False)
        self.label_9.setVisible(False)
        self.label_4.setVisible(False)
        self.textEdit.setVisible(False)
        self.textEdit_2.setVisible(False)
        self.textEdit_3.setVisible(False)
        self.lineEdit.setVisible(False)
        self.lineEdit_2.setVisible(False)
        self.lineEdit_3.setVisible(False)
        self.lineEdit_4.setVisible(False)
        self.lineEdit_5.setVisible(False)
        self.label_2.setVisible(False)
        self.label_3.setVisible(False)
        self.label_6.setVisible(False)
        self.label_7.setVisible(False)
        self.label_8.setVisible(False)
        
        self.pushButton.clicked.connect(self._search_client_works)
        
    def _search_client_works(self):
        self.tableWidget.resizeRowsToContents()
        
        client_name = self.lineEdit_6.text().strip()
        works = self.factory.get_controller('workController').search_client_works(client_name)

        self.tableWidget.setRowCount(len(works))
        for i in range(len(works)):
            checkBox = QCheckBox()
            checkBox.stateChanged.connect(lambda state, row=i: self._onCheckBoxChanged(row, state))
            widget = QWidget()
            layout = QHBoxLayout(widget)
            layout.addWidget(checkBox)
            layout.setAlignment(Qt.AlignCenter)
            layout.setContentsMargins(0, 0, 0, 0)
            widget.setLayout(layout)
            
            self.tableWidget.setCellWidget(i, 0, widget)
            self.tableWidget.setItem(i, 1, updateWorkUI.QTableWidgetItem(works[i][5]))
            self.tableWidget.setItem(i, 2, updateWorkUI.QTableWidgetItem(str(works[i][2])))
            self.tableWidget.setItem(i, 3, updateWorkUI.QTableWidgetItem(str(works[i][3])))
            self.tableWidget.setItem(i, 4, updateWorkUI.QTableWidgetItem(works[i][6]))
            self.tableWidget.setItem(i, 5, updateWorkUI.QTableWidgetItem(works[i][7]))
            self.tableWidget.setItem(i, 6, updateWorkUI.QTableWidgetItem(str(works[i][8])))
            self.tableWidget.setItem(i, 7, updateWorkUI.QTableWidgetItem(str(works[i][9])))
            self.tableWidget.setItem(i, 8, updateWorkUI.QTableWidgetItem(str(works[i][10])))
            self.tableWidget.setItem(i, 9, updateWorkUI.QTableWidgetItem(str(works[i][11])))
            self.tableWidget.setItem(i, 10, updateWorkUI.QTableWidgetItem(str(works[i][12])))
            
        self.tableWidget.setVisible(True)
        
        self.lineEdit_6.textChanged.connect(self._clear_table)
        
    def _clear_table(self):
        self.tableWidget.clear()
        self.tableWidget.setVisible(False)
        self.horizontalLayout.setVisible(False)
        self.gridLayout_4.setVisible(False)
        self.gridLayout_6.setVisible(False)
        
    def _onCheckBoxChanged(self, row, state):
        if state == Qt.Checked:
            for i in range(self.tableWidget.rowCount()):
                if i != row:
                    widget = self.tableWidget.cellWidget(i, 0)
                    if widget is not None:
                        checkBox = widget.findChild(QCheckBox)
                        if checkBox is not None:
                            checkBox.setChecked(False)
                            checkBox.setEnabled(False)
             
            values = self.onRowSelected(row)
            self.lineEdit.setText(values[1])
            self.lineEdit_2.setText(values[2])

            
        else:
            for i in range(self.tableWidget.rowCount()):
                widget = self.tableWidget.cellWidget(i, 0)
                if widget is not None:
                    checkBox = widget.findChild(QCheckBox)
                    if checkBox is not None:
                        checkBox.setEnabled(True)
    
    def onRowSelected(self, row):
        values = []
        for column in range(self.tableWidget.columnCount()):
            item = self.tableWidget.item(row, column)
            if item is not None:
                values.append(item.text())
            else:
                values.append("")