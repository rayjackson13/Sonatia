from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QFrame, QSizePolicy
from db.projects import ProjectModel

from .sections.todo import TodoSection
from .sections.demos import DemosSection
from .sections.labels import LabelsSection
from .sections.notes import NotesSection
from .sections.lyrics import LyricsSection


class MainGrid(QWidget):
    def __init__(self, project: ProjectModel, parent=None):
        super().__init__(parent)
        layout = QHBoxLayout()
        layout.setContentsMargins(48, 24, 48, 24)
        layout.setSpacing(24)
        columns = [Column() for _ in range(3)]
        
        columns[0].layout().addWidget(TodoSection(project), stretch=1)
        columns[0].layout().addWidget(DemosSection(project))
        columns[1].layout().addWidget(LabelsSection(project))
        columns[1].layout().addWidget(NotesSection(project), stretch=1)
        columns[2].layout().addWidget(LyricsSection(project))

        list(map(layout.addWidget, columns))

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setLayout(layout)


class Column(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(24)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setLayout(layout)
