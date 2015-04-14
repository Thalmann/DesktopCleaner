import win32con
import win32gui
import win32process
import subprocess
import time

def get_hwnds_for_pid (pid):
  def callback (hwnd, hwnds):
    if win32gui.IsWindowVisible (hwnd) and win32gui.IsWindowEnabled (hwnd):
      _, found_pid = win32process.GetWindowThreadProcessId (hwnd)
      if found_pid == pid:
        hwnds.append (hwnd)
    return True
    
  hwnds = []
  win32gui.EnumWindows (callback, hwnds)
  return hwnds

def move_window(filePath):
    app = subprocess.Popen("\"" + filePath + "\"", shell=True) # quotes to account for filenames with whitespace
    #
    # sleep to give the window time to appear
    #
    time.sleep (2.0)

    for hwnd in get_hwnds_for_pid(app.pid):
        print hwnd, "=>", win32gui.GetWindowText (hwnd)
        #win32gui.SendMessage (hwnd, win32con.WM_CLOSE, 0, 0)
        win32gui.MoveWindow(hwnd, 0, 0, 500, 500, True)
