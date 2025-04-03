class ProjectModel:
    def __init__(
        self, file_id=None, name=None, path=None, folder_id=None, updated_at=None
    ):
        self.id = file_id
        self.name = name
        self.path = path
        self.folder_id = folder_id
        self.updated_at = updated_at

    def __repr__(self):
        """Representation for debugging."""
        return f"ProjectModel(id={self.id}, name={self.name}, path={self.path}, folder_id={self.folder_id}, updated_at={self.updated_at})"
