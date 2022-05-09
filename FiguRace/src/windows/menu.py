import PySimpleGUI as sg

def build ():
    """Este método retorna la ventana principal del juego"""
    
    layout = [
              [sg.Text ('Menú principal',justification='center')],
              [sg.Button('Iniciar juego', key="-PLAY-", size=(50,2))],
              [sg.Button('Configurar', key="-SETTINGS-", size=(50,2))],
              [sg.Button('Ver puntajes', key="-PUNTAJES-", size=(50,2))], 
              [sg.Button('Ver perfil', key="-PERFIL-", size=(50,2))],
              [sg.Button('Salir', key="-EXIT-", size=(50,2))]
             ]

    return sg.Window ("FiguRace").Layout (layout)

    