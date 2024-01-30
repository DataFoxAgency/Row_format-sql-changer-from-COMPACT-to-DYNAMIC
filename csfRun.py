import os
import subprocess

current_directory = os.getcwd()
script_path = os.path.join(current_directory, "change_sql_format.py")
subprocess.call(["python3", script_path])
