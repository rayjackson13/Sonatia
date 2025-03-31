from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton


class HomeScreen(QWidget):
    def __init__(self, navigation):
        super().__init__()
        self.navigation = navigation
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        button = QPushButton("Go to Settings")
        button.setStyleSheet("color: white;")
        button.clicked.connect(self.open_settings)
        layout.addWidget(button)

    def open_settings(self):
        self.navigation.navigate("settings")
