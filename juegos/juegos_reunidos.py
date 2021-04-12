import hangman
import reverse
import tictactoe

def mostrar_menu():
    while True:
        print("""
        Seleccione la tarea a realizar:
        1: jugar al "Hangman"
        2: jugar al "Reverse"
        3: jugar al "Tic Tac Toe"
        0: finalizar el programa.
        """)
        x = input('Tarea a realizar: ')
        if x in ('0123'):
            return x
        else:
            print('Por favor, ingrese un valor válido.')

while True:
    x = mostrar_menu()
    if x == '1':
        hangman.programa_principal()
    elif x == '2':
        reverse.programa_principal()
    elif x == '3':
        tictactoe.programa_principal()
    else:
        break


