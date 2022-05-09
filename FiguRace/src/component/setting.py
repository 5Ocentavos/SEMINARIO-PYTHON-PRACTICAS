import PySimpleGUI as sg
from src.windows import setting
from src.handlers import setting as setting_save

def start ():
    window = loop ()
    window.close ()



def loop ():
    window = setting.build ()

    while True:
        event, values = window.read ()

        if event in (sg.WINDOW_CLOSED, "-CANCEL-"):
            break

        if event == "-SAVE-":
            setting_save.save (values)
            
    return window