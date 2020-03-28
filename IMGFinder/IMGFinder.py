import os
import pyautogui
import cv2
import numpy as np
import subprocess
import time
import sys
import inspect
import warnings


class IMGFinder:

    def __init__(self, path, functions=object):
        """

        :type functions: object
        """

        self.path = path
        self.imgs = os.listdir(self.path)

        
        myFuctions = dict()

        for key in list(self.imgs):
            myFuctions[key[:key.index('.')]] = ""

        for key in list(functions):
            if key[0:2] != "__" and "<function" in str(functions[key]):
                myFuctions[key] = functions[key]
        self.functions = myFuctions

    def monitorscreen(self, img):

        # Chama a funcão de comparação de imagem e verifica se foi encontra ou não
        # Caso pos[0] seja = -1 siginifica que a imagem não foi encontrada
        # Realiza chamada de função pelo nome da imagem desejada

        if img[-5:] != '_.png':
            pos = self.printscreen(self.path+img)
            if pos[0] != -1:
                print(img + " - econtrada na  posicao: ", pos[0], pos[1])
                func = img.replace('.png', '')
                
                if "<function" in str(self.functions[func]):
                    func = self.functions[func](img)
                else:
                    warnings.warn(f"Function '{func}' not declared")

                self.imgs.remove(img)
            else:
                print(img+" - nao encontrada na tela")

    @staticmethod
    def printscreen(image, precision=0.8):

        # Método que compara imagem passada por parametro com a tela
        # tira um print da tela e compara com a imagem passada por parametro

        im = pyautogui.screenshot()
        # im.save('testarea.bmp') useful for debugging purposes, this will save the captured region as "testarea.bmp"
        img_rgb = np.array(im)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        template = cv2.imread(image, 0)
        template.shape[::-1]

        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        if max_val < precision:
            return [-1, -1]
        return max_loc

    def run(self):
        # Loop que busca a pasta de imagens e chama a função avaliaTela para verificar se encontrou a imagem
        # na tela

        stop = False
        while not stop:
            if len(self.imgs) == 0:
                stop = True
            for img in self.imgs:
                if img[-4:] == '.png':
                    self.monitorscreen(img)
            time.sleep(2)
        
        return print("Finish")
