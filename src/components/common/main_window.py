from PySide6.QtWidgets import QVBoxLayout
from qframelesswindow import FramelessWindow

from constants.colors import Colors
from components.common.titlebar import CustomTitleBar
from components.common.footer import Footer
from navigation.index import Navigation

from utils.window import center_window


class MainWindow(FramelessWindow):
    def __init__(self):
        super().__init__()
        self.resize(1200, 900)  # Set window dimensions
        self.setMinimumWidth(1200)

        center_window(self)

        # Remove the titlebar
        self.setWindowTitle("Sonatia")  # Optional for internal title usage
        self.setResizeEnabled(True)  # Enable resizing if needed

        self.navigation = Navigation(self)
        self.setTitleBar(CustomTitleBar(self, self.navigation))
        self.setObjectName('MainWindow')

        # Paint the entire window black
        self.setStyleSheet(f"QWidget#MainWindow {{ background-color: {Colors.BG_PRIMARY}; }}")
        self.setContentsMargins(0, 0, 0, 0)

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)  # Add margins for titlebar
        layout.setSpacing(0)
        layout.addWidget(self.navigation, stretch=1)
        layout.addWidget(Footer())
        self.setLayout(layout)
