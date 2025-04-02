from PySide6.QtWidgets import QHBoxLayout, QLabel, QPushButton, QLayout
from PySide6.QtCore import Qt, QEvent

from components.common.svg_icon import SvgIcon, Alignment
from constants.colors import Colors

root_style = f"""
    FoldersListItem {{
        border: 0;
        background-color: transparent;
        color: {Colors.FG_PRIMARY};
        border-radius: 4px;
        height: 32px;
    }}
    
    FoldersListItem:hover {{
        background-color: {Colors.HOVER};
        color: {Colors.BG_SECONDARY};
    }}
"""

delete_style = f"""
    QPushButton#FolderListItemDelButton {{
        margin-left: 4px;
        text-align: right;
    }}
    QPushButton#FolderListItemDelButton:hover {{
        background-color: transparent;
    }}
    QPushButton#FolderListItemDelButton:clicked {{
        background-color: transparent;
    }}
"""

def get_label_style(hover: bool):
    color = Colors.WHITE if hover else Colors.FG_PRIMARY

    return f"""
        QLabel#FolderListItemLabel {{
            font-size: 16px;
            line-height: 24px;
            color: {color};
            background-color: transparent;
        }}
    """


class FoldersListItem(QLabel):
    def __init__(self, folder_path: str, parent=None):
        super().__init__(parent)
        
        self.setObjectName('FoldersListItem')
        self.setStyleSheet(root_style)
        self.setMinimumHeight(32)
        self.raise_()
        
        layout = QHBoxLayout()
        layout.setContentsMargins(8, 0, 8, 0)
        layout.setSpacing(0)

        icon = SvgIcon('assets/svg/folder.svg', 16, 16)       
        label = QLabel(folder_path)
        label.setObjectName('FolderListItemLabel')
        label.setStyleSheet(get_label_style(False))
        
        layout.addWidget(icon)
        layout.addSpacing(12)
        layout.addWidget(label)
        layout.addStretch(1)
        self.render_remove_button(layout)
        
        self.setLayout(layout)
        
    def render_remove_button(self, layout: QLayout):
        button = QPushButton()
        button.setFixedWidth(32)
        button.setObjectName('FolderListItemDelButton')
        button.setStyleSheet(delete_style)
        button.setCursor(Qt.PointingHandCursor)
        b_layout = QHBoxLayout()
        b_layout.setAlignment(Qt.AlignRight)
        b_layout.setContentsMargins(0,0,0,0)
        b_layout.setSpacing(0)
        icon = SvgIcon('assets/svg/remove.svg', 16, 16, Alignment.Right)
        b_layout.addWidget(icon)
        button.setLayout(b_layout)
        layout.addWidget(button, stretch=0)

    def eventFilter(self, obj, event):
        is_hovered = event.type() == QEvent.Enter
        label_style = get_label_style(is_hovered)

        if event.type() in (QEvent.Enter, QEvent.Leave):
            self.label.setStyleSheet(label_style)
            
        return super().eventFilter(obj, event)
        