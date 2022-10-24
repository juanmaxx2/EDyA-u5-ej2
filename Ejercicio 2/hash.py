import numpy as np
import random
import math

class Hash:
    __tam = None
    __arre = None
   
    def primo(self,num):
        band = False
        while not band:
            band = True
            i = 2
            while i < num and band:
                if num % i == 0:
                    band = False
                i+=1
            num += 1
        return num-1
   
    def __init__(self, tam):
        tam = self.primo(math.floor(tam/0.70))
        self.__tam = tam
        self.__arre = np.zeros(tam, dtype = int)
        self.__random = random.randint(1,self.__tam-1)

    def lleno(self):
        return range(self.__arre) != self.__tam

    def insertar(self, clave):
        if self.lleno:
            indice = clave % self.__tam
            if self.__arre[indice] == 0:
                self.__arre[indice] = clave
            else:
                band = False
                while not band:
                    if self.__arre[indice] == 0:
                        band = True
                    else:
                        indice = (indice+self.__random)%self.__tam
                self.__arre[indice] = clave

    def buscar(self, clave):
        indice = clave % self.__tam
        if self.__arre[indice] == clave:
            return self.__arre[indice]
        else:
            i = 0
            band = False
            while not band:
                if self.__arre[indice] == clave or i == self.__tam:
                    band = True
                else:
                    indice = (indice+self.__random)%self.__tam
                    i += 1
            if band:
                return self.__arre[indice]
            else: return "\nEl elemento no se encontro"