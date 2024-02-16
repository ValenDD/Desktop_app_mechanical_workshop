from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QIcon
from utils.Factory import Factory
from views.clientView import findDeleteClientWindowUI
from utils.Factory import Factory
from WindowManager.error import errorWindow
from WindowManager.notice import noticeWindow
from exceptions import ClientExceptions


class findDeleteClientWindow(QWidget, findDeleteClientWindowUI.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('./assets/icono-windows.png'))
        self.setWindowTitle("DualD - Buscar Cliente")
        
        self.factory = Factory()
        self.client_controller = self.factory.get_controller("clientController")
        clients = self.client_controller.list_client_only_name()
        for index in range(len(clients)):
            self.lista_clientes.addItem(clients[index][0])
        
        self.Eliminar_button.clicked.connect(self._delete_client)
        self.Cancelar_button.clicked.connect(self.close)
        
    def _delete_client(self):
        client_name = self.lista_clientes.currentText()
        try:
            self.work_controller = self.factory.get_controller('workController')
            self.work_controller.delete_all_works(self.client_controller.client_id(client_name))
            self.client_controller.delete_client(client_name)
            self.error = noticeWindow()
            self.error.ErrorLabel.setText("Cliente eliminado con éxito")
            self.error.show()
            self._close_window()
        except ClientExceptions.ClientNotExistException as e:
            self.error = errorWindow()
            self.error.ErrorLabel.setText(str(e))
            self.error.show()
        except Exception as e:
            self.error = errorWindow()
            self.error.ErrorLabel.setText(str(e))
            self.error.show()
        
    def _close_window(self):
        self.close()