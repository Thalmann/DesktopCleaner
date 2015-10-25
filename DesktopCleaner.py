import os
import time
import archive
import extensions
import shutil
import desktop_item
import kept_items_handler

def open_file_dialog(di):
    print 'Do you want to open {0}? (y/n)'.format(di.filename)
    while True:
        answer = raw_input()
        if answer is 'y':
            return True
        elif answer is 'n':
            return False
        print 'Pls input y for yes or n for no!'

def open_file_ui(di):
    if di.is_dir:
        if open_dialog(di):
            di.start("explorer.exe")
    elif di.is_file:    
        if di.file_extension == "":
            print "File has no file extension."
            if di.size < 1000000:
                if open_dialog(di):
                    di.start("notepad.exe")
        elif di.file_extension in extensions.get_shortcut_extensions():
            print "This is a shortcut for: " + di.filename
        else:
            if open_dialog(di):
                di.start()
    else:
        print "Error - not a file or folder." #error handling af hvis det ikke er en fil eller dir..
        

def is_dir_ui(di):
    if di.is_dir:
        return ", compress and archive(c)"
    else:
        return " "

    
kept_items_handler = kept_items_handler.KeptItemsHandler()

#LOAD PATHS from file paths.dc
with open("settings.dc", "r") as f:
    try:
        desktop_path = f.readline().split(" ")[1].replace("\n","")
        archive_path = f.readline().split(" ")[1].replace("\n","")
        clean_desktop_time_days = int(f.readline().split(" ")[1].replace("\n",""))
    except Exception:
        print "Please set paths and the time for how long items are allowed on the desktop in the settings.dc file."
        exit(0)

def is_path_valid(path, error_msg='Path is invalid.'):
    if(not os.path.isdir(path) or not os.path.exists(path)):
        print error_msg
        exit(0)

is_path_valid(desktop_path, error_msg='The given desktop path is invalid.')
is_path_valid(archive_path, error_msg='The given archive path is invalid.')


archive.create_archive(archive_path)

#while(True): issue #1
for item in os.listdir(desktop_path):
    di = desktop_item.DesktopItem(item, desktop_path)
    if kept_items_handler.contains(di):
        continue
    
    if di.last_modified_epoch < time.time()-(clean_desktop_time_days*24*60*60): #All files older than 3 months
        # For testing the time
        # print str(time.time())
        # print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()-(24*60*60*30)))
        # print time.time()-(24*60*60*30)
        # print last_modified_epoch

        print "This file is older than: " + time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(time.time()-(clean_desktop_time_days*24*60*60)))
        di.print_last_modified()

        open_file_ui(di)

        
        print "Do you want to delete(d), archive(a)" + is_dir_ui(di) + "or keep(k) the file. Enter q to quit."

        while True:
            user_input = raw_input()

            if user_input == "d":
                di.delete()
                print "file deleted"
                break
            elif user_input == "a":
                archive.archive_item(di)
                break
            elif user_input == "k":
                kept_items_handler.add_item(di)
                print "kept"
                break
            elif user_input == "q":
                kept_items_handler.save_kept_items()
                exit()
            elif di.is_dir and user_input == "c":
                di.zip_dir()
                archive.archive_item(di)
                break
            else:
                print "Please choose one of the options specified."    


kept_items_handler.save_kept_items()
print "Good work - your desktop is clean."

    

