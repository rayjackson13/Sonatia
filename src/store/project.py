from PySide6.QtCore import Signal, QObject
from models.file import FileModel


class ProjectStore(QObject):
    _instance = None

    data_updated = Signal(FileModel)

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
        self.__file = None

    def set_file(self, file: FileModel) -> None:
        self.__file = file
        self.data_updated.emit(file)

    def get_file(self) -> FileModel | None:
        return self.__file
