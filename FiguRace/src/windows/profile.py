import PySimpleGUI as sg

def build ():
    """Este método crea la ventana eliminar perfil"""
    layout = [
        [sg.Push(), sg.Text('PERFILES', font=("Helvetica", 72)), sg.Push()],
        [sg.Push(),sg.Button("Agregar perfil",button_color=('white', '#333333'), size=(15, 2), font=("Helvetica", 20)),sg.Push()],
        [sg.Push(),sg.Button("Eliminar perfil", button_color=('white', '#333333'), size=(15, 2), font=("Helvetica", 20)),sg.Push()],
        [sg.Push(),sg.Button('Atras', button_color=('white', '#333333'), size=(15, 2), font=("Helvetica", 20)),sg.Push()]
    ]
    return sg.Window("Perfil").Layout(layout)