import sys
from PySide6.QtWidgets import QStackedWidget

from screens.home import HomeScreen
from screens.settings import SettingsScreen

screen_titles = {"main": "Home", "settings": "Settings"}


class Navigation(QStackedWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__history: list[str] = []
        self.__listeners = []
        self.__screen_map = {}

        self.register_screen("main", HomeScreen(self))
        self.register_screen("settings", SettingsScreen(self))

        self.navigate("main")

    @property
    def screen_title(self):
        return self.__screen_title

    def register_screen(self, uri, widget):
        self.__screen_map[uri] = widget
        self.addWidget(widget)

    def navigate(self, uri: str):
        if uri in self.__screen_map:
            self.__history.insert(0, uri)
            self.setCurrentWidget(self.__screen_map[uri])
            self.notify_listeners()
        else:
            print(f'The stack has no screen with uri: "{uri}".', file=sys.stderr)

    def go_back(self):
        try:
            self.__history.pop(0)
            prev_uri = self.__history[0]
            prev_widget = self.__screen_map[prev_uri]
            self.setCurrentWidget(prev_widget)
            self.notify_listeners()
        except:
            print(f"The stack is empty.", file=sys.stderr)

    def get_state(self):
        uri = self.__history[0]
        title = screen_titles[uri] if uri in screen_titles else ""
        size = len(self.__history)
        return (uri, title, size)

    def register_listener(self, listener):
        self.__listeners.append(listener)

    def notify_listeners(self):
        for listener in self.__listeners:
            listener.update_state(self.get_state())
