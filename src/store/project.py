from PySide6.QtCore import Signal, QObject
from models.project import ProjectModel


class ProjectStore(QObject):
    _instance = None

    data_updated = Signal(ProjectModel)

    @staticmethod
    def get_instance():
        """Get or create the singleton instance."""
        if ProjectStore._instance is None:
            ProjectStore._instance = ProjectStore()
        return ProjectStore._instance

    def __init__(self):
        if ProjectStore._instance is not None:
            raise Exception("This class is a singleton!")

        super().__init__()
        self.__project = None

    def set_project(self, project: ProjectModel) -> None:
        self.__project = project
        self.data_updated.emit(project)

    def get_project(self) -> ProjectModel | None:
        return self.__project
