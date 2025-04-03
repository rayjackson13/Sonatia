from db.folders import FolderDBController
from db.projects import ProjectDBController
from db.manager import DatabaseManager

def load_db():
    DatabaseManager.register_controller('folders', FolderDBController())
    DatabaseManager.register_controller('projects', ProjectDBController())