import os
import platform
from PySide6.QtWidgets import QFileDialog

from .config import ConfigHandler
from .find_program import get_program_path
from .run_program import run_program


class ProgramHandler:
    @staticmethod
    def initialize() -> None:
        registered_path = ProgramHandler.get_path()
        if registered_path:
            return
        path = get_program_path("ableton")
        if path:
            ConfigHandler.save_to_config("Settings", "program_path", path)
            
    @staticmethod
    def run_program() -> None:
        path = ProgramHandler.get_path()
        if path:
            run_program(path)
        else:
            print("No program path found.")
            
    @staticmethod
    def get_path() -> str | None:
        return ConfigHandler.read_from_config("Settings", "program_path")
    
    @staticmethod
    def set_path(path: str) -> None:
        ConfigHandler.save_to_config("Settings", "program_path", path)
        
    @staticmethod
    def choose_program_path() -> str | None:
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        
        system = platform.system()
        if system == "Windows":
            # Restrict to .exe files on Windows
            file_dialog.setNameFilter("Executable Files (*.exe)")
        elif system == "Darwin":  # macOS
            # Restrict to .app bundles on macOS
            file_dialog.setNameFilter("Application Bundles (*.app)")
        elif system == "Linux":
            # Allow all files on Linux
            file_dialog.setNameFilter("Executable Files (*)")
            
        if file_dialog.exec():
            selected_file = file_dialog.selectedFiles()[0]
            if system == "Linux" and not os.access(selected_file, os.X_OK):
                print("Selected file is not executable.")
                return
            ProgramHandler.set_path(selected_file)
                
        
