import numpy as np
n = 3
arreglo = np.empty(n,dtype=int)
exito = False


def recursivo(posactual):
    vertice = 0
    
    while vertice < n:
      
        print(arreglo) 
        arreglo[posactual] =  vertice
        vertice += 1
        
    
        if posactual < n-1:  
            recursivo(posactual+1)

        


recursivo(0)