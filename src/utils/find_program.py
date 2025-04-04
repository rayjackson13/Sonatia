import platform
import shutil
import os


def _get_program_path_windows(program_name: str) -> str | None:
    """
    Scans the Start Menu for shortcuts and retrieves their target executable paths.
    """
    import win32com.client

    start_menu_dirs = [
        r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs",
        os.path.expandvars(r"%AppData%\Microsoft\Windows\Start Menu\Programs"),
    ]

    shell = win32com.client.Dispatch("WScript.Shell")

    for start_menu_dir in start_menu_dirs:
        for root, _, files in os.walk(start_menu_dir):
            for file in files:
                if file.endswith(".lnk"):  # Look for shortcut files
                    shortcut_path = os.path.join(root, file)
                    try:
                        # Resolve the shortcut to its target path
                        shortcut = shell.CreateShortcut(shortcut_path)
                        target_path = shortcut.TargetPath

                        # Check if the target path matches the app name
                        if (
                            program_name.lower()
                            in os.path.basename(target_path).lower()
                        ):
                            return target_path
                    except Exception as e:
                        print(f"Error resolving shortcut {shortcut_path}: {e}")

    return None


def _get_program_path_unix(program_name: str) -> str | None:
    """
    Retrieves the path of a program using `shutil.which` on Unix-based systems.
    """
    return shutil.which(program_name)


def _get_program_path_mac(program_name: str) -> str | None:
    program_path = shutil.which(program_name)
    if program_path:
        return program_path

    # Search standard directories for .app bundles
    search_dirs = ["/Applications", os.path.expanduser("~/Applications")]

    for directory in search_dirs:
        if os.path.exists(directory):  # Ensure the directory exists
            for app in os.listdir(directory):
                if app.lower().startswith("ableton") and app.endswith(".app"):
                    return os.path.join(directory, app)

    return None


def get_program_path(program_name: str) -> str | None:
    """
    Determines the operating system and retrieves the path of a program.
    """
    system = platform.system()

    if system == "Windows":
        return _get_program_path_windows(program_name)
    elif system == "Darwin":
        return _get_program_path_mac(program_name)
    elif system == "Linux":
        return _get_program_path_unix(program_name)
    else:
        print(f"Unsupported operating system: {system}")
        return None
