from PySide6.QtCore import Qt
from PySide6.QtWidgets import QPushButton, QHBoxLayout, QLabel, QSizePolicy

from components.common.svg_icon import SvgIcon
from constants.colors import Colors

DEFAULT_OPACITY = 1
HOVER_OPACITY = 0.7
PRESSED_OPACITY = 0.5


class BackButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setMinimumSize(80, 32)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setStyleSheet(
            f"""
            QPushButton {{
                background-color: transparent;
                border: none;
                border-radius: 4px;
            }}
            QPushButton:hover {{ background-color: {Colors.HOVER}; }}
            QPushButton:pressed {{ background-color: {Colors.SELECTED}; }}
        """
        )
        self.setCursor(Qt.PointingHandCursor)

        layout = self.get_layout()
        self.setLayout(layout)
        self.raise_()

    def get_layout(self):
        layout = QHBoxLayout()

        icon = SvgIcon("assets/svg/back-arrow.svg", 11, 12)
        text = QLabel("Back")
        text.setStyleSheet(f"background: transparent; color: {Colors.FG_PRIMARY};")

        layout.addWidget(icon)
        layout.addSpacing(4)
        layout.addWidget(text)
        layout.setAlignment(Qt.AlignCenter)

        layout.setContentsMargins(8, 0, 8, 0)
        layout.setSpacing(0)
        return layout
