from .controller import AbstractDBController
from .folders import FolderDBController
from .projects import ProjectDBController


class DBNames:
    Folders = "folders"
    Projects = "projects"


class DatabaseManager:
    _controllers: dict[str, AbstractDBController] = {}

    @staticmethod
    def initialize() -> None:
        DatabaseManager.register_controller(DBNames.Folders, FolderDBController())
        DatabaseManager.register_controller(DBNames.Projects, ProjectDBController())

    @staticmethod
    def register_controller(name: str, instance: AbstractDBController) -> None:
        """Register a controller instance with the manager."""
        if name not in DatabaseManager._controllers:
            DatabaseManager._controllers[name] = instance

    @staticmethod
    def get_controller(name: str) -> AbstractDBController:
        """Retrieve the controller instance by name."""
        return DatabaseManager._controllers.get(name, None)

    @staticmethod
    def close_all_connections():
        """Close connections for all registered controllers."""
        for controller in DatabaseManager._controllers.values():
            controller.close_connection()
        DatabaseManager._controllers.clear()  # Clear the manager
