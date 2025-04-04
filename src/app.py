import sys
from PySide6.QtWidgets import QApplication

from components.common.main_window import MainWindow
from db.manager import DatabaseManager
from utils.fonts import load_fonts

if __name__ == "__main__":
    app = QApplication(sys.argv)
    load_fonts(app)
    DatabaseManager.initialize()
    
    window = MainWindow()
    window.show()
    
    app.aboutToQuit.connect(DatabaseManager.close_all_connections)
    sys.exit(app.exec())
