from PySide6.QtCore import Qt
from PySide6.QtWidgets import QPushButton, QHBoxLayout, QLabel, QSizePolicy

from components.common.opacity_button import OpacityButton
from components.common.svg_icon import SvgIcon
from constants.colors import Colors

DEFAULT_OPACITY = 1
HOVER_OPACITY = 0.7
PRESSED_OPACITY = 0.5


class BackButton(OpacityButton):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setMinimumSize(80, 32)
        self.setCursor(Qt.PointingHandCursor)

        layout = self.get_layout()
        self.setLayout(layout)

    def get_layout(self):
        layout = QHBoxLayout()

        icon = SvgIcon("assets/svg/back-arrow.svg", 11, 12)
        text = QLabel("Back")
        text.setObjectName('back_button_label')
        text.setStyleSheet(f"""
            QLabel#back_button_label {{
                background: transparent;
                color: {Colors.FG_PRIMARY};
            }}
        """)

        layout.addWidget(icon)
        layout.addSpacing(4)
        layout.addWidget(text)
        layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        return layout
