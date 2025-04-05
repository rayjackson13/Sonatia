from PySide6.QtWidgets import QHBoxLayout, QLabel, QLayout
from PySide6.QtCore import Qt, QEvent

from components.common.opacity_button import OpacityButton
from components.common.svg_icon import SvgIcon, Alignment
from constants.colors import Colors
from db.manager import DatabaseManager, DBNames
from db.folders import FolderModel

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
        border: 0px;
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
    def __init__(self, folder: FolderModel, on_remove_pressed, parent=None):
        super().__init__(parent)

        self.on_remove_pressed = on_remove_pressed
        self.__folder_id = folder.id
        self.setObjectName("FoldersListItem")
        self.setStyleSheet(root_style)
        self.setMinimumHeight(32)
        self.raise_()

        layout = QHBoxLayout()
        layout.setContentsMargins(8, 0, 8, 0)
        layout.setSpacing(0)

        icon = SvgIcon("assets/svg/folder.svg", 16, 16)
        label = QLabel(folder.path)
        label.setObjectName("FolderListItemLabel")
        label.setStyleSheet(get_label_style(False))

        layout.addWidget(icon)
        layout.addSpacing(12)
        layout.addWidget(label)
        layout.addStretch(1)
        self.render_remove_button(layout)

        self.setLayout(layout)

    def render_remove_button(self, layout: QLayout):
        button = OpacityButton()
        button.setFixedWidth(32)
        button.setObjectName("FolderListItemDelButton")
        button.setStyleSheet(delete_style)
        button.clicked.connect(lambda: self.on_remove_pressed(self.__folder_id))

        b_layout = QHBoxLayout()
        b_layout.setAlignment(Qt.AlignRight)
        b_layout.setContentsMargins(0, 0, 0, 0)
        b_layout.setSpacing(0)

        icon = SvgIcon("assets/svg/remove.svg", 16, 16, Alignment.Right)
        b_layout.addWidget(icon)
        button.setLayout(b_layout)
        layout.addWidget(button, stretch=0)

    def eventFilter(self, obj, event):
        is_hovered = event.type() == QEvent.Enter
        label_style = get_label_style(is_hovered)

        if event.type() in (QEvent.Enter, QEvent.Leave):
            self.label.setStyleSheet(label_style)

        return super().eventFilter(obj, event)
