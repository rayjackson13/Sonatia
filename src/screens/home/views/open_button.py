import os
from PySide6.QtWidgets import QPushButton, QSizePolicy

from components.common.opacity_button import OpacityButton
from constants.colors import Colors
from store.navigation import NavigationStore

btn_style = f"""
    OpenInDAWButton {{
        color: {Colors.SELECTED};
        background-color: {Colors.WHITE};
        padding: 2px 4px;
        border-radius: 4px;
        font-size: 14px;
        line-height: 16px;
    }}
"""


class OpenInDAWButton(OpacityButton):
    def __init__(self, path: str, parent=None):
        super().__init__(parent)

        self.__file_path = path
        self.setMinimumWidth(0)
        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.setText("Open in DAW")
        self.clicked.connect(self.on_click)
        self.setStyleSheet(btn_style)

    def on_click(self):
        # os.startfile(self.__file_path)
        navigation = NavigationStore.get_instance()
        navigation.navigate('project')
