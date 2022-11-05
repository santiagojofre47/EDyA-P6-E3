from claseGrafoSecuencial import GrafoSecuencial

if __name__ == '__main__':
    obj = GrafoSecuencial(5)
    obj.crearArista(1, 2)
    obj.crearArista(1, 3) 
    obj.crearArista(2, 4)
    obj.crearArista(2, 5)   
    print('Cantidad de sitios criticos: {}'.format(obj.getCantidadCriticos()))
    