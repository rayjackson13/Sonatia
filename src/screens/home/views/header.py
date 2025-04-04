from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout, QLayout
from PySide6.QtCore import Qt

from components.common.opacity_button import OpacityButton
from components.common.svg_icon import SvgIcon, Alignment
from constants.colors import Colors

text_style = f"""
    QLabel#RecentsHeaderTitle {{
        color: {Colors.FG_PRIMARY};
        font-family: Inter, sans-serif;
        font-size: 24px;
        font-weight: 700;
        line-height: 24px;
    }}
"""


class RecentsHeader(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedHeight(40)

        layout = QHBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setAlignment(Qt.AlignVCenter)

        self.render_label(layout)
        layout.addStretch(1)
        self.render_refresh_btn(layout)
        self.setLayout(layout)

    def render_label(self, layout: QLayout):
        label = QLabel("Recents")
        label.setObjectName("RecentsHeaderTitle")
        label.setStyleSheet(text_style)
        layout.addWidget(label)

    def render_refresh_btn(self, layout: QLayout):
        self.refresh_btn = OpacityButton()
        self.refresh_btn.setFixedSize(20, 32)
        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(0)
        btn_layout.setContentsMargins(0, 0, 0, 0)
        btn_layout.addWidget(
            SvgIcon("assets/svg/refresh.svg", 20, 20, align=Alignment.Right)
        )
        self.refresh_btn.setLayout(btn_layout)
        layout.addWidget(self.refresh_btn)
