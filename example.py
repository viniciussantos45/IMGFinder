from IMGFinder.IMGFinder import IMGFinder
import pyautogui
import time


def achou(par):
    time.sleep(0.5)
    pyautogui.hotkey('win', 'r')
    time.sleep(0.5)
    pyautogui.typewrite("notepad")
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(0.5)
    pyautogui.typewrite("FUNCIONOU")


#Directory of your images
directoryImgs = 'C:\\Your\\Path\\Images\\'


img = IMGFinder(directoryImgs, globals())
img.run()






