from PySide6.QtWidgets import QWidget
from views.clientView import ClientesEntontradosUI
from PySide6.QtGui import QIcon
from utils.Factory import Factory
from WindowManager.error import errorWindow
from exceptions import exceptions

class findedClientWindow(QWidget, ClientesEntontradosUI.Ui_Form):
    def __init__(self, name):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('./assets/icono-windows.png'))
        self.setWindowTitle("DualD - Clientes Encontrados")
        self.name = name

        self.pushButton.clicked.connect(self._close_window)
        
        self.factory = Factory()
        self.client_controller = self.factory.get_controller('clientController')
        try:
            clients = self.client_controller.find_users(self.name)
            self.lineEdit.setText(clients[0][0])
            self.lineEdit_2.setText(clients[0][1])
        except exceptions.ClientNotExistException as e:
            self.error = errorWindow()
            self.error.ErrorLabel.setText(str(e))
            self.error.show()
            self.close()
        except Exception as e:
            self.error = errorWindow()
            self.error.ErrorLabel.setText(str(e))
            self.error.show()
            self.close()
            
    def _close_window(self):
        self.close()