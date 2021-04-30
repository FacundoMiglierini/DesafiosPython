import PySimpleGUI as sg 
from src.GUI import Menu
from src.Controllers import LoL_Champions
from src.Controllers import VG_Sales

def start():
    loop()

def loop():
    window = Menu.build()

    while True:

        event, values = window.read()

        if event == '-EXIT-':
            break

        if event == '-DATASET1-':
            LoL_Champions.start()
            sg.Popup('Se ha generado un archivo con 20 personajes de LoL cuyo rol es Asesino en la carpeta "Export". ', 
            no_titlebar= True, background_color= 'LightBlue', text_color= 'Black')

        if event == '-DATASET2-':
            VG_Sales.start()
            sg.Popup('Se ha generado un archivo con las ventas de videojuegos para PC realizadas en el año 2013 en la carpeta "Export". ', 
            no_titlebar= True, background_color= 'LightBlue', text_color= 'Black')

    window.close()
