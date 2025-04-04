from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtGui import Qt

from .views.folders import FoldersSection
from .views.program import ProgramSection


class SettingsScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 48, 0, 0)
        container = self.draw_container()
        layout.addWidget(container, alignment=Qt.AlignHCenter)

    def draw_container(self):
        container = QWidget()
        container.setFixedWidth(800)
        c_layout = QVBoxLayout()
        c_layout.setAlignment(Qt.AlignTop)
        c_layout.setContentsMargins(48, 96, 48, 96)
        c_layout.setSpacing(0)

        c_layout.addWidget(FoldersSection())
        c_layout.addSpacing(48)
        c_layout.addWidget(ProgramSection())
        c_layout.addStretch(1)

        container.setLayout(c_layout)
        return container
