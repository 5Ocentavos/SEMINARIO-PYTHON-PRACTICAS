from src.windows import profile_add
import PySimpleGUI as sg

def start ():
    window = loop ()
    window.close ()



def loop ():

    window = profile_add.build ()

    while True:
        event, values = window.read ()

        if event in (sg.WINDOW_CLOSED, "-CANCEL-"):
            break

        if event == "--ACCEP-":
            pass
    return window