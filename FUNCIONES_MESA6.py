import random

def mostrar_butacas(matriz):
    '''Muestra el estado actual de la reserva de butacas de la sala en cuestion, de frente a la pantalla
    Autor: Rodrigo Forcadell '''

    filas = len(matriz)
    columnas = len(matriz[0])
    butaca = 0
    print(columnas*"▓"*6)
    print(columnas*"▓"*6)
    
    for f in range(filas):
        for c in range(columnas):
            if matriz[f][c] == 0:
                print("%5d" %butaca , end=" ")
            else:     
                espacio = len(str(butaca)) * " " + "■"
                print("%5s" %espacio , end=" ")
            butaca+=1
        print()   

    print("")
    print("(LIBRE: (n°) | RESERVADA: ■)")

def butacas_contiguas(matriz,n_fila):
    '''Busca la mayor cantidad de butacas contiguas en la fila recibida, y devuelve tanto la cantidad como su ubicación
    Autor: Rodrigo Forcadell'''

    seguidas = 0
    maxcontador = 0
    columna = 0
    ubicacion = -1
    
    if 0 in matriz[n_fila]:
        for butaca in matriz[n_fila]:
            
            if butaca == 0:
                seguidas+=1
                                
            elif maxcontador<seguidas:
                
                maxcontador = seguidas
                ubicacion = columna-seguidas
                seguidas=0
            columna+=1    
        if maxcontador<seguidas:
                
                maxcontador = seguidas
                ubicacion = columna-seguidas
                seguidas=0
        return ubicacion, maxcontador         
    else:
        return ubicacion, maxcontador

def cargar_sala(matrizSala):
    '''Llena aleatoriamente la sala, simulando las reservas que pudieron haberse realizado. (0 = Vacía | 1 = Reservada)
    Autor: Gustavo Escudero'''

    for f in range(len(matrizSala)):
        for c in range(len(matrizSala[f])):
            butacaReservada = random.randint(0, 1)
            matrizSala[f][c] = butacaReservada

    return matrizSala

def butacas_libres(matrizSala): 
    '''Recibe una sala y devuelve la cantidad de butacas disponibles
    Autor: Ezequiel Villa Paredes'''

    cont_libres = 0
    fila = len(matrizSala)
    columna = len(matrizSala[0])

    for f in range(fila):
        for c in range(columna):
            if matrizSala[f][c] == 0:
                cont_libres = cont_libres + 1

    return cont_libres     

def reservar(matriz,x,y):
    '''Recibe una representación matricial de una sala de cine y reserva la butaca seleccionada
    Autor: Ramiro Farfañuk'''
    
    reserva = True
    try:
        if matriz[x][y] == 0:
            matriz[x][y] = 1
        else:
            reserva = False
    
    except IndexError:
        reserva = False
    
    return reserva