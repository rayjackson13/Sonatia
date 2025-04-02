from PySide6.QtCore import Signal, QObject


class NavigationStore(QObject):
    _instance = None

    data_updated = Signal(str, bool)

    @staticmethod
    def get_instance():
        """Get or create the singleton instance."""
        if NavigationStore._instance is None:
            NavigationStore._instance = NavigationStore()
        return NavigationStore._instance

    def __init__(self):
        if NavigationStore._instance is not None:
            raise Exception("This class is a singleton!")

        super().__init__()
        self.__title = ""
        self.__can_go_back = False
        
    def set_data(self, title: str, can_go_back: bool) -> None:
        self.__title = title
        self.__can_go_back = can_go_back
        self.data_updated.emit(title, can_go_back)

    def set_title(self, title: str) -> None:
        self.__title = title
        self.data_updated.emit(title, self.__can_go_back)

    def get_title(self) -> str:
        return self.__title

    def set_can_go_back(self, value: bool) -> None:
        self.__can_go_back = value
        self.data_updated.emit(self.__title, value)

    def get_can_go_back(self) -> bool:
        return self.__can_go_back
