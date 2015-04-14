import os
import time
import archive
import subprocess
import extensions
import shutil
import desktop_item

def open_file_ui(f, file_path):
    filename, file_extension = os.path.splitext(f)
    if os.path.isdir(file_path):
        subprocess.Popen(["explorer.exe", file_path])
    elif os.path.isfile(file_path):    
        if file_extension == "":
            print "File has no file extension."
            if os.path.getsize(file_path) < 1000000:
                subprocess.Popen(["notepad.exe", file_path])
        elif file_extension in extensions.get_shortcut_extensions():
            print "This is a shortcut for: " + filename
        else:
            os.system("\"" + file_path + "\"") # quotes to account for filenames with whitespace
    else:
        print "Error - not a file or folder." #error handling af hvis det ikke er en fil eller dir..
        

desktopPath = "C:\Users\Bruno\Desktop"
archive.create_archive()

for f in os.listdir(desktopPath):
    file_path = os.path.join(desktopPath, f)
    last_modified_epoch = os.path.getmtime(file_path)
    last_modified_string = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(last_modified_epoch))
   
    if last_modified_epoch < time.time()-(3*24*60*60*30): #All files older than 3 months
        # For testing the time
        # print str(time.time())
        # print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()-(24*60*60*30)))
        # print time.time()-(24*60*60*30)
        # print last_modified_epoch

        print "This file is older than 3 months: "
        print f + '\t' + "last modified: " + last_modified_string

        open_file_ui(f, file_path)

        
        print "Do you want to delete(d), archive(a) or keep(k) the file. Enter q to quit."
        user_input = raw_input()
        
        if user_input == "d":
            try:
                os.remove(file_path)
            except:
                shutil.rmtree(file_path) #takes care of if the folder is empty
            print "file deleted"
        elif user_input == "a":
            # do archive stuff - maybe have some kind of archive structure
            archive.archive_file(f, file_path)
        elif user_input == "k":
            # do some keep stuff maybe
            print "kept"
        elif user_input == "q": # quit
            exit()
        else:
            print "kept"
            

print "done deal"

    

