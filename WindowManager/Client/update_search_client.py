from PySide6.QtWidgets import QWidget
from views.clientView import updateClientUI
from PySide6.QtGui import QIcon, Qt
from WindowManager.error import errorWindow
from WindowManager.notice import noticeWindow
from exceptions import ClientExceptions
from utils.Factory import Factory

class updateSearchClient(QWidget, updateClientUI.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('./assets/icono-windows.png'))
        self.setWindowTitle("DualD - Actualizar Informacion")
        self.factory = Factory()
        self.client_controller = self.factory.get_controller('clientController')
        self.client = self.client_controller.list_client_only_name()
        self.pushButton.clicked.connect(self._close_window)
        self.label_2.hide()
        self.label_3.hide()
        self.lineEdit.hide()
        self.lineEdit_2.hide()
        self.pushButton_2.hide()
        self.pushButton.hide()
        
        self.comboBox.addItem("")
        for index in range(len(self.client)):
            self.comboBox.addItem(self.client[index][0])
            
        self.comboBox.currentIndexChanged.connect(self._on_comboBox_changed)
        self.lineEdit.textChanged.connect(self._on_lineEdit_changed)
        self.lineEdit_2.textChanged.connect(self._on_lineEdit_changed)
        self._on_comboBox_changed(self.comboBox.currentIndex())
        self.pushButton_2.clicked.connect(self._update_client)
        self.pushButton.clicked.connect(self._close_window)
        
    def _close_window(self):
        self.close()
        
    def _on_comboBox_changed(self, index):
        if index > 0:
            self.client_controller = self.factory.get_controller('clientController')
            client = self.client_controller.find_users(self.comboBox.currentText())
            self.lineEdit.setText(client[0][1])
            self.lineEdit_2.setText(client[0][2])
            self.label_2.show()
            self.label_3.show()
            self.lineEdit.show()
            self.lineEdit_2.show()
            self.pushButton_2.show()
            self.pushButton.show()
        else:
            self.label_2.hide()
            self.label_3.hide()
            self.lineEdit.hide()
            self.lineEdit_2.hide()
            
    def _on_lineEdit_changed(self, ):
        self.client_controller = self.factory.get_controller('clientController')
        client = self.client_controller.find_users(self.comboBox.currentText())
        name_changed = False
        phone_changed = False
        
        if self.lineEdit.text() != client[0][1]:
            name_changed = True
        if self.lineEdit_2.text() != client[0][2]:
            phone_changed = True
        if name_changed or phone_changed:
            self.pushButton_2.setEnabled(True)
        
    def _update_client(self):
        if len(self.lineEdit_2.text().strip()) < 9:
            self.error = errorWindow()
            self.error.ErrorLabel.setText("El teléfono debe ser menor a 8 digitos")
            self.error.show()
            return

        try:
            self.client_controller.update_client_name(self.comboBox.currentText(), self.lineEdit.text().strip(), self.lineEdit_2.text().strip())
            self.notice = noticeWindow()
            self.notice.ErrorLabel.setText("Cliente actualizado correctamente")
            self.notice.show()
            self.close()
        except ClientExceptions.ClientNotExistException as e:
            self.error = errorWindow()
            self.error.ErrorLabel.setText(str(e))
            self.error.show()
        except Exception as e:
            self.error = errorWindow()
            self.error.ErrorLabel.setText(str(e))
            self.error.show()

    def keyPressEvent(self, event):
        if event.key() in (Qt.Key_Return, Qt.Key_Enter):
            self._update_client()
        
        if event.key() == Qt.Key_Escape:
            self._close_window()
        super().keyPressEvent(event)