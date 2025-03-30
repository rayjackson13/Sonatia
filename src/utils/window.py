from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QCursor

def center_window(window):
    # Get the screen geometry
    screen = QApplication.screenAt(QCursor.pos())

    if (screen):
        screen_geometry = screen.geometry()

        # Calculate center position
        x = screen_geometry.x() + (screen_geometry.width() - window.width()) // 2
        y = screen_geometry.y() + (screen_geometry.height() - window.height()) // 2

        # Move the window to the calculated position
        window.move(x, y)
    else:
        # Fallback: center on primary screen if screen detection fails
        primary_screen = QApplication.primaryScreen().geometry()
        x = primary_screen.x() + (primary_screen.width() - window.width()) // 2
        y = primary_screen.y() + (primary_screen.height() - window.height()) // 2
        window.move(x, y)
