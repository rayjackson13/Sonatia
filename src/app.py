import sys
from PySide6.QtWidgets import QApplication, QLabel
from qframelesswindow import FramelessWindow

from constants.colors import Colors
from components.common.header import CustomTitleBar

from utils.window import center_window

class CustomWindow(FramelessWindow):
    def __init__(self):
        super().__init__()
        self.resize(1200, 900)  # Set window dimensions

        # Remove the titlebar
        self.setWindowTitle("Sonatia")  # Optional for internal title usage
        self.setResizeEnabled(True)  # Enable resizing if needed
        self.setTitleBar(CustomTitleBar(self))

        # Paint the entire window black
        self.setStyleSheet(f"background-color: {Colors.BG_PRIMARY};")
        self.setContentsMargins(0, 0, 0, 0)

        # Add a label for demonstration (optional)
        label = QLabel("The window is fully black with no titlebar.", self)
        label.setStyleSheet(f"color: {Colors.WHITE}; font-size: 14px;")
        
        center_window(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CustomWindow()
    window.show()
    sys.exit(app.exec())
