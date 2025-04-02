from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QFileDialog

from components.common.scroll_view import ScrollView
from constants.colors import Colors
from store.settings import SettingsStore

from .add_button import AddButton

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
        self.store = SettingsStore()
        self.store.data_updated.connect(self.on_data_updated)
        self.init_ui()

    def clear_list(self):
        while self.scrollview.scroll_layout.count():
            item = self.scrollview.scroll_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        l_text = QLabel("Project folders")
        l_text.setObjectName("FoldersSectionTitle")
        l_text.setStyleSheet(text_style)

        self.scrollview = ScrollView()
        self.render_list()

        layout.addWidget(l_text)
        layout.addWidget(self.scrollview)

        self.setLayout(layout)
        self.setMinimumHeight(0)
        
    
    def render_list(self):
        self.clear_list()
        
        data = self.get_folders()
        for item in data:
            self.scrollview.scroll_layout.addWidget(QLabel(item.path))
        
        add_btn = AddButton()
        add_btn.clicked.connect(self.on_add_pressed)
        self.scrollview.scroll_layout.addWidget(add_btn)

    def on_add_pressed(self):
        folder_dialog = QFileDialog()
        folder_dialog.setFileMode(QFileDialog.Directory)
        folder_dialog.setOption(QFileDialog.ShowDirsOnly, True)

        if folder_dialog.exec():
            selected_folder = folder_dialog.selectedFiles()[0]
            self.add_folder(selected_folder)

    def add_folder(self, folder_path: str):
        self.store.add_folder(folder_path)
        
    def get_folders(self):
        return self.store.get_folders()
        
    def on_data_updated(self):
        self.render_list()
