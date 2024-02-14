from PySide6.QtWidgets import QWidget
from views.clientView import ClientesEntontradosUI
from PySide6.QtGui import QIcon
from WindowManager.error import errorWindow
from exceptions import exceptions

class findedClientWindow(QWidget, ClientesEntontradosUI.Ui_Form):
    def __init__(self, clients):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('./assets/icono-windows.png'))
        self.setWindowTitle("DualD - Clientes Encontrados")
        self.clients = clients

        self.pushButton.clicked.connect(self._close_window)
        
        try:
            self.lineEdit.setText(self.clients[0][1])
            self.lineEdit_2.setText(self.clients[0][2])
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