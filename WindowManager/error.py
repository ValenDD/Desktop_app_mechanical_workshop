from PySide6.QtWidgets import QWidget
from views.ErrorView import errorUI
from PySide6.QtGui import QIcon, Qt


class errorWindow(QWidget, errorUI.Ui_Frame):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('./assets/icono-windows.png'))
        self.setWindowTitle("Error")
        
    def _close_window(self):
        self.close()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self._close_window()