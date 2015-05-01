import os
import shutil
import extensions

archivePath = ""

# Archive folder names:
pictures = "pictures"
textfiles = "textfiles"
shortcuts = "shortcuts"
videofiles = "videofiles"
musicfiles = "musicfiles"
systemfiles = "systemfiles"
other = "other"
folders = "folders"

def create_dir(name):
    if not os.path.exists(name):
        os.mkdir(name)

def create_archive(archivePath):
    archivePath = archivePath
    create_dir(archivePath)    
    os.chdir(archivePath)
    
    create_dir(pictures)
    create_dir(textfiles)
    create_dir(shortcuts)
    create_dir(videofiles)
    create_dir(musicfiles)
    create_dir(systemfiles)
    create_dir(other)
    create_dir(folders)

def move_file(srcFilePath, dstDir):
    shutil.move(srcFilePath, os.path.join(os.getcwd(),dstDir))

def archive_item(di): #Where di is a custom type - DesktopItem

    if di.is_dir:
        print "folders"
        move_file(di.file_path, textfiles)
    elif os.path.isfile(di.file_path):
        if di.file_extension in extensions.get_textfile_extensions():
            print "textfile"
            move_file(di.file_path, textfiles)
        elif di.file_extension in extensions.get_picture_extensions():
            print "picture"
            move_file(di.file_path, pictures)
        elif di.file_extension in extensions.get_shortcut_extensions():
            print "shortcut"
            move_file(di.file_path, shortcuts)
        elif di.file_extension in extensions.get_video_extensions():
            print "video"
            move_file(di.file_path, videofiles)
        elif di.file_extension in extensions.get_music_extensions():
            print "music"
            move_file(di.file_path, musicfiles)
        elif di.file_extension in extensions.get_system_extensions():
            print "system"
            move_file(di.file_path, systemfiles)
        else:
            print "fileformat no found - moved to other"
            move_file(di.file_path, other)
    else:
        print "Error - not a file or folder." #error handling af hvis det ikke er en fil eller dir..
        
    print "archived"
