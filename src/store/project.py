from PySide6.QtCore import Signal, QObject


class ProjectStore(QObject):
    _instance = None

    data_updated = Signal(int)

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
        self.__project_id = None

    def set_project_id(self, project_id: int | None) -> None:
        self.__project_id = project_id
        self.data_updated.emit(project_id)

    def get_project_id(self) -> int | None:
        return self.__project_id
