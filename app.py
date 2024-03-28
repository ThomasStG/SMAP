"""Module imports required modules and starts app."""
import subprocess
import sys
import os
from server import startApp

if len(sys.argv) > 1:
    if sys.argv[1] == "i" or sys.argv[1] == "install" or sys.argv[1] == "get":

        # Get the path to the Python executable
        python_executable = sys.executable

        # Calculate the path to pip based on the Python executable path
        pip_path = os.path.join(os.path.dirname(python_executable), "pip")

        subprocess.run([
            pip_path, "install", "-r",
            "./static/documentation/requirements.txt"
        ],
                       check=True)
    else:
        for item in os.listdir('.'):
            if item.endswith("_test.py"):
                subprocess.run(["python3", item], check=True)
else:
    startApp()