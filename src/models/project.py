class ProjectModel:
    def __init__(
        self,
        file_id=None,
        filename=None,
        path=None,
        folder_path=None,
        title=None,
        updated_at=None,
    ):
        self.id = file_id
        self.filename = filename
        self.path = path
        self.folder_path = folder_path
        self.title = title
        self.updated_at = updated_at

    def __repr__(self):
        """Representation for debugging."""
        return (
            f"ProjectModel(id={self.id}, filename={self.filename}, path={self.path}, "
            + f"folder_path={self.folder_path}, title={self.title}, updated_at={self.updated_at})"
        )
