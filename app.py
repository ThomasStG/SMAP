"""Module imports required modules and starts app."""
import subprocess
import sys
from server import startApp

if len(sys.argv) > 1:
    subprocess.run(["pip", "install", "-r", "./static/documentation/requirements.txt"], check=True)
startApp()
# LF (\n) (EOF)