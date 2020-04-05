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
    print('Achou a imagem conexão, escreva mais código para explorar do meu poder')

def compartilhar(par):
    print('Achou a imagem compartilhar, escreva mais código para explorar do meu poder')


#Directory of your images
directoryImgs = '.\\Images\\'


img = IMGFinder(directoryImgs, globals())
img.run()






