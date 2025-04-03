from PySide6.QtWidgets import QHBoxLayout, QLabel

from components.common.svg_icon import SvgIcon
from constants.colors import Colors

from .opacity_button import OpacityButton

icon_path_map = {
    "add": "assets/svg/plus.svg",
    "folder-open": "assets/svg/folder-open.svg",
    "gear": "assets/svg/gear.svg",
}

labelStyle = f"""
    QLabel#ButtonWithIconLabel {{
        color: {Colors.FG_PRIMARY};
        background-color: transparent;
        font-size: 16px;
        line-height: 20px;
    }}
"""


class ButtonWithIcon(OpacityButton):
    def __init__(self, title: str, icon_name: str, parent=None):
        super().__init__(parent)
        self.__title = title
        self.__icon_name = icon_name
        self.draw_ui()

    def draw_ui(self):
        self.setFixedHeight(20)
        self.setObjectName("ButtonWithIcon")
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        icon = self.init_icon()
        label = self.init_label()
        layout.addWidget(icon)
        layout.addSpacing(12)
        layout.addWidget(label)
        self.setLayout(layout)

    def init_label(self):
        label = QLabel(self.__title)
        label.setObjectName("ButtonWithIconLabel")
        label.setStyleSheet(labelStyle)
        return label

    def init_icon(self):
        if self.__icon_name not in icon_path_map:
            return

        icon_path = icon_path_map[self.__icon_name]
        icon = SvgIcon(icon_path, 16, 16)
        return icon
