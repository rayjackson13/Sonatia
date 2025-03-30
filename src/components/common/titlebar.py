from PySide6.QtWidgets import QWidget, QLayout, QHBoxLayout, QLabel
from PySide6.QtGui import QColor, QFont
from PySide6.QtCore import Qt
from qframelesswindow import TitleBar

from constants.colors import Colors
from .logo import Logo
from .back_button import BackButton

BACK_BTN_WIDTH = 80

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

        self.title = "App Settings"
        self.back_button = BackButton()
        self.handle_system_buttons()
        layout = self.layout()
        
        if not layout:
            return
        
        self.remove_extra_spacers(layout)
        
        logo = Logo()
        cc = self.get_center_container()
        layout.insertWidget(0, cc, 1)
        layout.insertWidget(0, logo)
        
    def get_center_container(self):        
        center_container = QWidget()
        center_container.setFixedHeight(48)

        self.c_layout = QHBoxLayout()
        self.c_layout.setContentsMargins(*self.get_container_margins())
        self.c_layout.setSpacing(0)
        
        title = QLabel(self.title)
        title_font = QFont('Inter')
        title_font.setPixelSize(20)
        title_font.setWeight(QFont.Medium)
        title.setFont(title_font)
        title.setStyleSheet(f"color: {Colors.WHITE}")
        title.setAlignment(Qt.AlignCenter)
        self.c_layout.addWidget(self.back_button)
        self.c_layout.addStretch(1)
        self.c_layout.addWidget(title)
        self.c_layout.addStretch(1)
        center_container.setLayout(self.c_layout)
        return center_container
    
    def get_container_margins(self, is_back_btn_visible = True):
        left_margin = 48 + BACK_BTN_WIDTH if not is_back_btn_visible else 48
        right_margin = (200 - 48*3) + BACK_BTN_WIDTH + 48 + 8
        return (left_margin, 8, right_margin, 8)
    
    def toggle_back_button(self):
        is_visible = not self.back_button.isVisible()
        self.back_button.setVisible(is_visible)
        margins = self.get_container_margins(is_visible)
        self.c_layout.setContentsMargins(*margins)
        
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
            
    def remove_extra_spacers(self, layout: QLayout):
        """Remove extra spacer added by qframelesswindow library"""
        
        item = layout.itemAt(0)
        if item and item.spacerItem():
            item.spacerItem().invalidate()
            layout.removeItem(item)
            del item
    