import pygame
import sys
import PySimpleGUI as sg

pygame.mixer.init(frequency=44100)

pygame.mixer.music.load('recursos2/ringtones-super-mario-bros.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(1.0)

size = 800, 600

VENTANA = pygame.display.set_mode(size)
pygame.display.set_caption('Musica')
Imagen = pygame.image.load('recursos2/mariobros.png')
pygame.display.set_icon(Imagen)

fondo = pygame.image.load('recursos2/mariobros_redimensionada.png')
VENTANA.blit(fondo,(0,0))

ejecuta = True

while ejecuta:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecuta = False
    pygame.display.update()

    keys=pygame.key.get_pressed()

    if keys[pygame.K_2]:
        pygame.mixer.music.set_volume(0.25)

    elif keys[pygame.K_3]:
        pygame.mixer.music.set_volume(0.50)
    
    elif keys[pygame.K_1]:
        pygame.mixer.music.set_volume(0.0)

    elif keys[pygame.K_4]:
        pygame.mixer.music.set_volume(1.0)
    
    sg.theme("DarkBlue8") # Diseño de la ventana 

    # Funciones para crear las ventanas
    def hacer_saludo():
        ly_saludo = [  [sg.Text("Este programa de ayudará a identificar las notas musicales en el pentagrama", text_color = "Black")],
                [sg.Text("Introduce tu nombre: "), sg.Input()],
                [sg.Button("OK")], [sg.Button("Salir")]
                ]
        return sg.Window("Proyecto Grupo 08: Aprende a leer el pentagrama", ly_saludo)

    def hacer_inicio():
        ly_inicio = [  [sg.Button("Aprende las notas musicales")],
                [sg.Button("Pon en práctica tus conocimientos")],
                [sg.Button("Salir de la aplicación")]
                ]   
        return sg.Window("Menú inicio", ly_inicio)

    def hacer_aprender():
        ly_aprender = [ [sg.Text("Estas son las notas ubicadas en el pentagrama en clave de sol:")],
                [sg.Image("recursos2/clave_de_sol.png")],
                [sg.Text("Estas son las notas ubicadas en el pentagrama en clave de fa:")],
                [sg.Image("recursos2/clave_de_fa.png")],
                [sg.Button("Salir de la aplicación")]
                ]
        return sg.Window("Aprende la ubicación de las notas musicales", ly_aprender)

    def hacer_elegir():
        ly_elegir = [  [sg.Text("Elige la clave de tu preferencia")],
                [sg.Button("sol")],
                [sg.Button("fa")],
                [sg.Button("Salir de la aplicación")]
                ]
        return sg.Window("Elige la clave", ly_elegir)

    def hacer_juego_sol():
        ly_sol = [
                [sg.Text("Practica con un pentagrama en clave de sol")]
            ]
        return sg.Window("Juego en clave de sol", ly_sol)

    def hacer_juego_fa():
        ly_fa = [
                [sg.Text("Practica con un pentagrama en clave de fa")]
            ]
        return sg.Window("Juego en clave de fa", ly_fa)

    # Creación de las ventanas
    saludo = hacer_saludo()
    inicio = hacer_inicio()
    aprender = hacer_aprender()
    elegir = hacer_elegir()
    juego_sol = hacer_juego_sol()
    juego_fa = hacer_juego_fa()

    try:
        while True:
            event, values = saludo.read()
            if event == "Salir"  or event == sg.WIN_CLOSED:
                break
            if event == "OK":
                sg.popup_ok("Bienvenido/a " + values[0] + ". ¿Estás listo/a para empezar a aprender?")
                saludo.close()
                while True:
                    event, values = inicio.read()
                    if event == "Salir de la aplicación"  or event == sg.WIN_CLOSED:
                        break
                    if event == "Aprende las notas musicales":
                        inicio.close()
                        while True:
                            event, values = aprender.read()
                            if event == "Salir de la aplicación" or event == sg.WIN_CLOSED:
                                break
                    elif event == "Pon en práctica tus conocimientos":
                        inicio.close()
                        while True:
                            event, values = elegir.read()
                            if event == "Salir de la aplicación" or event == sg.WIN_CLOSED:
                                break
                            if event == "sol":
                                elegir.close()
                                while True:
                                    event, values = juego_sol.read()
                                    if event == sg.WIN_CLOSED:
                                        break
                            elif event =="fa":
                                elegir.close()
                                while True:
                                    event, values = juego_fa.read()
                                    if event == sg.WIN_CLOSED:
                                        break
    except: 
        print("Ocurrió algún error")
    finally:
        saludo.close()
        inicio.close()
        aprender.close()
        elegir.close()
        juego_sol.close()
        juego_fa.close()
        print("Todo cerrado")
        
    pygame.quit()
