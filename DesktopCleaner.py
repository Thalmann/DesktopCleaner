import os
import time
import archive
import subprocess
import extensions
import shutil
import desktop_item

def open_file_ui(di):
    if di.is_dir:
        subprocess.Popen(["explorer.exe", di.file_path])
    elif di.is_file:    
        if di.file_extension == "":
            print "File has no file extension."
            if os.path.getsize(di.file_path) < 1000000:
                subprocess.Popen(["notepad.exe", di.file_path])
        elif di.file_extension in extensions.get_shortcut_extensions():
            print "This is a shortcut for: " + di.filename
        else:
            os.system("\"" + di.file_path + "\"") # quotes to account for filenames with whitespace
    else:
        print "Error - not a file or folder." #error handling af hvis det ikke er en fil eller dir..
        

desktopPath = "C:\Users\Bruno\Desktop"
archive.create_archive()

for i in os.listdir(desktopPath):
    di = desktop_item.DesktopItem(i, os.path.join(desktopPath, i))
    
    if di.last_modified_epoch < time.time()-(3*24*60*60*30): #All files older than 3 months
        # For testing the time
        # print str(time.time())
        # print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()-(24*60*60*30)))
        # print time.time()-(24*60*60*30)
        # print last_modified_epoch

        print "This file is older than 3 months: "
        di.print_last_modified()

        open_file_ui(di)

        
        print "Do you want to delete(d), archive(a) or keep(k) the file. Enter q to quit."
        user_input = raw_input()
        
        if user_input == "d":
            try:
                os.remove(di.file_path)
            except:
                shutil.rmtree(di.file_path) #takes care of if the folder is empty
            print "file deleted"
        elif user_input == "a":
            # do archive stuff - maybe have some kind of archive structure
            archive.archive_file(di.filename+di.file_extension, di.file_path)
        elif user_input == "k":
            # do some keep stuff maybe
            print "kept"
        elif user_input == "q": # quit
            exit()
        else:
            print "kept"
            

print "done deal"

    

