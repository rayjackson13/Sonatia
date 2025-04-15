from PySide6.QtWidgets import QLabel
from constants.colors import Colors

text_style = f"""
    QLabel#SectionTitle {{
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


class SectionTitle(QLabel):
    def __init__(self, text: str, parent=None):
        super().__init__(text, parent)
        self.setObjectName("SectionTitle")
        self.setStyleSheet(text_style)
        self.setFixedHeight(40)
