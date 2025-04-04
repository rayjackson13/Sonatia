import threading
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QFileDialog, QLayout

from components.common.scroll_view import ScrollView
from constants.colors import Colors
from db.manager import DatabaseManager, DBNames
from db.folders import FolderModel
from utils.index_worker import IndexWorker

from .add_button import AddButton
from .list_item import FoldersListItem

text_style = f"""
    QLabel#FoldersSectionTitle {{
        color: {Colors.FG_PRIMARY};
        font-family: Inter, sans-serif;
        font-size: 24px;
        font-weight: 700;
        line-height: 24px;
        padding-top: 8px;
        padding-bottom: 8px;
        padding-left: 0;
        margin: 0;
        margin-left: -6px;
    }}
"""


class FoldersSection(QWidget):
    def __init__(self):
        super().__init__()
        self._db_controller = DatabaseManager.get_controller(DBNames.Folders)
        self.subscribe_to_db_updates()
        self._layout = QVBoxLayout()
        self.render_ui()
        self.worker = IndexWorker()

    def clear_layout(self, layout: QLayout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

    def clear_list(self):
        self.clear_layout(self._layout)

    def render_ui(self):
        self.clear_list()
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)

        l_text = QLabel("Project folders")
        l_text.setObjectName("FoldersSectionTitle")
        l_text.setStyleSheet(text_style)

        self.scrollview = ScrollView()
        self.scrollview.setMaximumHeight(380)
        self.render_list()

        self._layout.addWidget(l_text)
        self._layout.addWidget(self.scrollview)

        self.setLayout(self._layout)
        self.setMinimumHeight(0)

    def render_list(self):
        self.clear_list()
        self.scrollview.scroll_layout.setSpacing(4)

        add_btn = AddButton()
        add_btn.clicked.connect(self.on_add_pressed)
        self.scrollview.scroll_layout.addWidget(add_btn)
        data = self.get_folders()
        for item in data:
            self.scrollview.scroll_layout.addWidget(FoldersListItem(item, self.on_remove_pressed))

    def on_add_pressed(self):
        folder_dialog = QFileDialog()
        folder_dialog.setFileMode(QFileDialog.Directory)
        folder_dialog.setOption(QFileDialog.ShowDirsOnly, True)

        if folder_dialog.exec():
            selected_folder = folder_dialog.selectedFiles()[0]
            self.add_folder(selected_folder)
        
    def on_remove_pressed(self, id: int):
        self._db_controller.delete_record(id)
        self.start_indexing()

    def add_folder(self, folder_path: str):
        self._db_controller.insert_records([FolderModel(path=folder_path)])
        self.start_indexing()

    def get_folders(self):
        return self._db_controller.fetch_all()
            
    def start_indexing(self):
        thread = threading.Thread(target=self.worker.index_files)
        thread.start()

    def subscribe_to_db_updates(self):
        self._db_controller.data_updated.connect(self.render_ui)
