from PySide6.QtWidgets import QWidget
from views.clientView import newClientUI
from PySide6.QtGui import QIcon
from utils.Factory import Factory
from WindowManager.error import errorWindow
from exceptions import exceptions

class newClientWindow(QWidget, newClientUI.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('./assets/icono-windows.png'))
        self.setWindowTitle("DualD - Nuevo Cliente")

        self.Aceptar_button.clicked.connect(self.pick_date)
        self.Cancelar_button.clicked.connect(self.close_window)
        

    def pick_date(self):
        Nombre = self.Nombre_line_edit.text()
        Apellido = self.Apellido_line_edit.text()
        Telefono = self.Telefonos_line_edit.text()

        if Nombre == "" or Apellido == "" or Telefono == "":
            self.error = errorWindow()
            self.error.ErrorLabel.setText("Por favor, complete todos los campos")
            self.error.show()
            return
        
        if Telefono.isnumeric() == False:
            self.error = errorWindow()
            self.error.ErrorLabel.setText("El teléfono debe ser un número")
            self.error.show()
            return

        Nombre_completo = Nombre + " " + Apellido
        self.factory = Factory()
        self.client_controller = self.factory.get_controller("clientController")
        try:
            self.client_controller.create_user(Nombre_completo, Telefono)
            self.close_window()
        except exceptions.ClientExistException as e:
            self.error = errorWindow()
            self.error.ErrorLabel.setText(str(e))
            self.error.show()
        except Exception as e:
            self.error = errorWindow()
            self.error.ErrorLabel.setText(str(e))
            self.error.show()

    def close_window(self):
        self.close()