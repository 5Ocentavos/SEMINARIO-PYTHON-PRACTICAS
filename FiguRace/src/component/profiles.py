from src.windows import profiles
import PySimpleGUI as sg
from src.component import profile_add
from src.component import profile_remove

def start ():
    window = loop ()
    window.close ()



def loop ():

    window = profiles.build ()

    while True:
        event, values = window.read ()

        if event in (sg.WINDOW_CLOSED, "-AFTER-"):
            break

        if event == "-ADD_PROFILE-":
            window.hide ()
            profiles_add.start ()
            window.un_hide ()    

        if event == "-REMOVE_PROFILE-":
            window.hide ()
            profiles_remove.start ()
            window.un_hide ()

    return window
