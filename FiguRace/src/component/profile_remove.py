from src.windows import profile_remove
import PySimpleGUI as sg
from src.handlers import profiles_remove as delate

def start ():
    window = loop ()
    window.close ()



def loop ():

    window = profile_remove.build ()

    while True:
        event, values = window.read ()

        if event in (sg.WINDOW_CLOSED, "-CANCEL-"):
            break

        if event == "--ACCEP-":
            delate.eliminar_perfil (values["-NOMBRE-"])
    return window