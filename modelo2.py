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
    [sg.Text('¿Qué nota musical es?')],[sg.Button('Do')],
    [sg.Button('Re')],[sg.Button('Mi')],[sg.Button('Fa')],[sg.Button('Cancel')],
]

window=sg.Window('Ejercicio', layout)

while True:
    event, value =window.read()  
    if event == 'REPRODUCIR':
        reproductor('do.wav')
    if event == 'Cancel' or sg.WIN_CLOSED:
        break
    if event==None:
        pass
    elif event == 'Do':
        sg.popup_ok('Felicitaciones :D')
    elif event == 'RE' or 'Mi'or 'Fa':
        sg.popup_ok('Intenta de nuevo :c')
    


window.close()