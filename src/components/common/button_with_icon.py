from PySide6.QtWidgets import QPushButton, QHBoxLayout, QLabel, QGraphicsOpacityEffect
from PySide6.QtCore import Qt

from components.common.svg_icon import SvgIcon
from constants.colors import Colors

icon_path_map = {
    "add": "assets/svg/plus.svg",
    "folder-open": "assets/svg/folder-open.svg",
    "gear": "assets/svg/gear.svg",
}

buttonStyle = f"""
    QPushButton {{
        border: 0px;
    }}
"""

labelStyle = f"""
    QLabel {{
        color: {Colors.FG_PRIMARY};
        background-color: transparent;
        font-size: 20px;
        line-height: 24px;
    }}
"""

HOVER_OPACITY = 0.7
PRESS_OPACITY = 0.5


class ButtonWithIcon(QPushButton):
    def __init__(self, title: str, icon_name: str, parent=None):
        super().__init__(parent)
        self.__title = title
        self.__icon_name = icon_name
        self.setCursor(Qt.PointingHandCursor)
        self.draw_ui()
        self.draw_fx()

    def draw_ui(self):
        self.setFixedHeight(24)
        self.setStyleSheet(buttonStyle)
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
        label.setStyleSheet(labelStyle)
        return label

    def init_icon(self):
        if self.__icon_name not in icon_path_map:
            return

        icon_path = icon_path_map[self.__icon_name]
        icon = SvgIcon(icon_path, 16, 16)
        return icon

    def draw_fx(self):
        self.__opacity_fx = QGraphicsOpacityEffect()
        self.__opacity_fx.setOpacity(1)
        self.setGraphicsEffect(self.__opacity_fx)

    def enterEvent(self, event):
        self.__opacity_fx.setOpacity(HOVER_OPACITY)
        return super().enterEvent(event)

    def leaveEvent(self, event):
        self.__opacity_fx.setOpacity(1)
        return super().leaveEvent(event)

    def mousePressEvent(self, e):
        self.__opacity_fx.setOpacity(PRESS_OPACITY)
        return super().mousePressEvent(e)

    def mouseReleaseEvent(self, e):
        self.__opacity_fx.setOpacity(HOVER_OPACITY)
        return super().mouseReleaseEvent(e)
