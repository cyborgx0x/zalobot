import pyautogui
import requests
banbe = pyautogui.screenshot("count.png",region=(418,104, 160, 60))

f = {'file': open("count.png","rb")}
res = requests.post("https://detection.diopthe20.com/detect/", files=f)
print(res.text)