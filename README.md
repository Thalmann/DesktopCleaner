# DesktopCleaner
Clean your desktop for the Windows operating system.

#### What you need:
* Python 2.7 installed

#### How to run DesktopCleaner:
1. Clone this repo or download the zip
2. Open the "settings.dc"-file in your favourite text-editor
  1. Insert your desktop path
  2. Insert where you want your files to be archived
  3. Insert how old files should be to be added to the list of files
3. Run DesktopCleaner.py with python, eg: in the copmmand line input: "python DesktopCleaner.py". (requires python in PATH)

#### The settings.dc file
##### The file looks like this when you download it:
<pre>
desktop_path <b>some_path</b>
archive_path <b>some_path</b>
clean_desktop_time_in_days <b>some_time_in_days</b>
</pre>

##### Example:
<pre>
desktop_path <b>C:\Users\Username\Desktop</b>
archive_path <b>C:\desktopArchive</b>
clean_desktop_time_in_days <b>30</b>
</pre>
