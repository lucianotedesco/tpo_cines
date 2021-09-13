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


def cargar_sala(matrizButacas):
    '''Llena aleatoriamente la sala, simulando las reservas que pudieron haberse realizado. (0 = Vacía | 1 = Reservada)
    Autor: Gustavo Escudero'''

    for f in range(len(matrizButacas)):
        for c in range(len(matrizButacas[f])):
            butacaReservada = random.randint(0, 1)
            matrizButacas[f][c] = butacaReservada

    return matrizButacas