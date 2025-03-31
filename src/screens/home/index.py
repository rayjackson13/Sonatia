from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QSizePolicy
from PySide6.QtGui import Qt

from .views.recents import RecentsSection


class HomeScreen(QWidget):
    def __init__(self, navigation):
        super().__init__()
        self.navigation = navigation
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        layout.setContentsMargins(0,48,0,0)
        
        
        container = QWidget()
        container.setFixedWidth(800)
        c_layout = QVBoxLayout()
        c_layout.setAlignment(Qt.AlignTop)
        c_layout.setContentsMargins(48, 96, 48, 96)
        c_layout.setSpacing(0)
        
        button = QPushButton("Go to Settings")
        button.setStyleSheet("color: white;")
        button.clicked.connect(self.open_settings)
        c_layout.addWidget(RecentsSection())
        c_layout.addSpacing(48)
        
        container.setLayout(c_layout)
        layout.addWidget(container, alignment=Qt.AlignHCenter)

    def open_settings(self):
        self.navigation.navigate("settings")
