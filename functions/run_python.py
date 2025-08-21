import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    if not abs_file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    try:
        result = subprocess.run(["python3", file_path] + args, cwd=working_directory, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=30)
        output = f'STDOUT: {result.stdout}\nSTDERR: {result.stderr}'
        if result.returncode != 0:
            return f'{output}\nProcess exited with code {result.returncode}'
        if not result.stdout and not result.stderr:
            return f'No output produced.'
        return output
    except Exception as e:
        return f"Error: executing Python file: {e}"
