from PySide6.QtCore import Signal, QObject

from utils.files import index_files


class IndexWorker(QObject):
    """Worker to index files"""

    indexing_complete = Signal()

    def index_files(self):
        try:
            index_files()
            self.indexing_complete.emit()
        except Exception as e:
            print(f"There was a problem while indexing files: {e}")
