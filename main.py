from Grafo import Grafo
from Reconecedor import Reconocerdor

if __name__ == '__main__':
    Grafo1 = Grafo(3)
    Grafo2 = Grafo(3)

    Grafo1.CrearArco(0,1)
    Grafo1.CrearArco(0,2)


    Grafo2.CrearArco(1,0)
    Grafo2.CrearArco(1,2)


    Reconocedor = Reconocerdor(Grafo1,Grafo2)
    
