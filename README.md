# DesktopCleaner
Clean your desktop for the Windows operating system.

#### What you need:
* Python 2.7 installed

#### How to run DesktopCleaner:
* Clone this repo or download the zip
* Open the "settings.dc"-file in your favourite text-editor and input your desktop path, where you want your files to get archived and how old files should be to be added to the list of files
* Run DesktopCleaner.py with python, eg: in the copmmand line input: "python DesktopCleaner.py". (requires python in PATH)

#### The settings.dc file
The file looks like this when you download it:

desktop_path some_path
archive_path some_path
clean_desktop_time_in_days some_time_in_days

Example:

desktop_path C:\Users\Username\Desktop
archive_path C:\desktopArchive
clean_desktop_time_in_days 30
