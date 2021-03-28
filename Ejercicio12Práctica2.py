

def generarLista(estructura):
    """ Genera una nueva lista de enteros a partir de la lista de strings. """
    lista = []
    for elem in estructura:
        fila = []
        for car in elem:
            x = 0 if car == '-' else -1
            fila.append(x)
        lista.append(fila)
    return lista

def devolverRango(sublista, x):
    """ Retorna una lista que contiene el rango de índices a recorrer. """
    rango = [0, 0]
    rango[0] = x - 1 if x > 0 else x
    rango[1] = x + 1 if x < len (sublista) - 1 else x
    return rango


def generarCadena(lista, i, j):
    """ Genera una cadena que contiene los valores de todas las celdas que entran en 
    contacto con la celda ubicada en [i][j]. """
    rangoi = devolverRango(lista, i)
    rangoj = devolverRango(lista[i], j)
    cad = ''
    for x in range(rangoi[0], rangoi[1] + 1):
        for y in range(rangoj[0], rangoj[1] + 1):
            cad += str(lista[x][y])
    return cad

def cantBombasAlrededor(lista, i, j):
    """ Retorna la cantidad de bombas que rodean a una celda. """
    cadena = generarCadena(lista, i, j)
    cant = cadena.count('-1')
    return cant

def recorrerLista(lista):
    """ Recorre la lista de enteros y actualiza su valor en función de cuántas
    bombas rodean a una celda. """
    for i in range(0, len(lista)):
        for j in range(0, len(lista[i])):
            if lista[i][j] != -1:
                lista[i][j] = cantBombasAlrededor(lista, i, j)

estructura = [
'-*-*-',
'--*--',
'----*',
'*----',
]

nueva_estructura = generarLista(estructura)
recorrerLista(nueva_estructura)
for elem in nueva_estructura:
    elem = str(elem).replace('-1', '*').replace(',', '')
    print (elem)