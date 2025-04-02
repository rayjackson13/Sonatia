from PySide6.QtWidgets import QWidget, QLayout, QHBoxLayout, QLabel
from PySide6.QtGui import QColor, QFont
from PySide6.QtCore import Qt
from qframelesswindow import TitleBar

from constants.colors import Colors
from store.navigation import NavigationStore

from .logo import Logo
from .back_button import BackButton

BACK_BTN_WIDTH = 80

titleBarButtonStyles = f"""
    TitleBarButton#CustomTitleBarBtn {{
        qproperty-normalColor: white;
        qproperty-normalBackgroundColor: transparent;
        qproperty-hoverColor: white;
        qproperty-pressedColor: white;
    }}
"""


class CustomTitleBar(TitleBar):
    """Custom title bar"""

    def __init__(self, parent, navigation):
        super().__init__(parent)

        self.navigation = navigation
        self.store = NavigationStore.get_instance()
        self.store.data_updated.connect(self.on_data_updated)
        self.title = self.store.get_title()
        self.back_button = BackButton()
        self.handle_system_buttons()

        self.init_ui()
        self.setObjectName('CustomTitleBar')
        self.setStyleSheet("TitleBar#CustomTitleBar { background-color: transparent; }")
        self.toggle_back_button(False)

    def init_ui(self):
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

        self.title_label = QLabel(self.title)
        title_font = QFont("Inter")
        title_font.setPixelSize(20)
        title_font.setWeight(QFont.Medium)
        self.title_label.setFont(title_font)
        self.title_label.setObjectName('CustomTitleBarLabel')
        self.title_label.setStyleSheet(f"QLabel#CustomTitleBarLabel {{ color: {Colors.WHITE}; }}")
        self.title_label.setAlignment(Qt.AlignCenter)

        self.back_button.clicked.connect(self.navigation.go_back)

        self.c_layout.addWidget(self.back_button)
        self.c_layout.addStretch(1)
        self.c_layout.addWidget(self.title_label)
        self.c_layout.addStretch(1)

        center_container.setLayout(self.c_layout)
        return center_container

    def get_container_margins(self, is_back_btn_visible=True):
        left_margin = 48 + BACK_BTN_WIDTH if not is_back_btn_visible else 48
        right_margin = (200 - 48 * 3) + BACK_BTN_WIDTH + 48 + 8
        return (left_margin, 8, right_margin, 8)

    def toggle_back_button(self, visible: bool):
        self.back_button.setVisible(visible)
        margins = self.get_container_margins(visible)
        self.c_layout.setContentsMargins(*margins)

    def handle_system_buttons(self):
        """Customizes the style of title bar buttons"""

        self.minBtn.setObjectName('CustomTitleBarBtn')
        self.maxBtn.setObjectName('CustomTitleBarBtn')
        self.closeBtn.setObjectName('CustomTitleBarBtn')
        self.minBtn.setStyleSheet(titleBarButtonStyles)
        self.maxBtn.setStyleSheet(titleBarButtonStyles)
        self.closeBtn.setStyleSheet(titleBarButtonStyles)
        self.closeBtn.setPressedBackgroundColor(QColor("#92202a"))

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
        
    def on_data_updated(self, title: str, can_go_back: bool):
        self.title_label.setText(title)
        self.toggle_back_button(can_go_back)
