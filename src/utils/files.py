from pathlib import Path
from datetime import datetime

from db.files import FileDBController, FileModel

FOLDERS = [r"D:\Music", r"C:\Users\rayja\Documents\Music"]


def get_file_paths() -> list[str]:
    all_paths = []

    for folder_path in FOLDERS:
        folder = Path(folder_path)

        all_paths.extend(
            [
                file
                for file in folder.rglob("*.als")
                if "Backup" not in file.parts and not file.name.startswith(".")
            ]
        )

    return all_paths


def get_file_data(file_path: str) -> FileModel | None:
    path = Path(file_path)

    if not path.exists() or not path.is_file():
        return None

    name = path.name
    timestamp = path.stat().st_mtime
    updated_at = datetime.fromtimestamp(timestamp)

    return FileModel(file_id=None, path=file_path, name=name, updated_at=updated_at)


def get_files_in_folder(folder_path: str) -> list[FileModel]:
    file_paths = get_file_paths(folder_path)
    files: list[FileModel] = []
    for path in file_paths:
        files.append(get_file_data(path))

    for file in files:
        print(file)

    return files


def index_files() -> list[FileModel]:
    file_paths = get_file_paths()
    files: list[FileModel] = []
    for path in file_paths:
        files.append(get_file_data(path))

    for file in files:
        print(file)

    return files
