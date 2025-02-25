from setuptools import setup
import warnings


warnings.simplefilter("ignore", SyntaxWarning)

APP = ["main.py"]

DATA_FILES = []
OPTIONS = {
    "argv_emulation": True, # hide terminal
    "packages": ["wx", "OpenGL"],
    "iconfile": "icon.icns" # custom icon
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={"py2app": OPTIONS},
    install_requires=["py2app"],
)