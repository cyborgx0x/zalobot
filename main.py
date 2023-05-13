import os
import requests
import pyautogui
import time
import math
from PIL import Image
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from pyautogui import locateAll
import re
from datetime import datetime
from html_gen import html_gen
import base64
from io import BytesIO

zalo_location = f"{os.environ['USERPROFILE']}/AppData/Local/Programs/Zalo/Zalo.exe"
os.system(zalo_location)
time.sleep(1)
pyautogui.hotkey('win', 'up')
time.sleep(1)
pyautogui.hotkey('alt', '1')
pyautogui.hotkey('alt', '2')

folder = f"images"+str(datetime.now().timestamp())
os.makedirs(folder, exist_ok=True)
time.sleep(1)
banbe = pyautogui.screenshot("count.png", region=(418,104, 160, 60))
f = {'file': open("count.png","rb")}
res = requests.post("https://detection.diopthe20.com/detect/", files=f)
print(res.text)
r = re.findall(r'\d+', res.text)
count  = int(r[0])

queue = []
for i in range(math.ceil(count/10)):
    queue.append(pyautogui.screenshot())
    pyautogui.moveTo(800,119)
    pyautogui.scroll(-1100)
    pyautogui.moveTo(20,20)
    time.sleep(0.1)
i = 0
crop_image_queue = []
for image in queue:

    # image = Image.open("bgf.png").convert('RGB') 
    open_cv_image = np.array(image) 
    open_cv_image = open_cv_image[:, :, ::-1].copy() 
    button = cv.imread('button.png')
    res = locateAll(button, open_cv_image)

    for box in res:
        if i == count:
            break
        if box.top > 1000:
            break
        y = box.top-30
        x = 420
        h = 80
        w = 450
        crop_img = open_cv_image[y:y+h, x:x+w]
        crop_image_queue.append(crop_img)
        i+=1

data = []
for index, img in enumerate(crop_image_queue):
    cv.imwrite(f'{folder}/{index}.png',img)
    data.append(f'{folder}/{index}.png')

html_gen(data=data)