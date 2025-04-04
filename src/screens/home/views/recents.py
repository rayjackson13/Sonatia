from typing import Callable
from functools import partial
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QScrollArea, QLayout

from components.common.scroll_view import ScrollView
from constants.colors import Colors
from db.manager import DatabaseManager, DBNames, AbstractDBController
from models.project import ProjectModel
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


class RecentsSection(QWidget):
    def __init__(self, open_project: Callable[[ProjectModel], None]):
        super().__init__()
        folders_controller = DatabaseManager.get_controller(DBNames.Folders)
        self.subscribe_to_db_updates(folders_controller)
        self.__open_project = open_project
        self._layout = QVBoxLayout()
        self.__files = index_files()
        self.init_ui()

    def clear_layout(self, layout: QLayout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

    def clear_list(self):
        self.clear_layout(self._layout)

    def init_ui(self):
        self.clear_list()
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)

        l_text = QLabel("Recents")
        l_text.setObjectName("RecentsSectionTitle")
        l_text.setStyleSheet(text_style)

        self.scrollview = ScrollView()
        self.render_list()

        self._layout.addWidget(l_text)
        self._layout.addWidget(self.scrollview, 1)
        self.setLayout(self._layout)

    def render_list(self):
        self.scrollview.scroll_layout.setSpacing(4)

        for file in self.__files:
            item = RecentsItem(file)
            item.clicked.connect(partial(self.on_project_clicked, file))
            self.scrollview.scroll_layout.addWidget(item)

    def on_project_clicked(self, file: ProjectModel):
        store = ProjectStore.get_instance()
        store.set_project(file)
        self.__open_project()
        
    def on_folders_updated(self):
        """Rescan and render projects in updated folders"""
        self.__files = index_files()
        self.init_ui()
        
    def subscribe_to_db_updates(self, controller: AbstractDBController):
        controller.data_updated.connect(self.on_folders_updated)
