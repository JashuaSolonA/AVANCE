import pygame
import PySimpleGUI as sg

def reproductor(cancion):
    pygame.mixer.init(frequency=44100)
    pygame.mixer.music.load(str(cancion))
    pygame.mixer.music.set_volume(1) 
    pygame.mixer.music.play(1) 

sg.theme('Sandybeach')

layout=[
    [sg.Button('REPRODUCIR')],
    [sg.Image('do.png')],
    [sg.Text('¿Qué nota musical es?')],[sg.InputText()],
    [sg.Button('OK')],[sg.Button('Cancel')],
]

windowdo=sg.Window('Ejercicio', layout)

while True:
    event, value =windowdo.read()  
    if event == 'REPRODUCIR':
        reproductor('do.wav')
    if event == 'Cancel' or sg.WIN_CLOSED:
        break
    elif value[1] == '':
        pass
    elif value[1] != 'do':
        sg.popup_ok('Intentalo de nuevo')
    else:
        sg.popup_ok('Felicitaciones')


windowdo.close()