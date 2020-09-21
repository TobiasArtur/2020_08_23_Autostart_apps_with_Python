import autoit
import time

autoit.run("C:\\Users\\Tobias_Artur\\AppData\\Local\\Obsidian\\Obsidian")
autoit.win_wait_active("Obsidian", 0)
obsidian = autoit.win_get_handle("Obsidian")
print(obsidian)
autoit.win_move_by_handle(obsidian, 1273, 0, 1300, 1087)
#time.sleep(3)
#autoit.win_close_by_handle(obsidian)

###############################################################################################

autoit.run("C:\\Program Files\\Mozilla Firefox\\firefox")
autoit.win_wait_active("Mozilla Firefox", 0)
firefox = autoit.win_get_handle("Mozilla Firefox")
print(firefox)
autoit.win_move_by_handle(firefox, -7, 0, 1287, 1087)
#time.sleep(3)
#autoit.win_close_by_handle(firefox)

###############################################################################################

autoit.run("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome")
#autoit.run('C:\\Program Files (x86)\\Chromium\\Application\\chrome')
# With chromium, you can get away just typing in "Google"
autoit.win_wait_active("ServiceNow - Google Chrome", 0)
chrome = autoit.win_get_handle("ServiceNow - Google Chrome")
print(chrome)
autoit.win_move_by_handle(chrome, 2560, 0, 1280, 1080)
#time.sleep(3)
#autoit.win_close_by_handle(chrome)

##############################################################################################

autoit.run("C:\\Program Files\\darktable\\bin\\darktable")
autoit.win_wait_active("darktable", 0)
darktable = autoit.win_get_handle("darktable")
print(darktable)
autoit.win_move_by_handle(darktable, 3840, 0, 5120, 540)
#time.sleep(3)
#autoit.win_close_by_handle(darktable)

###############################################################################################

autoit.run("C:\\Program Files (x86)\\Steam\\steam.exe")
autoit.win_wait_active("Steam", 0)
steam = autoit.win_get_handle("Steam")
print(steam)
autoit.win_move_by_handle(steam, 3840, 540, 1280, 1080)
#time.sleep(3)
#autoit.win_close_by_handle(steam)
