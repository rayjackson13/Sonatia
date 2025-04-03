from .controller import AbstractDBController

class DatabaseManager:
    _controllers: dict[str, AbstractDBController] = {}

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
