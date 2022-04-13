def contarBombas (aux_str):
    cant_bombas = 0
    for caracter in aux_str:
        if (caracter == '*'):
            cant_bombas += 1
    return str(cant_bombas)

def contarBombasMejorado (aux_str):
    return str(aux_str.count ('*'))


def analizarColumnas (*filas):
    cant_filas = len (filas)
    cant_columnas = len (filas[0])
    str_total = ''
    for pos_columna in range (cant_columnas):
        if (filas[0][pos_columna] != '*'):
            aux_str = ''
            for pos_fila in range (cant_filas):
               
                if (pos_columna == 0):
                    aux_str += filas [pos_fila][pos_columna:pos_columna +2]
                elif (pos_columna == cant_columnas -1):
                     aux_str += filas [pos_fila][pos_columna - 1 :pos_columna + 1]
                else:
                    aux_str += filas [pos_fila][pos_columna - 1:pos_columna + 2]
            str_total += contarBombasMejorado (aux_str)
        else:
            str_total += '*'
    return str_total


def analizarFilas (buscamina):
    buscamina_con_pista = []
    cant_filas = len (buscamina)
     
    for pos_fila in range (cant_filas):
        str_fila = ''
        if (pos_fila == 0):
            str_fila += analizarColumnas (buscamina[pos_fila], buscamina[pos_fila +1])
        elif (pos_fila == (cant_filas -1)):
            str_fila += analizarColumnas (buscamina[pos_fila], buscamina[pos_fila -1])
        else:
            str_fila += analizarColumnas (buscamina[pos_fila], buscamina[pos_fila -1], buscamina [pos_fila + 1])
        buscamina_con_pista.append (str_fila)
    return buscamina_con_pista



buscamina = [
    '-*-*-',
    '--*--',
    '----*',
    '-----',
    '***--',
]

buscamina_con_pista = analizarFilas (buscamina)


print ('[')
for linea in buscamina_con_pista:
    print (' ' + linea + ',') 
print (']')




















