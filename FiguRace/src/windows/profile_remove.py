import PySimpleGUI as sg

def build ():
    """Este método crea la ventana eliminar perfil"""
    layout= [
                [sg.Push(),sg.Text('Ingrese su nick', font=("Helvetica", 72)),sg.Push()],
                [sg.Push(),sg.Input('Nick',key='Nombre',font=("Helvetica", 20)),sg.Push()],
                [sg.Push(),sg.Button('Aceptar',button_color=('white', '#333333'), size=(15, 2), font=("Helvetica", 20)),
                 sg.Button('Cancelar',button_color=('white', '#333333'), size=(15, 2), font=("Helvetica", 20)),sg.Push()]
                 ]
    return sg.Window('Eliminar perfil', layout).Layout(layout)
   
