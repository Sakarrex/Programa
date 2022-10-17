class Grafo(object):
    __relaciones = None

    def __init__(self):
        self.__relaciones = {}

    def __str__(self):
        return str(self.__relaciones)
 
    def agregar(self,elemento):
        if not(elemento in self.__relaciones):
            self.__relaciones.update({elemento:[]})

    def relacionar(self,elemento1, elemento2):
        if (elemento1 in self.__relaciones) and (elemento2 in self.__relaciones):
            self.relacionarUnilateral(elemento1, elemento2)
    
    def relacionarUnilateral(self,origen, destino):
        self.__relaciones[origen].append(destino)
    
    def getCantArcos(self):
        cant = 0
        for items in self.__relaciones.items():
            cant += len(items[1])
            
        return cant
    def getCantNodos(self):
        return len(self.__relaciones)
    
    
    def getDict(self):
        return self.__relaciones