from PySide6.QtWidgets import QWidget, QVBoxLayout

from components.common.scroll_view import ScrollView
from components.common.section_title import SectionTitle
from db.projects import ProjectModel


class LabelsSection(QWidget):
    def __init__(self, project: ProjectModel, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        label = SectionTitle("Labels")
        scroll_view = ScrollView()
        scroll_view.setFixedHeight(88)
        layout.addWidget(label)
        layout.addWidget(scroll_view)
        self.setLayout(layout)
