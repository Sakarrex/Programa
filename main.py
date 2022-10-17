from Grafo import Grafo
from Reconecedor import Reconocerdor

if __name__ == '__main__':
    Grafo1 = Grafo()
    Grafo2 = Grafo()
    Grafo1.agregar(1)
    Grafo1.agregar(2)
    Grafo1.agregar(3)
    Grafo1.relacionar(1,1)
    Grafo1.relacionar(1,2)
    Grafo1.relacionar(2,3)
    Grafo1.relacionar(3,1)
    Grafo2.agregar(4)
    Grafo2.agregar(5)
    Grafo2.agregar(6)
    Grafo2.relacionar(4,4)
    Grafo2.relacionar(4,5)
    Grafo2.relacionar(5,6)
    Grafo2.relacionar(6,4)
    Reconocedor = Reconocerdor(Grafo1,Grafo2)
    
