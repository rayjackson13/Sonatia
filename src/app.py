import sys
from PySide6.QtWidgets import QApplication

from components.common.main_window import MainWindow
from utils.fonts import load_fonts

if __name__ == "__main__":
    app = QApplication(sys.argv)
    load_fonts(app)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
