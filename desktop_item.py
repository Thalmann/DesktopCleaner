import os
import time

class DesktopItem:
    "A class representing a desktop item, which can be a file or a folder."

    filename = None
    file_path = None
    file_extension = None
    is_dir = False
    is_file = False
    last_modified_epoch = None
    last_modified_string = None

    def __init__(self, file_, file_path):
        self.filename, self.file_extension = os.path.splitext(file_)
        self.file_path = file_path
        is_dir = os.path.isdir(file_path)
        is_file = os.path.isfile(file_path)
        last_modified_epoch = os.path.getmtime(file_path)
        last_modified_string = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(last_modified_epoch))
