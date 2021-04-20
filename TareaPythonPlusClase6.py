import csv
import collections
import requests

with open('Desafios Python\\appstore_games.csv','r', encoding= 'utf8') as a:
    archivo_csv = csv.reader(a, delimiter = ',')
    next(archivo_csv)
    juegos_gratuitos_esp = list(filter(lambda x : x[7] == 0 and 'ES' in x[12] , archivo_csv))

    a.seek(0)
    next(a)
    dicc = {elem[4]: elem[6] for elem in archivo_csv}
    juegos_mas_calificaciones = collections.Counter(dicc).most_common(10)

    print('Juegos gratuitos disponibles en idioma español: ')
    for elem in juegos_gratuitos_esp:
        print(elem[2])

    print('Iconos de los 10 juegos con más calificaciones de usuarios: ')
    for elem in juegos_mas_calificaciones:
        print(elem)