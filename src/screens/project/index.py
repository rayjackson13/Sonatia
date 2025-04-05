from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QLayout
from PySide6.QtCore import Qt

from db.manager import DatabaseManager, DBNames
from db.projects import ProjectModel
from navigation.index import Navigation
from store.project import ProjectStore
from utils.projects import get_project_title

from .views.hero import HeroSection


class ProjectScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.navigation = Navigation()
        self.store = ProjectStore.get_instance()
        self.db = DatabaseManager.get_controller(DBNames.Projects)
        self.store.data_updated.connect(self.on_data_updated)
        self.db.data_updated.connect(self.on_data_updated)

        self._layout = QVBoxLayout(self)
        self.setLayout(self._layout)

        self.render()

    def clear_layout(self, layout: QLayout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

    def render(self):        
        project = self.get_project()
        if not project:
            return
        
        self.clear_layout(self._layout)
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)
        self._layout.setAlignment(Qt.AlignCenter | Qt.AlignTop)

        hero = HeroSection(project)
        label = QLabel(get_project_title(project))
        label.setObjectName("ProjectScreenTitle")
        label.setStyleSheet("QLabel#ProjectScreenTitle { color: white; }")
        button = QPushButton("Go Back")
        button.setObjectName("SettingsScreenBack")
        button.setStyleSheet("QPushButton#SettingsScreenBack { color: white; }")
        button.clicked.connect(self.navigation.go_back)

        self._layout.addWidget(hero)
        self._layout.addWidget(label)
        self._layout.addWidget(button)
        
    def get_project(self) -> ProjectModel | None:
        project_id = self.store.get_project_id()
        if not project_id:
            return None
        
        return self.db.fetch_by_id(project_id)

    def on_data_updated(self) -> None:
        """Update the UI when data changes in the ProjectStore."""
        self.render()
