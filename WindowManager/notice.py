from PySide6.QtWidgets import QWidget
from views.NoticeView import avisoUI
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt
import sys
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class noticeWindow(QWidget, avisoUI.Ui_Frame):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon(resource_path(os.path.join('assets', 'icono-windows.ico'))))
        self.setWindowTitle("Aviso")
        
    def _close_window(self):
        self.close()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self._close_window()