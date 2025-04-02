class FileModel:
    def __init__(self, file_id=None, name=None, path=None, updated_at=None):
        self.id = file_id
        self.name = name
        self.path = path
        self.updated_at = updated_at
    
    def __repr__(self):
        """Representation for debugging."""
        return f"FileModel(id={self.id}, name={self.name}, path={self.path}, updated_at={self.updated_at})"