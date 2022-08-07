import PySimpleGUI as sg #Importación

sg.theme("DarkBlue8") # Diseño de la ventana 

# Funciones a utilizar
def menu_inicio(): #En progreso, aún no se usa
    event, values = inicio.read()
    if event == "Aprende las notas musicales":
        inicio.close()
        while True:
            event, values = aprender.read()
            if event == sg.WIN_CLOSED:
                break
            if event == "Regresar al menú inicio": 
                event, values = inicio.read()
                aprender.close()
            if event == "Pon en práctica tus conocimientos":
                inicio.close()
                while True:
                    event, values = elegir.read()
                    if event == "Salir de la aplicación" or event == sg.WIN_CLOSED:
                        break
                    if event == "Regresar al menú inicio":
                        event, values = inicio.read()
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


# Contenidos de las ventanas
ly_saludo = [  [sg.Text("Aprende a leer el pentagrama", size =(30, 2))],
            [sg.Text("Introduce tu nombre: ", size =(15, 1)), sg.Input()],
            [sg.Button("OK")], [sg.Button("Salir")]
            ]

ly_inicio = [  [sg.Button("Aprende las notas musicales")],
            [sg.Button("Pon en práctica tus conocimientos")],
            [sg.Button("Salir de la aplicación")]
            ]

ly_aprender = [ [sg.Text("Mostrar el pentagrama con las notas musicales ubicadas, tanto en clave de sol como de fa")],
            [sg.Button("Regresar al menú inicio")]
            ]

ly_elegir = [  [sg.Text("Elige la clave de tu preferencia")],
            [sg.Button("sol")],
            [sg.Button("fa")],
            [sg.Button("Regresar al menú inicio")],
            [sg.Button("Salir de la aplicación")]
            ]

ly_sol = [
            [sg.Text("Practica con un pentagrama en clave de sol", size =(30, 2))]
        ]

ly_fa = [
            [sg.Text("Practica con un pentagrama en clave de fa", size =(30, 2))]
        ]

# Creación de las ventanas
saludo = sg.Window("Proyecto Grupo 08: Aprende a leer el pentagrama", ly_saludo)
inicio = sg.Window("Menú inicio", ly_inicio)
elegir = sg.Window("Elige la clave", ly_elegir)
aprender = sg.Window("Aprende la ubicación de las notas musicales", ly_aprender)
juego_sol = sg.Window("Juego en clave de sol", ly_sol)
juego_fa = sg.Window("Juego en clave de fa", ly_fa)

try:
    while True:
        event, values = saludo.read()
        if event == "Salir"  or event == sg.WIN_CLOSED:
            break
        if event == "OK":
            sg.popup_ok("Bienvenido " + values[0] + ". ¿Estás listo para empezar a aprender?")
            saludo.close()
            while True:
                event, values = inicio.read()
                if event == "Salir de la aplicación"  or event == sg.WIN_CLOSED:
                    break
                if event == "Aprende las notas musicales":
                    inicio.close()
                    while True:
                        event, values = aprender.read()
                        if event == sg.WIN_CLOSED:
                            break
                        if event == "Regresar al menú inicio": 
                            event, values = inicio.read()
                            aprender.close()
                if event == "Pon en práctica tus conocimientos":
                    inicio.close()
                    while True:
                        event, values = elegir.read()
                        if event == "Salir de la aplicación" or event == sg.WIN_CLOSED:
                            break
                        if event == "Regresar al menú inicio":
                            event, values = inicio.read()
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
    elegir.close()
    juego_sol.close()
    juego_fa.close()
