from PySide6.QtWidgets import QPushButton, QLabel, QHBoxLayout
from PySide6.QtCore import Qt, QEvent

from components.common.svg_icon import SvgIcon
from constants.colors import Colors

button_style = f"""
    QPushButton#AddButton {{
        border: 0;
        background-color: transparent;
        color: {Colors.FG_PRIMARY};
        border-radius: 4px;
        height: 32px;
    }}
    
    QPushButton#AddButton:hover {{
        background-color: {Colors.HOVER};
        color: {Colors.BG_SECONDARY};
    }}
    
    QPushButton#AddButton:pressed {{
        background-color: {Colors.SELECTED};
        color: {Colors.BG_SECONDARY};
    }}
"""


def get_label_color(hover: bool):
    return Colors.WHITE if hover else Colors.FG_PRIMARY


def get_label_style(hover: bool):
    color = get_label_color(hover)

    return f"""
        QLabel#AddButtonLabel {{
            font-size: 16px;
            line-height: 24px;
            color: {color};
            background-color: transparent;
        }}
    """


class AddButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.init_ui()

    def init_ui(self):
        layout = QHBoxLayout()
        layout.setContentsMargins(8, 0, 8, 0)
        layout.setSpacing(0)
        layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        icon = SvgIcon("assets/svg/plus.svg", 16, 16)
        self.label = QLabel("Add")
        self.label.setObjectName('AddButtonLabel')
        self.label.setStyleSheet(get_label_style(False))

        layout.addWidget(icon)
        layout.addSpacing(12)
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.setObjectName("AddButton")
        self.setStyleSheet(button_style)
        self.setCursor(Qt.PointingHandCursor)

    def eventFilter(self, obj, event):
        is_hovered = event.type() == QEvent.Enter
        label_style = get_label_style(is_hovered)

        if event.type() in (QEvent.Enter, QEvent.Leave):
            self.label.setStyleSheet(label_style)
            
        return super().eventFilter(obj, event)
