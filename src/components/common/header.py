from PySide6.QtGui import QColor
from qframelesswindow import StandardTitleBar

from constants.colors import Colors

titleBarButtonStyles = f"""
    qproperty-normalColor: white;
    qproperty-normalBackgroundColor: transparent;
    qproperty-hoverColor: white;
    qproperty-pressedColor: white;
"""

class CustomTitleBar(StandardTitleBar):
    """ Custom title bar """

    def __init__(self, parent):
        super().__init__(parent)

        # customize the style of title bar buttons
        self.minBtn.setStyleSheet(titleBarButtonStyles)
        self.maxBtn.setStyleSheet(titleBarButtonStyles)
        self.closeBtn.setStyleSheet(titleBarButtonStyles)
        self.closeBtn.setPressedBackgroundColor(QColor('#92202a'))