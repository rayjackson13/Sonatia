from PySide6.QtWidgets import QPushButton
from PySide6.QtGui import QColor
from PySide6.QtCore import Qt
from qframelesswindow import TitleBar

from .logo import Logo

titleBarButtonStyles = f"""
    qproperty-normalColor: white;
    qproperty-normalBackgroundColor: transparent;
    qproperty-hoverColor: white;
    qproperty-pressedColor: white;
"""

class CustomTitleBar(TitleBar):
    """ Custom title bar """

    def __init__(self, parent):
        super().__init__(parent)

        self.handle_system_buttons()
        
        layout = self.layout()
        
        if (layout):
            logo = Logo()
            layout.insertWidget(0, logo)
        
    def handle_system_buttons(self):
        """Customizes the style of title bar buttons"""
        
        self.minBtn.setStyleSheet(titleBarButtonStyles)
        self.maxBtn.setStyleSheet(titleBarButtonStyles)
        self.closeBtn.setStyleSheet(titleBarButtonStyles)
        self.closeBtn.setPressedBackgroundColor(QColor('#92202a'))
        
        self.setFixedHeight(48)
        btnGroupLayout = self.minBtn.parentWidget().layout()
        if btnGroupLayout:
            btnGroupLayout.setAlignment(self.minBtn, Qt.AlignTop)
            btnGroupLayout.setAlignment(self.maxBtn, Qt.AlignTop)
            btnGroupLayout.setAlignment(self.closeBtn, Qt.AlignTop)
    
    
    