from .config import ConfigHandler
from .find_program import get_program_path
from .run_program import run_program


class ProgramHandler:
    @staticmethod
    def initialize():
        path = get_program_path("ableton")
        if path:
            ConfigHandler.save_to_config("Settings", "program_path", path)
            
    @staticmethod
    def run_program():
        path = ConfigHandler.read_from_config("Settings", "program_path")
        if path:
            run_program(path)
        else:
            print("No program path found.")
