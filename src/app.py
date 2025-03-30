import sys
from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget, QPushButton
from PySide6.QtCore import Qt
from qframelesswindow import FramelessWindow

from constants.colors import Colors
from components.common.titlebar import CustomTitleBar
from components.common.footer import Footer

from utils.window import center_window
from utils.fonts import load_fonts

class CustomWindow(FramelessWindow):
    def __init__(self):
        super().__init__()
        self.resize(1200, 900)  # Set window dimensions
        self.setMinimumWidth(1200)
        
        center_window(self)

        # Remove the titlebar
        self.setWindowTitle("Sonatia")  # Optional for internal title usage
        self.setResizeEnabled(True)  # Enable resizing if needed
        self.setTitleBar(CustomTitleBar(self))

        # Paint the entire window black
        self.setStyleSheet(f"background-color: {Colors.BG_PRIMARY};")
        self.setContentsMargins(0, 0, 0, 0)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 48, 0, 0)  # Add margins for titlebar
        layout.setSpacing(0)
        layout.addStretch(1)
        layout.addWidget(Footer())
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    load_fonts(app)
    window = CustomWindow()
    window.show()
    sys.exit(app.exec())
