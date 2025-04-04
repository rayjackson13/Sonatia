from functools import partial
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLayout

from components.common.scroll_view import ScrollView
from db.manager import DatabaseManager, DBNames, AbstractDBController
from models.project import ProjectModel
from navigation.index import Navigation
from store.project import ProjectStore
from utils.files import index_files, list_files
from utils.projects import get_project_title

from .header import RecentsHeader
from .recents_item import RecentsItem

box_style = f"""
    QWidget#RecentsSectionBox {{
        background-color: transparent;
    }}
"""


class RecentsSection(QWidget):
    def __init__(self):
        super().__init__()
        self.subscribe_to_db_updates()
        self._layout = QVBoxLayout()
        index_files()
        self.__files = list_files()
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

        header = RecentsHeader()
        header.refresh_btn.clicked.connect(self.on_folders_updated)

        self.scrollview = ScrollView()
        self.render_list()

        self._layout.addWidget(header)
        self._layout.addWidget(self.scrollview, 1)
        self.setLayout(self._layout)

    def render_list(self):
        self.scrollview.scroll_layout.setSpacing(4)

        for file in self.__files:
            item = RecentsItem(file)
            item.clicked.connect(partial(self.open_project, file))
            item.open_btn.clicked.connect(partial(self.open_project, file))
            self.scrollview.scroll_layout.addWidget(item)
        
    def on_folders_updated(self):
        """Rescan and render projects in updated folders"""
        index_files()
        self.__files = list_files()
        self.init_ui()
        
    def on_projects_updated(self):
        """Rescan and render projects in updated folders"""
        self.__files = list_files()
        self.init_ui()
        
    def subscribe_to_db_updates(self):
        folders_controller = DatabaseManager.get_controller(DBNames.Folders)
        projects_controller = DatabaseManager.get_controller(DBNames.Projects)
        folders_controller.data_updated.connect(self.on_folders_updated)
        projects_controller.data_updated.connect(self.on_projects_updated)
        
    def open_project(self, proj: ProjectModel):
        store = ProjectStore.get_instance()
        store.set_project(proj)
        Navigation().navigate('project', get_project_title(proj))
