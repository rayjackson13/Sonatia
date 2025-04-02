from typing import Callable
from functools import partial
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QScrollArea

from components.common.inset_shadow_box import InsetShadowBox
from constants.colors import Colors
from models.file import FileModel
from store.project import ProjectStore
from utils.files import index_files

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
        background-color: transparent;
    }}
"""

files: list[tuple[str, str, list[str]]] = [
    ("В мыслях только ты", "", []),
    ("Улетели", "", []),
    ("Красивая", "", []),
    ("Сломан", "", []),
]


class RecentsSection(QWidget):
    def __init__(self, open_project: Callable[[FileModel], None]):
        super().__init__()

        self.__open_project = open_project
        self.__files = index_files()

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        l_text = QLabel("Recents")
        l_text.setObjectName("RecentsSectionTitle")
        l_text.setStyleSheet(text_style)

        box = InsetShadowBox()
        box.setObjectName("RecentsSectionBox")
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
        scroll_area.setObjectName("RecentsSectionBoxScroll")
        scroll_area.setStyleSheet(
            "QWidget#RecentsSectionBoxScroll { background-color: transparent; }"
        )

        scroll_container = QWidget()
        scroll_container.setObjectName("RecentsSectionBoxContainer")
        scroll_container.setStyleSheet(
            "QWidget#RecentsSectionBoxContainer { background-color: transparent; }"
        )
        scroll_layout = QVBoxLayout()
        scroll_layout.setContentsMargins(8, 8, 8, 8)
        scroll_layout.setSpacing(4)
        scroll_layout.setAlignment(Qt.AlignTop)

        files = sorted(self.__files, key=lambda x: x.updated_at, reverse=True)
        for file in files:
            item = RecentsItem(file)
            item.clicked.connect(partial(self.on_project_clicked, file))
            scroll_layout.addWidget(item)

        scroll_container.setLayout(scroll_layout)
        scroll_area.setWidget(scroll_container)
        layout.addWidget(scroll_area)
        parent.setLayout(layout)

    def on_project_clicked(self, file: FileModel):
        store = ProjectStore.get_instance()
        store.set_file(file)
        self.__open_project()
