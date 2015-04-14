import os
import time
import archive
import extensions
import shutil
import desktop_item

def open_file_ui(di):
    if di.is_dir:
        di.start("explorer.exe")
    elif di.is_file:    
        if di.file_extension == "":
            print "File has no file extension."
            if di.size < 1000000:
                di.start("notepad.exe")
        elif di.file_extension in extensions.get_shortcut_extensions():
            print "This is a shortcut for: " + di.filename
        else:
            di.start()
    else:
        print "Error - not a file or folder." #error handling af hvis det ikke er en fil eller dir..
        

def is_dir_ui(di):
    if di.is_dir:
        return ", compress and archive(c)"
    else:
        return " "

desktop_path = "C:\Users\Bruno\Desktop"
archive.create_archive()

for item in os.listdir(desktop_path):
    di = desktop_item.DesktopItem(item, desktop_path)
    
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
            di.delete()
            print "file deleted"
        elif user_input == "a":
            # do archive stuff - maybe have some kind of archive structure
            archive.archive_file(di)
        elif user_input == "k":
            # do some keep stuff maybe
            print "kept"
        elif user_input == "q": # quit
            exit()
        else:
            print "kept"
            

print "Good work - your desktop is clean."

    

