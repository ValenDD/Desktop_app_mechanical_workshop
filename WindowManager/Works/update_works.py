from PySide6.QtWidgets import QWidget, QHeaderView, QCheckBox, QHBoxLayout, QTableWidgetItem, QWidget
from views.workView import updateWorkUI
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

class updateWorkWindow(QWidget, updateWorkUI.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon(resource_path(os.path.join('assets', 'icono-windows.ico'))))
        self.setWindowTitle("DualD - Actualizar Trabajo")
        self.factory = Factory()
        self.currentCheckBox = None
        self.work_id = None
        self.originalTexts = {}
        self.state = 'initial'
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
        self.dateEdit.hide()
        self.tableWidget.hide()
        self.Aceptar_button.hide()
        self.Cancelar_button.hide()
        self.checkBox.hide()
        self.dateEdit.hide()
        self.dateEdit_2.hide()
        self.label.hide()
        self.label_10.hide()
        self.label_5.hide()
        self.label_9.hide()
        self.label_4.hide()
        self.textEdit.hide()
        self.textEdit_2.hide()
        self.textEdit_3.hide()
        self.lineEdit.hide()
        self.lineEdit_2.hide()
        self.lineEdit_3.hide()
        self.lineEdit_4.hide()
        self.lineEdit_5.hide()
        self.label_2.hide()
        self.label_3.hide()
        self.label_6.hide()
        self.label_7.hide()
        self.label_8.hide()
        self.checkBox_2.hide()
        self.checkBox_2.setChecked(False)
        self.dateEdit.setEnabled(False)
        
        self.checkBox_2.stateChanged.connect(self._show_date_out)
        self.pushButton.clicked.connect(self._search_client_works)
        self.Aceptar_button.clicked.connect(lambda: self._update_work())
        self.Cancelar_button.clicked.connect(self._close_window)

    def _search_client_works(self):
        self.state = 'searched'
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
            
        header = self.tableWidget.horizontalHeader() 
        header.setMinimumSectionSize(117)
        header.setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.show()
        
        self.lineEdit_6.textChanged.connect(self.resetUI)
 
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
        self.state = 'displayed'
        values = []
            
        for column in range(1, self.tableWidget.columnCount()):
            item = self.tableWidget.item(row, column)
            if item is not None:
                values.append(item.text())
            else:
                values.append("")
                
        dateFormat = "yyyy-MM-dd"

        fechaIngreso = QDate.fromString(values[1], dateFormat)
        fechaEgreso = QDate.fromString(values[2], dateFormat)

        if fechaIngreso.isValid():
            self.dateEdit_2.setDate(fechaIngreso)
        if fechaEgreso.isValid():
            self.dateEdit.setDate(fechaEgreso)
        
        self.client_name = self.lineEdit_6.text().strip()
        self.lineEdit.setText(self.client_name)
        
        if self.lineEdit_2.setText(values[0]):
            self.checkBox_2.setChecked(True)
            self.lineEdit_2.setText(values[0])
        
        self.lineEdit_3.setText(values[5])
        self.lineEdit_4.setText(values[6])
        self.lineEdit_5.setText(values[7])
        
        self.textEdit.setText(values[3])
        self.textEdit_2.setText(values[4])
        self.textEdit_3.setText(values[8])
        
        self.checkBox.setChecked(values[9] == 'True')
        
        self.originalTexts = {
            'lineEdit_3': self.lineEdit_3.text(),
            'lineEdit_4': self.lineEdit_4.text(),
            'lineEdit_5': self.lineEdit_5.text(),
            'textEdit': self.textEdit.toPlainText(),
            'textEdit_2': self.textEdit_2.toPlainText(),
            'textEdit_3': self.textEdit_3.toPlainText(),
            'checkBox': self.checkBox.isChecked(),
            'checkBox_2': self.checkBox_2.isChecked(),
        }
        
        self._see_windows()
        
        
    def _see_windows(self):
        self.Aceptar_button.show()
        self.Cancelar_button.show()
        self.checkBox.show()
        self.dateEdit.show()
        self.dateEdit_2.show()
        self.label.show()
        self.label_10.show()
        self.label_5.show()
        self.label_9.show()
        self.label_4.show()
        self.textEdit.show()
        self.textEdit_2.show()
        self.textEdit_3.show()
        self.lineEdit.show()
        self.lineEdit_2.show()
        self.lineEdit_3.show()
        self.lineEdit_4.show()
        self.lineEdit_5.show()
        self.label_2.show()
        self.label_3.show()
        self.label_6.show()
        self.label_7.show()
        self.label_8.show()
        self.checkBox_2.show()
        
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
        
    def resetUI(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.textEdit.clear()
        self.textEdit_2.clear()
        self.textEdit_3.clear()
        self.checkBox.setChecked(False)
        self.checkBox_2.setChecked(False)
        
        if self.currentCheckBox:
            self.currentCheckBox.setChecked(False)
            self.currentCheckBox = None

        self.tableWidget.setRowCount(0)

        self.hideElements()
        
    def hideElements(self):
        elements = [self.Aceptar_button, self.Cancelar_button, self.checkBox, 
                    self.dateEdit, self.dateEdit_2, self.label, self.label_10, 
                    self.label_5, self.label_9, self.label_4, self.textEdit, 
                    self.textEdit_2, self.textEdit_3, self.lineEdit, self.lineEdit_2,
                    self.lineEdit_3, self.lineEdit_4, self.lineEdit_5, self.label_2, 
                    self.label_3, self.label_6, self.label_7, self.label_8, self.checkBox_2]
        
        for element in elements:
            element.hide()

        self.tableWidget.hide()
        
    def _update_work(self):
        self.work_controller = self.factory.get_controller('workController')
        self.work_id = self.work_controller.work_id(self.client_name)
        
        hasChanged = (
            self.lineEdit_3.text() != self.originalTexts['lineEdit_3'] or
            self.lineEdit_4.text() != self.originalTexts['lineEdit_4'] or
            self.lineEdit_5.text() != self.originalTexts['lineEdit_5'] or
            self.textEdit.toPlainText() != self.originalTexts['textEdit'] or
            self.textEdit_2.toPlainText() != self.originalTexts['textEdit_2'] or
            self.textEdit_3.toPlainText() != self.originalTexts['textEdit_3'] or
            self.checkBox.isChecked() != self.originalTexts['checkBox'] or
            self.checkBox_2.isChecked() != self.originalTexts['checkBox_2']
        )
        if hasChanged:
            self.client_name = self.lineEdit.text().strip()
            vehicle = self.lineEdit_2.text().strip()
            diagnosis = self.textEdit.toPlainText().strip()
            repair = self.textEdit_2.toPlainText().strip()
            spare_part_cost = self._convert_to_numeric(self.lineEdit_3.text().strip())
            repair_cost = self._convert_to_numeric(self.lineEdit_4.text().strip())
            total_price = self._convert_to_numeric(self.lineEdit_5.text().strip())
            payment_method = self.textEdit_3.toPlainText().strip()
            done = self.checkBox.isChecked()
            
            if self.checkBox_2.isChecked():
                date_out = self.dateEdit.date().toString("dd-MM-yyyy")
            else:
                date_out = None
            date_in = self.dateEdit_2.date().toString("dd-MM-yyyy")
            
            try:
                self.factory.get_controller('workController').update_work(self.work_id , date_in, date_out, self.client_name, vehicle, diagnosis, repair, spare_part_cost, repair_cost, total_price, payment_method, done)
                self.hideElements()
                self.resetUI()
                self.lineEdit_6.clear()
                self.lineEdit_6.setFocus()
                self.error = noticeWindow()
                self.error.ErrorLabel.setText("Trabajo actualizado con éxito")
                self.error.show()
                self._close_window()
            except WorksExceptions.WorkNotExistException as e:
                self.error = errorWindow()
                self.error.ErrorLabel.setText(str(e))
                self.error.show()
            except Exception as e:
                self.error = errorWindow()
                self.error.ErrorLabel.setText(str(e))
                self.error.show()
        
    def _convert_to_numeric(self, value):
        try:
            return float(value) if value else None
        except ValueError:
            self.error = errorWindow()
            self.error.ErrorLabel.setText("Los campos de costo deben ser números válidos")
            self.error.show()
            return None
    
    def _show_date_out(self, state):
        if state == 2:
            self.dateEdit.setEnabled(True)
        else:
            self.dateEdit.setEnabled(False) 
    
    def _close_window(self):
        self.hideElements()
        self.resetUI()
        self.lineEdit_6.clear()
        self.lineEdit_6.setFocus()
        self.close()

    def keyPressEvent(self, event):
        if event.key() in (Qt.Key_Return, Qt.Key_Enter):
            if self.state == "initial":
                self._search_client_works()
            elif self.state == "searched":
                self._displayRowData(self.tableWidget.currentRow())
            elif self.state == "displayed":
                self._update_work()
        
        if event.key() == Qt.Key_Escape:
            self._close_window()
        super().keyPressEvent(event)