import os
import datetime

def get_desktop_name():
    desktop_path = r"~\Desktop"
    return os.path.expanduser(desktop_path)

def go_to_desktop(path):
    os.chdir(path)
