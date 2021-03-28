cad = input ('Ingrese una palabra o frase: ').lower()

es = True

for car in cad:
    if car.isalpha() and cad.count(car) > 1:
        es = False
        break

print('La cadena es un heterograma.' if (es) else 'La cadena no es un heterograma.')

