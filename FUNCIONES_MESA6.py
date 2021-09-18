import random

def mostrar_butacas(salaCine):
    '''Muestra el estado actual de la reserva de butacas de la sala en cuestion, de frente a la pantalla
    Autor: Rodrigo Forcadell '''

    filas = len(salaCine)
    columnas = len(salaCine[0])
    
    print(columnas*"▓"*3)
    print(columnas*"▓"*3)
    
    for f in range(filas):
        for c in range(columnas):
            if salaCine[f][c] == 0:
                print(" ◙ ", end="")
            else:
                print(" · ", end="")
        print()

    print("")
    print("(LIBRE: ◙ | RESERVADA: ·)")


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
            raise IndexError
    
    except IndexError:
        reserva = False
    
    return reserva