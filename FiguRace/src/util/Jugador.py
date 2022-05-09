class Jugador():
    def __init__(self, nombre, edad, genero, puntajes=[0,0,0]):
        self._nombre=nombre
        self._edad=edad
        self._genero=genero
        self._puntajes=puntajes
    def get_nombre(self):
        return self._nombre
    def get_puntajes(self):
        return self._puntajes
    def get_edad(self):
        return self._edad
    def get_genero(self):
        return self._genero
    
    def nuevo_puntaje(self, dificultad, puntaje):
        self._puntajes[dificultad]=puntaje
        
