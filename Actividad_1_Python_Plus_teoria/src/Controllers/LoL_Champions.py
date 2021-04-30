import csv
import os
import json

def start():
    datos = open_file_csv()
    datos_filtrados = filtrar_datos(datos)
    export(datos_filtrados)

def es_asesino(tags):
    for elem in tags.replace('[', '').replace(']', '').replace("'", '').split(','):
        if elem.strip() == 'Assassin':
            return True

def filtrar_datos(datos):
    return list(filter(lambda x : es_asesino(x['tags']), datos))[:20]

def export(datos):
    path_exp = os.path.join(os.getcwd(), 'Export')
    archivo_exportado_lol = 'lol_assassins.json'
    path_file_exp = os.path.join(path_exp, archivo_exportado_lol)

    with open (path_file_exp, 'w') as archivo_exp:
        json.dump(datos, archivo_exp, indent= 4)


def open_file_csv():
    archivo_lol = 'riot_champion.csv'
    path_arch = os.path.join(os.getcwd(), 'src', 'Models')

    with open(os.path.join(path_arch, archivo_lol), encoding= 'UTF-8') as campeones_lol:
        datos = []

        for i in csv.DictReader(campeones_lol):
            datos.append(dict(i))
            
    return datos