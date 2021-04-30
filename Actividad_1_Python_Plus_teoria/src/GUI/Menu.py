import PySimpleGUI as sg 

def build():

    sg.theme('DarkBlue')

    pad_buttons = (120,10)
    size_buttons = (27, 2)

    layout = [
        [sg.Text('Seleccione datos a analizar', justification= 'center', font= ('Candara', 20), background_color= sg.theme_background_color(), pad= (80, (30, 50)))],
        [sg.Button('Personajes de League of Legends', key= '-DATASET1-', pad= pad_buttons, size= size_buttons, border_width= 2)],
        [sg.Button('Ventas de Videojuegos', key= '-DATASET2-', pad= pad_buttons, size= size_buttons, border_width= 2)],
        [sg.Button('Salir', key= '-EXIT-', pad= pad_buttons, size= size_buttons, border_width= 2)]
            ]

    return sg.Window('Actividad 1 x Python Plus', no_titlebar= True, grab_anywhere= True).Layout(layout)