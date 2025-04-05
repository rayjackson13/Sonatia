import sys
from PySide6.QtWidgets import QStackedWidget
from PySide6.QtCore import Signal, QObject

screen_titles = {"main": "", "settings": "Settings"}


def get_title_by_uri(uri: str) -> str:
    return screen_titles[uri] if uri in screen_titles else ""


class Navigation(QObject):
    _instance = None  # Singleton instance

    data_updated = Signal()

    def __new__(cls, stack_parent=None):
        if not cls._instance:
            cls._instance = super(Navigation, cls).__new__(cls)
        return cls._instance

    def __init__(self, stack_parent=None):
        if not hasattr(self, "_initialized"):
            super().__init__()
            self.stack = QStackedWidget(stack_parent)
            self.__history: list[tuple[str, str]] = []
            self.__screen_map = {}

            self._initialized = True

    def register_screen(self, uri, widget):
        self.__screen_map[uri] = widget
        self.stack.addWidget(widget)

    def navigate(self, uri: str, title: str = None):
        if uri in self.__screen_map:
            path_title = title if title else get_title_by_uri(uri)
            self.__history.insert(0, (uri, path_title,))
            self.stack.setCurrentWidget(self.__screen_map[uri])
            self.data_updated.emit()
        else:
            print(f'The stack has no screen with uri: "{uri}".', file=sys.stderr)

    def go_back(self):
        try:
            self.__history.pop(0)
            prev_entry = self.__history[0]
            prev_uri = prev_entry[0] # uri of a previous entry
            prev_widget = self.__screen_map[prev_uri]
            self.stack.setCurrentWidget(prev_widget)
            self.data_updated.emit()
        except:
            print(f"The stack is empty.", file=sys.stderr)

    @property
    def title(self) -> str | None:
        prev_entry = self.__history[0]
        return prev_entry[1] if len(self.__history) > 0 else ''
    
    def set_title(self, title: str) -> None:
        if len(self.__history) > 0:
            entry = self.__history[0]
            self.__history[0] = (entry[0], title)
            self.data_updated.emit()

    @property
    def can_go_back(self) -> bool:
        return len(self.__history) > 1
    
    @property
    def uri(self) -> str | None:
        route = self.__history[0]
        return route[0]
