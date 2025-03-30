from os import path

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel

from constants.common import PROJECT_ROOT

class Logo(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        icon_uri = path.join(PROJECT_ROOT, 'assets', 'images', 'logo.png')
        self.setPixmap(QPixmap(icon_uri).scaled(200, 48))
        