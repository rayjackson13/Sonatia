from pathlib import Path
from datetime import datetime

from db.projects import ProjectDBController, ProjectModel
from store.settings import SettingsStore, FolderModel


def get_folders() -> list[FolderModel]:
    return SettingsStore().get_folders()


def get_project_data(file_path: str, folder: FolderModel) -> ProjectModel | None:
    path = Path(file_path)

    if not path.exists() or not path.is_file():
        return None

    name = path.name
    timestamp = path.stat().st_mtime
    updated_at = datetime.fromtimestamp(timestamp)

    return ProjectModel(
        file_id=None,
        path=file_path,
        name=name,
        folder_id=folder.id,
        updated_at=updated_at,
    )


def get_files_in_folder(folder: FolderModel):
    return [
        get_project_data(str(file), folder)
        for file in Path(folder.path).rglob("*.als")
        if "Backup" not in file.parts and not file.name.startswith(".")
    ]


def index_files() -> list[ProjectModel]:
    projects: list[ProjectModel] = []
    folders = get_folders()

    for folder in folders:
        projects.extend(get_files_in_folder(folder))

    controller = ProjectDBController()
    controller.insert_records(projects)

    return controller.fetch_all()
