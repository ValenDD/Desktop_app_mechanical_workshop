from PySide6.QtWidgets import QWidget
from views.clientView import newClientUI
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt
from utils.Factory import Factory
from WindowManager.error import errorWindow
from WindowManager.notice import noticeWindow
from exceptions import ClientExceptions

class newClientWindow(QWidget, newClientUI.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('./assets/icono-windows.png'))
        self.setWindowTitle("DualD - Nuevo Cliente")

        self.Aceptar_button.clicked.connect(self._pick_date)
        self.Cancelar_button.clicked.connect(self._close_window)
        
    def _pick_date(self):
        Nombre = self.Nombre_line_edit.text().strip()
        Apellido = self.Apellido_line_edit.text().strip()
        Telefono = self.Telefonos_line_edit.text().strip()

        if Nombre == "" or Apellido == "" or Telefono == "":
            self.error = errorWindow()
            self.error.ErrorLabel.setText("Por favor, complete todos los campos")
            self.error.show()
            return
        
        if Nombre.isnumeric() == True or Apellido.isnumeric() == True:
            self.error = errorWindow()
            self.error.ErrorLabel.setText("El nombre y apellido no pueden ser números")
            self.error.show()
            return
        
        if Telefono.isnumeric() == False:
            self.error = errorWindow()
            self.error.ErrorLabel.setText("El teléfono debe ser un número")
            self.error.show()
            return

        if len(Telefono) < 9:
            self.error = errorWindow()
            self.error.ErrorLabel.setText("El teléfono debe ser mayor a 8 digitos")
            self.error.show()
            return
        
        Nombre_completo = Nombre + " " + Apellido
        self.factory = Factory()
        self.client_controller = self.factory.get_controller("clientController")

        try:
            self.client_controller.create_user(Nombre_completo, Telefono)
            self.error = noticeWindow()
            self.error.ErrorLabel.setText("Cliente creado con éxito")
            self.error.show()
            self.close_window()
        except ClientExceptions.ClientExistException as e:
            self.error = errorWindow()
            self.error.ErrorLabel.setText(str(e))
            self.error.show()
        except Exception as e:
            self.error = errorWindow()
            self.error.ErrorLabel.setText(str(e))
            self.error.show()

    def _close_window(self):
        self.close()

    def keyPressEvent(self, event):
        if event.key() in (Qt.Key_Return, Qt.Key_Enter):
            self._pick_date()
        
        if event.key() == Qt.Key_Escape:
            self._close_window()
        super().keyPressEvent(event)