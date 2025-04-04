from pathlib import Path
from datetime import datetime

from db.manager import DatabaseManager, DBNames
from db.folders import FolderModel
from db.projects import ProjectModel


def get_folders() -> list[FolderModel]:
    controller = DatabaseManager.get_controller(DBNames.Folders)
    return controller.fetch_all()


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
        folder_path=folder.path,
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

    controller = DatabaseManager.get_controller(DBNames.Projects)
    controller.insert_records(projects)
    controller.update_records(projects)

    folder_paths = [f'"{folder.path}"' for folder in folders]
    folder_paths_str = ','.join(folder_paths)
    return controller.fetch_all(f"folder_path in ({folder_paths_str})")
