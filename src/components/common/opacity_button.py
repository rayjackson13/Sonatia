from PySide6.QtWidgets import QPushButton, QGraphicsOpacityEffect
from PySide6.QtCore import Qt


buttonStyle = f"""
    OpacityButton {{
        border: 0px;
    }}
"""

HOVER_OPACITY = 0.7
PRESS_OPACITY = 0.5


class OpacityButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setCursor(Qt.PointingHandCursor)
        self.setStyleSheet(buttonStyle)
        self.draw_fx()

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
