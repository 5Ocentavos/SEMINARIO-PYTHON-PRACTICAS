from ast import Pass
import PySimpleGUI as sg
from src.windows import menu
from src.component import setting
#from src.component import profiles

def start ():
    window = loop ()
    window.close ()



def loop ():

    window = menu.build ()

    while True:
        event, values = window.read ()

        print (event)
        print (values)

        if event in (sg.WINDOW_CLOSED, "-EXIT-"):
            break

        
        if event == "-PLAY-":
            pass

        if event == "-SETTINGS-":
            window.hide ()
            setting.start ()
            window.un_hide ()
       
        if event =="-PUNTAJES-":
            pass
        
        if event == "-PERFIL-":
            #porfiles.start ()
            pass
    return window

