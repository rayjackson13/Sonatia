from PySide6.QtWidgets import QPushButton, QLabel, QHBoxLayout, QLayout, QSizePolicy
from PySide6.QtCore import Qt, QEvent

from components.common.svg_icon import SvgIcon
from constants.colors import Colors

button_style = f"""
    QPushButton#RecentsItem {{
        border: 0;
        background-color: transparent;
        color: {Colors.FG_PRIMARY};
        border-radius: 4px;
        height: 32px;
    }}
    
    QPushButton#RecentsItem:hover {{
        background-color: {Colors.HOVER};
        color: {Colors.BG_SECONDARY};
    }}
"""


def get_label_color(hover: bool):
    return Colors.WHITE if hover else Colors.FG_PRIMARY


def get_label_style(hover: bool):
    color = get_label_color(hover)

    return f"""
        QLabel#RecentsItemLabel {{
            font-size: 16px;
            line-height: 24px;
            color: {color};
            background-color: transparent;
        }}
    """


class RecentsItem(QPushButton):
    def __init__(self, name: str, file_path: str, tags: list[str], parent=None):
        super().__init__(parent)

        self.__name = name
        self.__file_path = file_path
        self.__tags = tags

        self.setFixedHeight(32)
        self.init_ui()

        self.installEventFilter(self)
        self.setCursor(Qt.PointingHandCursor)
        self.setObjectName('RecentsItem')
        self.setStyleSheet(button_style)

    def init_ui(self):
        layout = QHBoxLayout()
        layout.setContentsMargins(8, 0, 8, 0)
        layout.setSpacing(0)
        layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.draw_icon(layout)
        layout.addSpacing(16)
        self.draw_text(layout)

        self.setLayout(layout)

    def draw_icon(self, layout: QLayout):
        icon = SvgIcon("assets/svg/file.svg", 16, 16)
        layout.addWidget(icon)

    def draw_text(self, layout: QLayout):
        self.label = QLabel(self.__name)
        self.label.setObjectName('RecentsItemLabel')
        self.label.setStyleSheet(get_label_style(False))
        layout.addWidget(self.label)

    def eventFilter(self, obj, event):
        is_hovered = event.type() == QEvent.Enter
        label_style = get_label_style(is_hovered)

        if event.type() in (QEvent.Enter, QEvent.Leave):
            self.label.setStyleSheet(label_style)
            
        return super().eventFilter(obj, event)
