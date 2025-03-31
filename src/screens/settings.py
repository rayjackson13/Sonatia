from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton

class SettingsScreen(QWidget):
    def __init__(self, navigation):
        super().__init__()
        self.navigation = navigation
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        button = QPushButton("Go Back")
        button.setStyleSheet("color: white;")
        button.clicked.connect(self.navigation.go_back)
        layout.addWidget(button)