import os
import datetime
from detect import get_text
zalo_location = f"{os.environ['USERPROFILE']}/AppData/Local/Programs/Zalo/Zalo.exe"
os.system(zalo_location)
import time
time.sleep(3)
import pyautogui
pyautogui.hotkey('win', 'up')
time.sleep(1)
pyautogui.hotkey('alt', '2')
import os

folder = f"images"
os.makedirs(folder, exist_ok=True)
import re
i = 0

def auto_get(i):
    pyautogui.moveTo(100,100)
    locations = list(pyautogui.locateAllOnScreen('button.png'))
    print(locations)
    locations.pop(-1)
    locations.pop(-2)
    for location in locations:
        locationxy = pyautogui.center(location)
        if locationxy.y > 920:
            break
        # pyautogui.click(*locationxy)
        j,k = locationxy
        region  = (420,k+40, 350, 80)
        pyautogui.screenshot(f'{folder}/{i}.png', region=region)
        # x, y = pyautogui.locateCenterOnScreen('xemthongtin.png')
        # pyautogui.move(-30, 40) 
        # pyautogui.click(x,y)
        # time.sleep(1)
        # pyautogui.screenshot(f'images/{i}.png',region=(785,207, 350, 630))
        # pyautogui.press('esc')
        i+=1
    return i

banbe = pyautogui.screenshot(region=(416,103, 160, 60))
banbe_count = get_text(banbe)
print(banbe_count)
r = re.findall(r'\d+', banbe_count)
count  = int(r[0])
import math
for n in range(math.ceil(count/10)):
    i = auto_get(i)
    pyautogui.moveTo(800,119)
    pyautogui.scroll(-1000)
