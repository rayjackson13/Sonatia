from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QScrollArea
from PySide6.QtGui import QPainter, QColor, QBrush, QPen
from PySide6.QtCore import Qt

from constants.colors import Colors

from .recents_item import RecentsItem

text_style = f"""
    QLabel#RecentsSectionTitle {{
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
    QWidget#RecentsSectionBox {{
        border-radius: 8px;
        background-color: transparent;
    }}
"""

files: list[tuple[str, str, list[str]]] = [
    ("В мыслях только ты", "", []),
    ("Улетели", "", []),
    ("Красивая", "", []),
    ("Сломан", "", []),
]


class InsetShadowWidget(QWidget):
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


class RecentsSection(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        l_text = QLabel("Recents")
        l_text.setObjectName('RecentsSectionTitle')
        l_text.setStyleSheet(text_style)

        box = InsetShadowWidget()
        box.setObjectName('RecentsSectionBox')
        box.setStyleSheet(box_style)
        self.init_box_contents(box)

        layout.addWidget(l_text)
        layout.addWidget(box, 1)
        self.setLayout(layout)

    def init_box_contents(self, parent: QWidget):
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.setAlignment(Qt.AlignTop)
        
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setObjectName('RecentsSectionBoxScroll')
        scroll_area.setStyleSheet('QWidget#RecentsSectionBoxScroll { background-color: transparent; }')

        scroll_container = QWidget()
        scroll_container.setObjectName('RecentsSectionBoxContainer')
        scroll_container.setStyleSheet('QWidget#RecentsSectionBoxContainer { background-color: transparent; }')
        scroll_layout = QVBoxLayout()
        scroll_layout.setContentsMargins(8, 8, 8, 8)
        scroll_layout.setSpacing(4)
        scroll_layout.setAlignment(Qt.AlignTop)

        for file_data in files:
            item = RecentsItem(
                name=file_data[0], file_path=file_data[1], tags=file_data[2]
            )
            scroll_layout.addWidget(item)
            
        scroll_container.setLayout(scroll_layout)
        scroll_area.setWidget(scroll_container)
        layout.addWidget(scroll_area)
        parent.setLayout(layout)
