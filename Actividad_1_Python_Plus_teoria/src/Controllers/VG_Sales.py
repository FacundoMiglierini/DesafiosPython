import os
import csv
import json

def start():
    datos = open_file_csv()
    datos_filtrados = filtrar_datos(datos)
    export(datos_filtrados)

def filtrar_datos(datos):
    return list(filter(lambda x: x['Platform'] == 'PC' and x['Year'] == '2013', datos))

def export(datos):
    archivo_exp = 'VG_Sales_PC_2013.json'
    path_exp = os.path.join(os.getcwd(), 'Export')

    with open(os.path.join(path_exp, archivo_exp), 'w') as file_exp:
        json.dump(datos, file_exp, indent= 4)

def open_file_csv():
    archivo_vg = 'vgsales.csv'
    path_arch = os.path.join(os.getcwd(), 'src', 'Models')
    
    with open(os.path.join(path_arch, archivo_vg), encoding= 'UTF-8') as ventas_vg:

        datos = []

        for i in  csv.DictReader(ventas_vg):
            datos.append(dict(i))

    return datos