from IMGFinder.IMGFinder import IMGFinder
import pyautogui
import time


def explora(par):
    pyautogui.click(par['position']["x"]+30, par['position']["y"]+20)

def primeiraImg(par):
    time.sleep(2)
    pyautogui.click(par['position']["x"]+35, par['position']["y"]+80)

def curte(par):
    pyautogui.click(par['position']["x"]+20, par['position']["y"]+15)

def proxima(par):
    pyautogui.click(par['position']["x"]+20, par['position']["y"]+19)


#Directory of your images
directoryImgs = '.\\Images\\'


img = IMGFinder(directoryImgs, globals())
img.run(True, ['curte.png', 'proxima.png'])






