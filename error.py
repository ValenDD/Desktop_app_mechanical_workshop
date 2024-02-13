from PySide6.QtWidgets import QWidget
from views.ErrorView import error
from PySide6.QtGui import QIcon


class errorWindow(QWidget, error.Ui_Frame):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('./assets/icono-windows.png'))
        self.setWindowTitle("Error")
        
    