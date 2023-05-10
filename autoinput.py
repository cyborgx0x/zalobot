import pyautogui

import os
import time
os.system(f"{os.environ['USERPROFILE']}/AppData/Local/Programs/Zalo/Zalo.exe")
time.sleep(5)
pyautogui.typewrite("0852134401")
pyautogui.press("tab")
pyautogui.typewrite("Admin@123")
pyautogui.press("tab")

captcha = pyautogui.prompt('Input Captcha')
print(captcha)
pyautogui.typewrite(captcha)
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(5)