from PySide6.QtWidgets import QHBoxLayout, QLabel, QLineEdit
from PySide6.QtCore import Qt

from components.common.editable_label import EditableLabel
from components.common.gradient_image import GradientImageWidget
from components.common.opacity_button import OpacityButton
from constants.colors import Colors
from db.manager import DatabaseManager, DBNames
from db.projects import ProjectModel
from navigation.index import Navigation
from utils.files import open_file
from utils.projects import get_project_title

button_style = f"""
    QPushButton#HeroSectionButton {{
        color: {Colors.SELECTED};
        background-color: {Colors.WHITE};
        padding: 12px 16px;
        border-radius: 4px;
        font-size: 16px;
        line-height: 16px;
    }}
"""


class HeroSection(GradientImageWidget):
    def __init__(self, project: ProjectModel, parent=None):
        super().__init__(parent)
        self.__project = project
        self.setMinimumWidth(1200)
        self.setMinimumHeight(350)

        layout = QHBoxLayout()
        layout.setContentsMargins(36, 48, 48, 32)
        layout.setSpacing(0)
        layout.setAlignment(Qt.AlignBottom | Qt.AlignLeft)

        label = EditableLabel(get_project_title(self.__project))
        label.text_changed.connect(self.on_title_changed)

        button = OpacityButton("Open in DAW")
        button.setObjectName("HeroSectionButton")
        button.setStyleSheet(button_style)
        button.setFixedHeight(40)
        button.setCursor(Qt.PointingHandCursor)
        button.clicked.connect(self.on_open)

        layout.addWidget(label)
        layout.addStretch()
        layout.addWidget(button)
        self.setLayout(layout)
        label.clearFocus()

    def on_open(self):
        file_path = self.__project.path
        open_file(file_path)

    def on_title_changed(self, new_title):
        controller = DatabaseManager.get_controller(DBNames.Projects)
        navigation = Navigation()
        self.__project.title = new_title
        controller.update_record(self.__project)
        navigation.set_title(new_title)
        
