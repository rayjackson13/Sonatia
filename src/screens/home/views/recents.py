from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtGui import QPainter, QColor, QBrush, QPen
from PySide6.QtCore import Qt

from constants.colors import Colors

text_style = f"""
    QLabel {{
        color: {Colors.FG_PRIMARY};
        font-family: Inter, sans-serif;
        font-size: 24px;
        font-weight: 700;
        line-height: 24px;
        padding-top: 8px;
        padding-bottom: 8px;
        padding-left: 0;
        margin: 0;
        margin-left: -6px;
    }}
"""

box_style = f"""
    QWidget {{
        border-radius: 8px;
    }}
"""


class InsetShadowWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Black Inset Shadow on White Box")
        self.setMinimumHeight(200)

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


class RecentsSection(QWidget):
    def __init__(self):
        super().__init__()
        # TODO: remove fixed height
        # self.setFixedHeight(460)

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        l_text = QLabel("Recents")
        l_text.setStyleSheet(text_style)

        box = InsetShadowWidget()
        box.setStyleSheet(box_style)
        layout.addWidget(l_text)
        layout.addWidget(box, 1)
        self.setLayout(layout)
