from PySide6.QtWidgets import QWidget, QVBoxLayout

from components.common.scroll_view import ScrollView
from components.common.section_title import SectionTitle
from db.projects import ProjectModel


class NotesSection(QWidget):
    def __init__(self, project: ProjectModel, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        label = SectionTitle("Notes")
        scroll_view = ScrollView()
        layout.addWidget(label)
        layout.addWidget(scroll_view)
        self.setLayout(layout)
