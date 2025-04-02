from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QColor, QBrush, QPen
from PySide6.QtCore import Qt

from constants.colors import Colors

class InsetShadowBox(QWidget):
    def __init__(self):
        super().__init__()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw the white box
        box_rect = self.rect()  # Padding around the box
        painter.setBrush(QBrush(QColor(Colors.BG_SECONDARY)))  # White box
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(box_rect, 8, 8)

        # Draw the black inset shadow
        shadow_color = QColor(0, 0, 0)  # Black color for shadow
        shadow_radius = 8  # Shadow radius (blur depth)
        painter.setBrush(Qt.NoBrush)

        for i in range(shadow_radius):
            alpha = int(63 * (1 - i / shadow_radius))  # Gradual transparency
            rect = box_rect.adjusted(i, i, -i, -i)
            corner_radius = 8 * (rect.width() / box_rect.width())
            shadow_color.setAlpha(alpha)  # Set transparency for shadow
            painter.setBrush(Qt.NoBrush)
            pen = QPen(QColor(shadow_color))
            pen.setWidth(1)
            painter.setPen(pen)
            painter.drawRoundedRect(rect, corner_radius, corner_radius)