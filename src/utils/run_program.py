import subprocess
import threading


def run_subprocess(command):
    """
    Function to execute a command using subprocess.run.
    """
    subprocess.run(command, check=True, shell=True)

def run_program(program_path: str, *args):
    """
    Runs a program at the specified path with optional arguments.
    """
    try:
        command = [program_path] + list(args)
        thread = threading.Thread(target=run_subprocess, args=(command,))
        thread.start()
    except subprocess.CalledProcessError as e:
        print(f"Error running program:\n{e.stderr}")
    except FileNotFoundError:
        print(f"Program not found at path: {program_path}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
