import os
import datetime
import requests
import pyautogui
import time


zalo_location = f"{os.environ['USERPROFILE']}/AppData/Local/Programs/Zalo/Zalo.exe"
os.system(zalo_location)
time.sleep(3)
pyautogui.hotkey('win', 'up')
time.sleep(1)
pyautogui.hotkey('alt', '2')

folder = f"images"
os.makedirs(folder, exist_ok=True)
import re
i = 0

def auto_get(i, count, status):
    pyautogui.moveTo(100,100)
    locations = list(pyautogui.locateAllOnScreen('button.png'))
    print(locations)
    locations.pop(-1)
    locations.pop(-2)
    for location in locations:
        locationxy = pyautogui.center(location)
        # if locationxy.y > 920:
        #     break
        # pyautogui.click(*locationxy)
        j,k = locationxy
        region  = (420,k-30, 450, 80)
        pyautogui.screenshot(f'{folder}/{i}.png', region=region)
        # x, y = pyautogui.locateCenterOnScreen('xemthongtin.png')
        # pyautogui.move(-30, 40) 
        # pyautogui.click(x,y)
        # time.sleep(1)
        # pyautogui.screenshot(f'images/{i}.png',region=(785,207, 350, 630))
        # pyautogui.press('esc')
        i+=1
        if i == count:
            status = False
            break
    return i
time.sleep(2)
banbe = pyautogui.screenshot("count.png", region=(418,104, 160, 60))
f = {'file': open("count.png","rb")}
res = requests.post("https://detection.diopthe20.com/detect/", files=f)
print(res.text)
r = re.findall(r'\d+', res.text)
count  = int(r[0])
banbe = pyautogui.screenshot("count.png",region=(418,104, 160, 60))

import math
status = True 
while status:
    i = auto_get(i, count, status)
    pyautogui.moveTo(800,119)
    pyautogui.scroll(-700)
