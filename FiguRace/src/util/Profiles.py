
import json
from util.Jugador import Jugador

class Perfiles:
    def __init__(self):
        '''Comprueba si existe un archivo de perfiles, si existe: guarda los jugadores en una lista, sino: crea el archivo '''
        try:
            with open('perfiles.json', 'r', encoding='UTF-8')as dataset:
                reader=json.load(dataset)
                self._lista_jugadores=[Jugador(x['Name'],x['Age'],x['Genre'],[x['Easy'],x['Medium'],x['Hard']]) for x in reader]
        except:
            with open('perfiles.json', 'w', newline='', encoding='UTF-8')as dataset:
                self._lista_jugadores=[]



        
    def agregar_jugador(self, nombre, edad, genero):
        '''Comprueba si el nombre no existe, entonces lo agrega a la lista de jugadores'''
        if(nombre not in [x.get_nombre() for x in self._lista_jugadores]):
            self._lista_jugadores.append(Jugador(nombre, edad, genero))
        else:
            print('Este nick ya pertenece a un jugador -_-')
    
    def  eliminar_jugador(self, nombre):
        '''Elimina un jugador de la lista de jugadores'''
        try:
            self._lista_jugadores.remove([x for x in self._lista_jugadores if x.get_nombre()==nombre][0])
            return True
        except(IndexError):
            return False
            
    
    def get_lista_jugadores(self):
        return self._lista_jugadores
    
    def crear_archivo(self):
        '''Sobreescribe el archivo de perfiles'''
        with open('perfiles.json', 'w', newline='', encoding='UTF-8')as dataset:
            puntaje=json.dumps([{'Name':jugador.get_nombre(),'Age':jugador.get_edad(), 'Genre':jugador.get_genero(),'Easy': jugador.get_puntajes()[0],'Medium': jugador.get_puntajes()[1], 'Hard':jugador.get_puntajes()[2]}for jugador in self._lista_jugadores])
            dataset.write(puntaje)

                #'Age':jugador.get_edad(), 'Genre':jugador.getGenero()

