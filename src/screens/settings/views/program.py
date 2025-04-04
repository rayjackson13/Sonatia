from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QLayout,
)

from components.common.inset_shadow_box import InsetShadowBox
from components.common.opacity_button import OpacityButton
from components.common.svg_icon import SvgIcon, Alignment
from constants.colors import Colors
from utils.programs import ProgramHandler

text_style = f"""
    QLabel#ProgramSectionTitle {{
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

field_style = f"""
    QLabel#ProgramSectionField {{
        color: {Colors.FG_DISABLED};
        font-family: Inter, sans-serif;
        font-size: 16px;
        line-height: 24px;
    }}
"""


class ProgramSection(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        l_text = QLabel("Ableton location")
        l_text.setObjectName("ProgramSectionTitle")
        l_text.setStyleSheet(text_style)

        layout.addWidget(l_text)
        self.render_box(layout)

        self.setLayout(layout)
        self.setMinimumHeight(0)

    def render_box(self, layout: QLayout):
        box = InsetShadowBox()
        box.setFixedHeight(32)
        box_layout = QHBoxLayout()
        box_layout.setContentsMargins(16, 4, 16, 4)
        box_layout.setSpacing(0)
        box_layout.setAlignment(Qt.AlignVCenter)

        self.path_field = QLabel(self.get_path())
        self.path_field.setObjectName("ProgramSectionField")
        self.path_field.setStyleSheet(field_style)

        box_layout.addWidget(self.path_field)
        box_layout.addStretch()
        self.render_change_button(box_layout)
        box.setLayout(box_layout)
        layout.addWidget(box)
        
    def render_change_button(self, layout: QLayout):
        btn = OpacityButton()
        btn.setFixedWidth(16)
        btn_layout = QVBoxLayout()
        btn_layout.setAlignment(Qt.AlignVCenter)
        btn_layout.setContentsMargins(0,0,0,0)
        btn_layout.setSpacing(0)
        btn_layout.addWidget(SvgIcon('assets/svg/folder-open.svg', 16, 16, align=Alignment.Right))
        btn.setLayout(btn_layout)
        btn.clicked.connect(self.on_change_pressed)
        layout.addWidget(btn)

    def get_path(self):
        return ProgramHandler.get_path()
    
    def on_change_pressed(self):
            ProgramHandler.choose_program_path()
            self.path_field.setText(self.get_path())
