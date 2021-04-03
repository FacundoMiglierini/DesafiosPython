
def encripto(cadena):
    """Retorna una cadena encriptada en Cifrado César si dicha cadena
        es válida, es decir, si tiene solo caracteres alfanuméricos."""
    lista_de_acciones = [lambda cad: cad.replace(' ', ''), lambda cad: cad.replace(',', ''), lambda cad: cad.replace('.', '')]
    for accion in lista_de_acciones:
        cadena = accion(cadena)
    if cadena.isalnum():
        return ''.join(map(lambda x: chr(ord(x) + 1) if (x not in 'Zz9') else (chr(ord(x) - 25) if (x in 'Zz') else chr(ord(x) - 9)), cadena))
    else:
        return "Error: cadena no válida."

print(encripto("a"))
print(encripto("ABC"))
print(encripto("Rock2021"))