from IMGFinder.IMGFinder import IMGFinder
import pyautogui
import time


def discoLocal(par):
    time.sleep(0.5)
    pyautogui.hotkey('win', 'r')
    time.sleep(0.5)
    pyautogui.typewrite("notepad")
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(0.5)
    pyautogui.typewrite("FUNCIONOU")

def cursos(par):
    print("hahahahahh")

def conexao(par):
    print('Problema com tamanho de array')

def compartilhar(par):
    print("Passou por aqui também")


#Directory of your images
directoryImgs = '.\\Images\\'


img = IMGFinder(directoryImgs, globals())
img.run()






