from PySide6.QtWidgets import QVBoxLayout
from qframelesswindow import FramelessWindow

from constants.colors import Colors
from components.common.titlebar import CustomTitleBar
from components.common.footer import Footer
from navigation.index import Navigation
from screens.home.index import HomeScreen
from screens.project.index import ProjectScreen
from screens.settings.index import SettingsScreen

from utils.window import center_window


class MainWindow(FramelessWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumWidth(1200)
        self.setMinimumHeight(900)
        self.navigation = Navigation(stack_parent=self)
        self.init_nav()

        center_window(self)

        # Remove the titlebar
        self.setWindowTitle("Sonatia")  # Optional for internal title usage
        self.setResizeEnabled(True)  # Enable resizing if needed

        self.setTitleBar(CustomTitleBar(self))
        self.setObjectName('MainWindow')

        # Paint the entire window black
        self.setStyleSheet(f"QWidget#MainWindow {{ background-color: {Colors.BG_PRIMARY}; }}")
        self.setContentsMargins(0, 0, 0, 0)

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)  # Add margins for titlebar
        layout.setSpacing(0)
        layout.addWidget(self.navigation.stack, stretch=1)
        layout.addWidget(Footer(self))
        self.setLayout(layout)
        
    def init_nav(self):
        self.navigation.register_screen("main", HomeScreen())
        self.navigation.register_screen("settings", SettingsScreen())
        self.navigation.register_screen("project", ProjectScreen())

        self.navigation.navigate("main")
