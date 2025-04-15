from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QFrame, QSizePolicy
from db.projects import ProjectModel

from .todo import TodoSection


class MainGrid(QWidget):
    def __init__(self, project: ProjectModel, parent=None):
        super().__init__(parent)
        layout = QHBoxLayout()
        layout.setContentsMargins(48, 24, 48, 24)
        layout.setSpacing(24)
        columns = [Column() for _ in range(3)]
        
        columns[0].layout().addWidget(TodoSection(project))

        list(map(layout.addWidget, columns))

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setLayout(layout)


class Column(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setLayout(layout)
