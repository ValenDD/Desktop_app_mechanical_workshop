from PySide6.QtWidgets import QWidget
from views.workView import newWorkUI
from PySide6.QtGui import QIcon, Qt
from utils.Factory import Factory
from WindowManager.error import errorWindow
from WindowManager.notice import noticeWindow
from exceptions import ClientExceptions
import sys
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class newWorkWindow(QWidget, newWorkUI.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon(resource_path(os.path.join('assets', 'icono-windows.ico'))))
        self.setWindowTitle("DualD - Nuevo Trabajo")
        self.dateEdit.setEnabled(False) 
        self.Aceptar_button.clicked.connect(self._create_work)
        self.Cancelar_button.clicked.connect(self._close_window)
        self.checkBox_2.stateChanged.connect(self._show_date_out)
        
    def _create_work(self):
        self.factory = Factory()
        self.client_controller = self.factory.get_controller('clientController')
        date_out = None
        if self.checkBox_2.isChecked():
            date_out = self.dateEdit.text()
        client_name = self.lineEdit.text().strip()
        vehicle = self.lineEdit_2.text().strip()
        spare_part_cost = self._convert_to_numeric(self.lineEdit_3.text().strip())
        repair_cost = self._convert_to_numeric(self.lineEdit_4.text().strip())
        total_price = self._convert_to_numeric(self.lineEdit_5.text().strip())
        date_in = self.dateEdit_2.text()
        
        diagnosis = self.textEdit.toPlainText().strip()
        repair = self.textEdit_2.toPlainText().strip()
        payment_method = self.textEdit_3.toPlainText().strip()
        done = self.checkBox.isChecked()
        
        if vehicle == "" or date_in == "1/1/2000":
            self.error = errorWindow()
            self.error.ErrorLabel.setText("Los campos de vehículo y fecha de ingreso son obligatorios")
            self.error.show()
            return
        
        try:
            self.work_controller = self.factory.get_controller('workController')
            self.work_controller.create_work(date_in, date_out, client_name, vehicle, diagnosis, repair, spare_part_cost, repair_cost, total_price, payment_method, done)
            self.error = noticeWindow()
            self.error.ErrorLabel.setText("El trabajo se ha creado exitosamente")
            self.error.show()
            self.close()
        except ClientExceptions.ClientNotExistException as e:
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
        self.close()
    
    def keyPressEvent(self, event):
        if event.key() in (Qt.Key_Return, Qt.Key_Enter):
            self._create_work()
        
        if event.key() == Qt.Key_Escape:
            self._close_window()
        super().keyPressEvent(event)