import PySimpleGUI as sg

def build ():
    """Este método crea la ventana configuración"""
    layout = [
              [sg.Text ("Tiempo: ", size =(20, 1)), sg.Combo(list (range (10, 240, 10)), default_value=5, key="-TIEMPO LIMITE-", size=(5,15))],
              [sg.Text ("Rondas: ", size =(20, 1)), sg.Combo(list (range (1,16)), default_value=3, key="-CANTIDAD DE RONDAS-", size=(5,10))],
              [sg.Text ("Puntaje sumado: ", size =(20, 1)), sg.Combo(list (range (1,6)), default_value=1, key="-PUNTOS A SUMAR-", size=(5,10))],
              [sg.Text ("Puntaje restado: ", size =(20, 1)), sg.Combo(list (range (1,6)), default_value=1, key="-PUNTOS A RESTAR-", size=(5,10))],
              [sg.Text ("Columnas a mostrar: ", size =(20, 1)), sg.Combo(list (range (1,6)), default_value=5, key="-COLUMNAS A MOSTRAR", size=(5,10))],
              [sg.Button ('Guardar cambios', key = "-SAVE-"), sg.Button ('Cancelar', key = "-CANCEL-") ]
             ]
    return sg.Window ("Configuración").Layout (layout)
