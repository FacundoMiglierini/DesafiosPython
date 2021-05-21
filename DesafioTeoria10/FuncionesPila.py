from Pila import Pila


def crear_pila_vacia():
    obj = Pila()

    return obj

def crear_pila_con_datos():
    obj = Pila(1)
    
    for i in range(5):
        obj.push(i)

    return obj