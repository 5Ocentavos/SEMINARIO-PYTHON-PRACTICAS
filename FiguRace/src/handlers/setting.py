import json
import os

def validate_data (values):
    """Este método verifica que el valor de cada dato ingresado por el jugador sea válido. """

    for clave in values:
        if values [clave] == "":
            values[clave] = 5
        elif type (values [clave]) == str: # Si el jugador ingreso "quince" el manejador pone el valor por defecto 5 
            try:
                values [clave] = int (values[clave])
            except ValueError:
                values [clave] = 5
    return values



def save (values):
    """Este método pisa la configuración por defecto que guarda el archivo configuracion_actual.json
       por la nueva configuración que el jugador ingresó"""

    values = validate_data (values)
   # print (os.path.dirname(os.path.realpath (".")))
   # print (os.getcwd())
    ruta = (os.path.join (os.getcwd(), "src", "generated_data", "configuracion_figurase.json"))
    #ruta_completa = os.path.join (ruta, "generated_data", "configuracion_figurase.json")
    archivo_configuracion = open (ruta, "w")
    json.dump (values, archivo_configuracion)
    archivo_configuracion.close ()
