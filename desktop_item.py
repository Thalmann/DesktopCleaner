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
    size = None

    def __init__(self, file_, file_path):
        self.filename, self.file_extension = os.path.splitext(file_)
        self.file_path = file_path
        self.is_dir = os.path.isdir(file_path)
        self.is_file = os.path.isfile(file_path)
        self.last_modified_epoch = os.path.getmtime(file_path)
        self.last_modified_string = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(self.last_modified_epoch))
        self.size = os.path.getsize(self.file_path)

    def print_last_modified(self):
        print self.filename + self.file_extension + '\t' + "last modified: " + self.last_modified_string

    def delete(self):
        try:
            os.remove(di.file_path)
        except:
            shutil.rmtree(di.file_path) #takes care of if the folder is empty

    def start(self, program=None):
        if program is None:
            os.system("\"" + self.file_path + "\"") # quotes to account for filenames with whitespace
        else:
            try:
                subprocess.Popen([program, self.file_path])
            except:
                print program + " not found."
