import sys
from PySide6.QtWidgets import QStackedWidget

from screens.home.index import HomeScreen
from screens.settings.index import SettingsScreen
from screens.project.index import ProjectScreen
from store.navigation import NavigationStore

screen_titles = {"main": "Home", "settings": "Settings"}


class Navigation(QStackedWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.__history: list[str] = []
        self.__listeners = []
        self.__screen_map = {}
        self.__store = NavigationStore.get_instance()

        self.register_screen("main", HomeScreen(self))
        self.register_screen("settings", SettingsScreen(self))
        self.register_screen("project", ProjectScreen(self))

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
            self.__store.set_data(self.get_title_by_uri(uri), len(self.__history) > 1)
            self.setCurrentWidget(self.__screen_map[uri])
        else:
            print(f'The stack has no screen with uri: "{uri}".', file=sys.stderr)

    def go_back(self):
        try:
            self.__history.pop(0)
            prev_uri = self.__history[0]
            prev_widget = self.__screen_map[prev_uri]
            self.__store.set_data(self.get_title_by_uri(prev_uri), len(self.__history) > 1)
            self.setCurrentWidget(prev_widget)
        except:
            print(f"The stack is empty.", file=sys.stderr)

    def get_title_by_uri(self, uri: str):
        cur_title = self.__store.get_title()
        return screen_titles[uri] if uri in screen_titles else cur_title
