from os import path

from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtCore import Qt

from components.common.svg_icon import SvgIcon


class Footer(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout()
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(0)
        layout.addWidget(SvgIcon("assets/svg/footer.svg", 181, 16))
        layout.setAlignment(Qt.AlignCenter)
        self.setLayout(layout)
