from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QScrollArea

from components.common.inset_shadow_box import InsetShadowBox
from models.file import FileModel
from store.project import ProjectStore

box_style = "QWidget#ScrollView { background-color: transparent; }"
area_style = "QWidget#ScrollViewArea { background-color: transparent; }"
container_style = "QWidget#ScrollViewContainer { background-color: transparent; }"


class ScrollView(InsetShadowBox):
    def __init__(self):
        super().__init__()
        self.setObjectName("ScrollView")
        self.setStyleSheet(box_style)
        self.setMinimumHeight(0)
        self.render_scroll_area()

    def render_scroll_area(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.setAlignment(Qt.AlignTop)

        scroll_area = QScrollArea()
        scroll_area.setMinimumHeight(0)
        scroll_area.setWidgetResizable(True)
        scroll_area.setObjectName("ScrollViewArea")
        scroll_area.setStyleSheet(area_style)

        scroll_container = QWidget()
        scroll_container.setObjectName("ScrollViewContainer")
        scroll_container.setStyleSheet(container_style)
        scroll_container.setMinimumHeight(0)

        scroll_layout = QVBoxLayout()
        scroll_layout.setContentsMargins(8, 8, 8, 8)
        scroll_layout.setSpacing(0)
        scroll_layout.setAlignment(Qt.AlignTop)

        scroll_container.setLayout(scroll_layout)
        scroll_area.setWidget(scroll_container)
        layout.addWidget(scroll_area)
        self.setLayout(layout)
        self.scroll_layout = scroll_layout

    def on_project_clicked(self, file: FileModel):
        store = ProjectStore.get_instance()
        store.set_file(file)
        self.__open_project()
