from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QLayout
from PySide6.QtCore import Qt

from navigation.index import Navigation
from store.project import ProjectStore


class ProjectScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.navigation = Navigation()
        self.store = ProjectStore.get_instance()
        self.store.data_updated.connect(self.on_data_updated)

        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)

        self.render()

    def clear_layout(self, layout: QLayout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

    def render(self):
        self.clear_layout(self.layout)

        title_text = self.get_project_title()
        self.layout.setAlignment(Qt.AlignCenter)
        label = QLabel(title_text)
        label.setObjectName("ProjectScreenTitle")
        label.setStyleSheet("QLabel#ProjectScreenTitle { color: white; }")
        button = QPushButton("Go Back")
        button.setObjectName("SettingsScreenBack")
        button.setStyleSheet("QPushButton#SettingsScreenBack { color: white; }")
        button.clicked.connect(self.navigation.go_back)

        self.layout.addWidget(label)
        self.layout.addWidget(button)

    def get_project_title(self) -> str:
        project = self.store.get_project()
        return project.name if project else ""

    def on_data_updated(self) -> None:
        """Update the UI when data changes in the ProjectStore."""
        self.render()
