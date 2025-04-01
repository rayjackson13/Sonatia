from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QSizePolicy
from PySide6.QtGui import Qt

from components.common.button_with_icon import ButtonWithIcon

from .views.recents import RecentsSection


class HomeScreen(QWidget):
    def __init__(self, navigation):
        super().__init__()
        self.navigation = navigation
        self.draw_ui()

    def draw_ui(self):
        layout = QVBoxLayout(self)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
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

        add_button = ButtonWithIcon("New session", "add")
        add_button.clicked.connect(self.open_settings)
        
        open_button = ButtonWithIcon("Open project", "folder-open")
        open_button.clicked.connect(self.open_settings)
        
        settings_button = ButtonWithIcon("Settings", "gear")
        settings_button.clicked.connect(self.open_settings)
        
        c_layout.addWidget(RecentsSection())
        c_layout.addSpacing(48)
        c_layout.addWidget(add_button)
        c_layout.addSpacing(16)
        c_layout.addWidget(open_button)
        c_layout.addSpacing(16)
        c_layout.addWidget(settings_button)

        container.setLayout(c_layout)
        return container

    def open_settings(self):
        self.navigation.navigate("settings")
