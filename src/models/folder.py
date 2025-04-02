class FolderModel:
    def __init__(self, folder_id=None, path=None):
        self.id = folder_id
        self.path = path
    
    def __repr__(self):
        """Representation for debugging."""
        return f"FileModel(id={self.id}, path={self.path})"