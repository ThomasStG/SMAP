"""Module imports required modules and starts app."""
import subprocess
import sys
import os


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
    elif sys.argv[1].lower() == "debug":
        from server import startApp
        startApp(1)
    else:
        for item in os.listdir('.'):
            from server import startApp
            if item.endswith("_test.py"):
                subprocess.run(["python3", item], check=True)
else:
    from server import startApp
    startApp(0)
