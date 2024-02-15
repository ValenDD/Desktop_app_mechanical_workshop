from PySide6.QtWidgets import QWidget
from views.workView import newWorkUI
from PySide6.QtGui import QIcon
from utils.Factory import Factory
from WindowManager.error import errorWindow
from exceptions import exceptions

class newWorkWindow(QWidget, newWorkUI.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('./assets/icono-windows.png'))
        self.setWindowTitle("DualD - Nuevo Trabajo")
        
        self.Aceptar_button.clicked.connect(self._create_work)
        self.Cancelar_button.clicked.connect(self._close_window)
        
    def _create_work(self):
        self.factory = Factory()
        self.client_controller = self.factory.get_controller('clientController')
        
        client_name = self.lineEdit.text().strip()
        vehicle = self.lineEdit_2.text().strip()
        spare_part_cost = self._convert_to_numeric(self.lineEdit_3.text().strip())
        repair_cost = self._convert_to_numeric(self.lineEdit_4.text().strip())
        total_price = self._convert_to_numeric(self.lineEdit_5.text().strip())
        
        date_in = self.dateEdit_2.text()
        date_out = self.dateEdit.text()
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
            self.error = errorWindow()
            self.error.ErrorLabel.setText("El trabajo se ha creado exitosamente")
            self.error.show()
            self.close()
        except exceptions.ClientNotExistException as e:
            self.error = errorWindow()
            self.error.ErrorLabel.setText(str(e))
            self.error.show()
        except Exception as e:
            self.error = errorWindow()
            self.error.ErrorLabel.setText(str(e))
            self.error.show()
            
    def _convert_to_numeric(self, value):
        # Intenta convertir el valor a un número flotante, si falla retorna None
        try:
            return float(value) if value else None
        except ValueError:
            self.error = errorWindow()
            self.error.ErrorLabel.setText("Los campos de costo deben ser números válidos")
            self.error.show()
            return None
            
    def _close_window(self):
        self.close()