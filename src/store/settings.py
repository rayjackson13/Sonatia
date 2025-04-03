from PySide6.QtCore import Signal, QObject

from db.folders import FolderDBController, FolderModel


class SettingsStore(QObject):
    _instance = None

    data_updated = Signal()

    def __new__(cls):
        """Create or return the singleton instance."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "_initialized"):
            super().__init__()

            self._initialized = True
            self.__db = FolderDBController()

    def add_folder(self, folder: str) -> None:
        self.__db.insert_folders([FolderModel(path=folder)])
        self.data_updated.emit()

    def get_folders(self) -> list[FolderModel]:
        return self.__db.get_all_folders()

    def remove_folder(self, folder_id: int) -> None:
        self.__db.delete_folder(folder_id)
        self.data_updated.emit()
