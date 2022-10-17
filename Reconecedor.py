from Grafo import Grafo
import numpy as np
class Reconocerdor:
    __grafo1 = None
    __grafo2 = None
    __matriz1 = None
    __matriz2 = None
    __cantVertices = None
    
    

    def __init__(self,grafo1,grafo2) -> None:
        self.__grafo1 = grafo1
        self.__grafo2 = grafo2
        self.__cantVertices = grafo1.getCantNodos()
        if self.__grafo1.getCantNodos() == self.__grafo2.getCantNodos() and self.__grafo1.getCantArcos() == self.__grafo2.getCantArcos():
            self.__matriz1 = self.generarMatrices(grafo1)
            self.__matriz2 = self.generarMatrices(grafo2)
            arregloSoluciones = -1*(np.ones(self.__cantVertices,dtype=int))
            
            print("CantVertices: "+str(self.__cantVertices))
            exito = self.Isomorfismo(0,arregloSoluciones,False)
            if exito:
                print("Grafos isomorfos")
            else:
                print("Grafos no isomorfos")
           
        else:
            print("Grafos Distintos")

   
    
    def generarMatrices(self,grafo):
        matriz = np.zeros((self.__cantVertices,self.__cantVertices),dtype=int)
        values = list(grafo.getDict().values())
        keys = list(grafo.getDict().keys())
        for i in range(len(values)):
            for j in range(len(values[i])):
                k = 0
                while values[i][j] != keys[k]:
                    k+=1
                matriz[i][k] = 1
        return matriz
    
    def Isomorfismo(self,posactual,arregloSoluciones,exito):
        vertice = 0
        while vertice < self.__cantVertices and not exito:
            arregloSoluciones[posactual] =  vertice
            vertice += 1
            if self.Validar(posactual,arregloSoluciones):
                if posactual < self.__cantVertices-1:  
                    return self.Isomorfismo(posactual+1,arregloSoluciones,exito)
                elif posactual == self.__cantVertices-1:
                    exito = True
                    print("Entro aca")
        return exito

    def Validar(self,posactual,ArregloSoluciones):
        resultado = True
        "print(ArregloSoluciones)"
        for i in range(posactual-1):
            if ArregloSoluciones[i] == ArregloSoluciones[posactual]:
                resultado = False
            
        
                
        if self.CantAristasVertice(self.__matriz1,posactual) != self.CantAristasVertice(self.__matriz2,ArregloSoluciones[posactual]):
            resultado = False
        for j in range(posactual):
            if (self.__matriz1[j][posactual] != self.__matriz2[ArregloSoluciones[j]][ArregloSoluciones[posactual]]) or (self.__matriz1[posactual][j] != self.__matriz2[ArregloSoluciones[posactual]][ArregloSoluciones[j]]):
                resultado = False
        "print(resultado)"
        return resultado
            
        
    def CantAristasVertice(self,matriz,posactual):
        cantAristas = 0
        for i in range(self.__cantVertices):
            if matriz[posactual][i] == 1:
                cantAristas += 1
            if matriz[i][posactual] == 1:
                cantAristas +=1
        return cantAristas