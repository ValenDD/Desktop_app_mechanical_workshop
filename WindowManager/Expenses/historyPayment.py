from views.expensesView import paymentHistoryUI
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget, QHeaderView, QCheckBox, QHBoxLayout, QWidget
from utils.Factory import Factory
from PySide6.QtCore import Qt, QDate
from WindowManager.notice import noticeWindow
from WindowManager.error import errorWindow
import sys
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class historyPaymentWindow(QWidget, paymentHistoryUI.Ui_Form):
    def __init__(self):
            super().__init__()
            self.setupUi(self)
            self.setWindowIcon(QIcon(resource_path(os.path.join('assets', 'icono-windows.ico'))))
            self.setWindowTitle("DualD - Actualizar pagos / Historial de Pagos")
            self.factory = Factory()
            self.month = None
            self.year = None
            self.currentCheckBox = None
            self.work_name = None
            self.amount = None
            self.reciver_name = None
            self.id_expense = None
            self.tableWidget.hide()
            self.pushButton_2.hide()
            self.pushButton_3.hide()
            self.lineEdit.hide()
            self.lineEdit_2.hide()
            self.lineEdit_3.hide()
            self.label_2.hide()
            self.label_3.hide()
            self.label_4.hide()
            
            self.tableWidget.horizontalHeader().setStyleSheet("""
            QHeaderView::section {
                background-color: lightgray;
                padding: 4px;
                border: none;
                border-bottom: 2px solid black;
                font-weight: bold;
            }
            """)
            self.pushButton.clicked.connect(self._show_expenses)
            self.dateEdit.dateChanged.connect(self._clear_fields)
            self.pushButton_2.clicked.connect(self._close_window)
            self.pushButton_3.clicked.connect(self._update_expense)
            
    def _show_expenses(self):
        self.fecha_ingreso = self.dateEdit.date()
        self.month = self.fecha_ingreso.month()
        self.year = self.fecha_ingreso.year()
        expenses = self.factory.get_controller('expensesController').list_expenes(self.month, self.year)
        
        self.tableWidget.setRowCount(len(expenses))
        for index in range(len(expenses)):
            checkBox = QCheckBox()
            widget = QWidget()
            layout = QHBoxLayout(widget)
            layout.addWidget(checkBox)
            layout.setAlignment(Qt.AlignCenter)
            layout.setContentsMargins(0, 0, 0, 0)
            widget.setLayout(layout)
            
            checkBox.stateChanged.connect(lambda checked, checkBox=checkBox, row=index: self._onCheckBoxChanged(checkBox, row))
        
            self.tableWidget.setCellWidget(index, 0, widget)
            self.tableWidget.setItem(index, 1, paymentHistoryUI.QTableWidgetItem(expenses[index][0]))
            self.tableWidget.setItem(index, 2, paymentHistoryUI.QTableWidgetItem(expenses[index][1]))
            self.tableWidget.setItem(index, 3, paymentHistoryUI.QTableWidgetItem(str(expenses[index][2])))
            self.tableWidget.setItem(index, 4, paymentHistoryUI.QTableWidgetItem(str(expenses[index][3])))
        
        header = self.tableWidget.horizontalHeader() 
        header.setMinimumSectionSize(117)
        header.setSectionResizeMode(QHeaderView.Stretch)
        
        self.tableWidget.show()
        
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
        
        self.lineEdit.setText(values[0])
        self.lineEdit_2.setText(values[1])
        self.lineEdit_3.setText(str(int(float(values[3]))))       
        
        self.work_name = values[0]
        self.reciver_name = values[1]
        self.amount = values[3]
        
        self.label_2.show()
        self.label_3.show()
        self.label_4.show()
        self.lineEdit.show()
        self.lineEdit_2.show()
        self.lineEdit_3.show()
        self.pushButton_2.show()
        self.pushButton_3.show()
         
    def _update_expense(self):
         if self.work_name != self.lineEdit.text() or self.reciver_name != self.lineEdit_2.text() or self.amount != self.lineEdit_3.text():
            if self.lineEdit.text() == "" or self.lineEdit_2.text() == "" or self.lineEdit_3.text() == "":
                self.notice = errorWindow()
                self.notice.ErrorLabel.setText("Por favor, rellene todos los campos")
                self.notice.show()
                return
            
            if not (self.lineEdit_3.text().isnumeric()):
                self.notice = errorWindow()
                self.notice.ErrorLabel.setText("El monto debe ser un número entero")
                self.notice.show()
                return
                
            self.id_expense = self.factory.get_controller('expensesController').expense_id(self.work_name, self.reciver_name, self.amount)
            self.factory.get_controller('expensesController').update_expense(self.id_expense, self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text())
            self.notice = noticeWindow()
            self.notice.ErrorLabel.setText("El pago ha sido actualizado correctamente")
            self.notice.show()
            self.close()
            self._close_window()
                
    def _clear_fields(self):
        self.tableWidget.hide()
        self.pushButton_2.hide()
        self.pushButton_3.hide()
        self.lineEdit.hide()
        self.lineEdit_2.hide()
        self.lineEdit_3.hide()
        self.label_2.hide()
        self.label_3.hide()
        self.label_4.hide()
        
    def _clearDisplayFields(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()

    def _close_window(self):
        self.close()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self._show_expenses()
        elif event.key() == Qt.Key_Escape:
            self._close_window()
        super().keyPressEvent(event)