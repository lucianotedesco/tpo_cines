import random

def mostrar_butacas(matriz):
    '''Muestra el estado actual de la reserva de butacas de la sala en cuestion, mostrando la pantalla del cine como referencia de ubicación.
    Autor: Rodrigo Forcadell '''

    #el sistema adjunta al principio del print codigos de colores para hacer mas interactiva la experiencia
    greenColor = '\033[92m'
    whiteColor = "\033[0m"

    print("")
    filas = len(matriz)
    columnas = len(matriz[0])
    butaca = 0
    print(columnas*"▓"*6)
    print(columnas*"▓"*6)
    
    for f in range(filas):
        for c in range(columnas):
            if matriz[f][c] == 0:
                color = whiteColor
                print(color + "%5d" %butaca , end=" ")
            else:     
                if (matriz[f][c] == 2):
                    caracterOcupado = "X"
                    color = greenColor
                else:
                    color = whiteColor
                    caracterOcupado = "■"
                espacio = len(str(butaca)) * " " + caracterOcupado
                print(color + "%5s" %espacio , end=" ")
            butaca+=1
        print()   

    print("")
    print("(LIBRE: n° butaca | RESERVADA: ■ | RESERVAS DE ESTA SESIÓN: X)")
    print("")


def butacas_contiguas(matriz,n_fila):
    '''Busca la mayor cantidad de butacas contiguas en la fila recibida, y devuelve tanto la cantidad como su ubicación
    Autor: Hernan Ducceschi'''

    contiguas = 0
    maxButacasContiguas = 0
    columnaInicio = 0

    for columnaFin,butaca in enumerate(matriz[n_fila]):
        if butaca == 0:
            contiguas += 1
        else:  
            contiguas = 0
        if contiguas > maxButacasContiguas:
            maxButacasContiguas = contiguas
            columnaInicio = (columnaFin + 1) - contiguas           
    return columnaInicio, maxButacasContiguas


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
            matriz[x][y] = 2
        else:
            reserva = False
    
    except IndexError:
        reserva = False
    
    return reserva