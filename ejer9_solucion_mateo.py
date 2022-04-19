def analizar_columnas(*filas):
    cant_columnas = len(filas[0])
    str_total = ''
    for pos_columna in range(cant_columnas):
        conteo = '*'
        if filas[0][pos_columna] != '*':
            cant = 0
            for fila in filas:
                if pos_columna == 0:
                    cant += fila[pos_columna:pos_columna+2].count('*')
                elif pos_columna == cant_columnas-1:
                    cant += fila[pos_columna-1:pos_columna+1].count('*')
                else:
                    cant += fila[pos_columna-1:pos_columna+2].count('*')
            conteo = f'{cant}'
        str_total += f'{conteo}'
    return str_total


def analizar_filas(buscamina):
    buscamina_con_pista = []
    cant_filas = len(buscamina)
     
    buscamina_con_pista.append(analizar_columnas(buscamina[0], buscamina[1]))
    for pos_fila in range(1, cant_filas-1):
        buscamina_con_pista.append(analizar_columnas(buscamina[pos_fila], buscamina[pos_fila-1], buscamina[pos_fila+1]))
    buscamina_con_pista.append(analizar_columnas(buscamina[-1], buscamina[-2]))

    return buscamina_con_pista



buscamina = [
    '-*-*-',
    '--*--',
    '----*',
    '-----',
    '***--',
]

buscamina_con_pista = analizar_filas(buscamina)


print('[')
for linea in buscamina_con_pista:
    print(f' {linea},') 
print(']')
