import sys
from PySide6.QtWidgets import QApplication

from db.manager import DatabaseManager
from components.common.main_window import MainWindow
from utils.db import load_db
from utils.fonts import load_fonts

if __name__ == "__main__":
    app = QApplication(sys.argv)
    load_fonts(app)
    load_db()
    
    window = MainWindow()
    window.show()
    
    app.aboutToQuit.connect(DatabaseManager.close_all_connections)
    sys.exit(app.exec())
