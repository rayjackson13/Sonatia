import subprocess

def run_program(program_path: str, *args):
    """
    Runs a program at the specified path with optional arguments.
    """
    try:
        command = [program_path] + list(args)
        result = subprocess.run(command, check=True)
        print('result', result)
    except subprocess.CalledProcessError as e:
        print(f"Error running program:\n{e.stderr}")
    except FileNotFoundError:
        print(f"Program not found at path: {program_path}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")