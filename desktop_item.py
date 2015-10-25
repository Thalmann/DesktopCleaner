import os
import time
import errno
import stat

#Stolen codesnippet :-b
def handleRemoveReadonly(func, path, exc):
        excvalue = exc[1]
        if func in (os.rmdir, os.remove) and excvalue.errno == errno.EACCES:
            os.chmod(path, stat.S_IRWXU| stat.S_IRWXG| stat.S_IRWXO) # 0777
            func(path)
        else:
            raise

class DesktopItem:
    "A class representing a desktop item, which can be a file or a folder."
    
    def __init__(self, item, desktop_path):
        self.filename, self.file_extension = os.path.splitext(item)
        self.desktop_path = desktop_path
        self.file_path = os.path.join(desktop_path, item)
        self.is_dir = os.path.isdir(self.file_path)
        self.is_file = os.path.isfile(self.file_path)
        self.last_modified_epoch = os.path.getmtime(self.file_path)
        self.last_modified_string = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(self.last_modified_epoch))
        self.size = os.path.getsize(self.file_path)

    def print_last_modified(self):
        print self.filename + self.file_extension + '\t' + "last modified: " + self.last_modified_string
    
    def delete(self):
        try:
            os.remove(self.file_path)
        except:
            import shutil
            shutil.rmtree(self.file_path, ignore_errors=False, onerror=handleRemoveReadonly) #takes care of if the folder is empty and if the item is readonly

    def start(self, program=None):
        if program is None:
            os.system("\"" + self.file_path + "\"") # quotes to account for filenames with whitespace
        else:
            try:
                import subprocess
                subprocess.Popen([program, self.file_path])
            except:
                print program + " not found."

    def zip_dir(self):
        if self.is_dir:
            import shutil
            shutil.make_archive(self.filename, "zip", self.file_path)
            self.delete()
            self.file_extension = ".zip"
            self.file_path = os.path.join(self.desktop_path, self.filename + self.file_extension)
            self.is_dir = False
            self.is_file = True
        else:
            print "Only possible to use directories for compression."
