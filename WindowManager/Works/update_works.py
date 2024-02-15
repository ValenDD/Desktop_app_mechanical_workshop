from PySide6.QtWidgets import QWidget, QHeaderView, QCheckBox, QHBoxLayout, QTableWidgetItem, QWidget
from views.workView import updateWorkUI
from PySide6.QtCore import Qt, QDate
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
        self.currentCheckBox = None
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
        self.checkBox_2.setVisible(False)
        
        self.pushButton.clicked.connect(self._search_client_works)
        
    def _search_client_works(self):
        client_name = self.lineEdit_6.text().strip()
        works = self.factory.get_controller('workController').search_client_works(client_name)

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
        self.checkBox_2.setVisible(False)
        self._clearDisplayFields()
 
    def _onCheckBoxChanged(self, checkBox, row):
        if checkBox.isChecked():

            if self.currentCheckBox and self.currentCheckBox != checkBox:
                self.currentCheckBox.setChecked(False)
            self.currentCheckBox = checkBox

            self._displayRowData(row)
        else:
            if self.currentCheckBox == checkBox:
                self.currentCheckBox = None
                self._clearDisplayFields()

    def _displayRowData(self, row):
        values = []
        for column in range(1, self.tableWidget.columnCount()):
            item = self.tableWidget.item(row, column)
            if item is not None:
                values.append(item.text())
            else:
                values.append("")

        dateFormat = "dd/MM/yyyy"
        
        fechaIngreso = QDate.fromString(values[1], dateFormat)
        fechaEgreso = QDate.fromString(values[2], dateFormat)

        client_name = self.lineEdit_6.text().strip()
        self.lineEdit.setText(client_name)
        self.lineEdit_2.setText(values[0])
        self.lineEdit_3.setText(values[5])
        self.lineEdit_4.setText(values[6])
        self.lineEdit_5.setText(values[7])
        
        if fechaIngreso.isValid():
            self.dateEdit_2.setDate(fechaIngreso)
        if fechaEgreso.isValid():
            self.dateEdit.setDate(fechaEgreso)
        self.textEdit.setText(values[3])
        self.textEdit_2.setText(values[4])
        self.textEdit_3.setText(values[8])
        
        self.checkBox.setChecked(values[8].lower() == 'true')
        
        self._see_windows()
        

    def _see_windows(self):
        self.Aceptar_button.setVisible(True)
        self.Cancelar_button.setVisible(True)
        self.checkBox.setVisible(True)
        self.dateEdit.setVisible(True)
        self.dateEdit_2.setVisible(True)
        self.label.setVisible(True)
        self.label_10.setVisible(True)
        self.label_5.setVisible(True)
        self.label_9.setVisible(True)
        self.label_4.setVisible(True)
        self.textEdit.setVisible(True)
        self.textEdit_2.setVisible(True)
        self.textEdit_3.setVisible(True)
        self.lineEdit.setVisible(True)
        self.lineEdit_2.setVisible(True)
        self.lineEdit_3.setVisible(True)
        self.lineEdit_4.setVisible(True)
        self.lineEdit_5.setVisible(True)
        self.label_2.setVisible(True)
        self.label_3.setVisible(True)
        self.label_6.setVisible(True)
        self.label_7.setVisible(True)
        self.label_8.setVisible(True)
        self.checkBox_2.setVisible(True)
        
    def _clearDisplayFields(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.textEdit.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.textEdit_3.clear()
        self.checkBox.setChecked(False)
        self.checkBox_2.setChecked(False)