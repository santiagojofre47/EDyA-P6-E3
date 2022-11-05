import numpy as np 

class GrafoSecuencial:
    __matrizAdyacencia = None
    __cantVertices =  None

    def __init__(self, cant_vertices = 3):
        self.__cantVertices = cant_vertices
        self.__matrizAdyacencia = np.zeros((self.__cantVertices,self.__cantVertices),dtype = int)
    
    def crearArista(self, v1, v2):
        if (v1 <= self.__cantVertices and v2 <= self.__cantVertices) and (v1 >= 1 and v2 >= 1):
            self.__matrizAdyacencia[v1-1][v2-1] = 1
            self.__matrizAdyacencia[v2-1][v1-1] = 1
        else:
            print('ERROR: Vertices no validos')
    def Adyacentes(self, v, matriz):
        list = []
        for j in range(self.__cantVertices):
            if matriz[v][j] == 1:
                list.append(j) 
        return list
    
   #Metodo recorrido en profundidad
    def REP(self, actual,arreglo = None, recorrido = None, iniciar = False):
        if not iniciar:
            if actual-1 >=0  and actual-1 < self.__cantVertices:
                arreglo = np.zeros(self.__cantVertices,dtype = int)
                recorrido = []
                recorrido = self.REP(actual = actual-1 , arreglo = arreglo,recorrido = recorrido, iniciar = True)
            else:
                print('ERROR: vertice  origen no valido')
                return None
        else:
            recorrido.append(actual+1)
            arreglo[actual] = 1
            adyacentes = self.Adyacentes(actual)
            for adyacente in adyacentes:
                if arreglo[adyacente] == 0:
                   recorrido =  self.REP(adyacente,arreglo = arreglo,recorrido = recorrido, iniciar = True)
         
        return recorrido

    
    def Warshall(self):
        P = self.__matrizAdyacencia
        for k in range(self.__cantVertices):
            for i in range(self.__cantVertices):
                for j in range(self.__cantVertices):
                    if P[i][j] == 1 or (P[i][k]*P[k][j]) == 1:
                        P[i][j] = 1
                    else:
                        P[i][j] = 0
        return P
 
    def Conexo(self, matriz, vertice):
        band = True
        i = 0
        while i < self.__cantVertices and band:
            if len(self.Adyacentes(i, matriz)) == 0 and i != vertice:
                band = False
            i+=1
        return band
    
 
    def getCantidadCriticos(self):
        count = 0
        for i in range(self.__cantVertices):
            arrAux = np.copy(self.__matrizAdyacencia)
            arrAux[i,:] = 0
            arrAux[:,i] = 0
            if not self.Conexo(arrAux,i):
               count+=1
        return count

            
