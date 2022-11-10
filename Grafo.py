import numpy as np
class Grafo(object):
    __matrizAdyacencia = None
    __cantVertices = None

    def __init__(self,tamanio):
        self.__matrizAdyacencia = np.zeros((tamanio,tamanio),dtype=int)
        self.__cantVertices = tamanio
 
    def CrearArco(self,vertice1,vertice2):
        if vertice1 >= self.__cantVertices or vertice1 < 0 or vertice2 >= self.__cantVertices or vertice2 < 0:
            print("Vertices no existente")
        else:
            self.__matrizAdyacencia[vertice1,vertice2] = 1
    
    def getCantArcos(self):
        cant = 0

        for i in range(self.__cantVertices):
            for j in range(self.__cantVertices):
                if self.__matrizAdyacencia[i][j] == 1:
                    cant += 1
            
        return cant

    def getCantNodos(self):
        return self.__cantVertices
    
    def getMatriz(self):
        return self.__matrizAdyacencia
    