import os
import shutil
import extensions

archivePath = "D:\desktopArchive"

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

def create_archive():
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

def archive_file(f, filePath):
    fileExtension = os.path.splitext(f)[1]

    if os.path.isdir(filePath):
        print "folders"
        move_file(filePath, textfiles)
    elif os.path.isfile(filePath):
        if fileExtension in extensions.get_textfile_extensions():
            print "textfile"
            move_file(filePath, textfiles)
        elif fileExtension in extensions.get_picture_extensions():
            print "picture"
            move_file(filePath, pictures)
        elif fileExtension in extensions.get_shortcut_extensions():
            print "shortcut"
            move_file(filePath, shortcuts)
        elif fileExtension in extensions.get_video_extensions():
            print "video"
            move_file(filePath, videofiles)
        elif fileExtension in extensions.get_music_extensions():
            print "music"
            move_file(filePath, musicfiles)
        elif fileExtension in extensions.get_system_extensions():
            print "system"
            move_file(filePath, systemfiles)
        else:
            print "fileformat no found - moved to other"
            move_file(filePath, other)
    else:
        print "Error - not a file or folder." #error handling af hvis det ikke er en fil eller dir..
        
    print "archived"
