import os
import sys

def resource_path(relative_path):
    """
    Return absolute path to resource, works for dev and PyInstaller.
    """
    try:
        # Se eseguito da PyInstaller
        base_path = sys._MEIPASS
    except Exception:
        # Se eseguito come script Python
        # base_path = cartella principale dove c'è run.py
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    return os.path.join(base_path, relative_path)
