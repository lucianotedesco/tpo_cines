#libreria utilizada en proceso de desarrollo para limpiar pantalla y facilitar lectura entre ejecucciones
from clear_screen import clear
import math
import FUNCIONES_MESA6


# ------------- MATRICES

def MATRIZ_crear(filas,columnas):
    '''Crea y devuelve una matriz del tamaño especificado'''

    matriz = []
    for f in range(int(filas)):
        matriz.append([])
        for c in range(int(columnas)):
            matriz[f].append(0)
    return matriz


# ------------- ARCHIVOS

def ARCHIVO_cargar_salas(salasCine):
    '''Obtengo del archivo de salas las mismas, su nombre y su capacidad'''

    try:
        arch = open("salas.txt")
    except OSError as msg:
        print("Error:", msg)
    else:
        linea = arch.readline()
        i = 0
        erroresLectura = []
        while linea:
            try:
                salasCine[i] = linea.strip().split(";")
            except ValueError:
                erroresLectura.append(i)

            linea = arch.readline()
            i += 1
            if (len(erroresLectura)):
                print("Han ocurrido los siguientes errores:", erroresLectura)
    finally:
        try:
            arch.close()
        except NameError:
            pass


# ------------- UTILIDADES GENERICAS

def UTILS_ingresar_entero_en_rango(enteroInicial, enteroFinal, mensajeError):
    '''Le pide al usuario ingresar un numero hasta que el mismo sea un entero, comprendido entre el rango solicitado.
       Los extremos están incluidos. Recibe el mensaje de error que debe mostrarse.'''

    while True:
        try:
            num = int(input("> "))
            if num < int(enteroInicial) or num > int(enteroFinal): raise ValueError
            break
        except ValueError:
            print(f"!> {mensajeError}")

    return num

def UTILS_transformar_butaca_en_coordenada(numeroButaca, infoSalaSeleccionada):
    longitudFilas = int(infoSalaSeleccionada[2])

    fila = math.floor(numeroButaca / longitudFilas)
    columna = numeroButaca % longitudFilas
    return fila, columna         

# ------------- SALAS

def SALA_seleccionar(salasCine):
    '''Permito que el usuario seleccione una sala, y devuelvo el registro de sala junto a su indice'''

    print("■ Seleccione en que sala desea realizar la reserva:")
    for index, sala in enumerate(salasCine):
        print(f"· SALA {index + 1} \"{sala[0]}\"")
    print("")

    numeroPrimerSala = 1
    numeroUltimaSala = len(salasCine)
    mensajeErrorSalaNoEncontrada = "La sala ingresada no fue encontrada, intente nuevamente"
    indiceSala = UTILS_ingresar_entero_en_rango(numeroPrimerSala, numeroUltimaSala, mensajeErrorSalaNoEncontrada)

    return salasCine[indiceSala - 1]

def SALA_obtener_butacas(salaSeleccionada):
    '''Obtenemos una matriz representando la ocupación de las butacas en la sala, y la agregamos junto con su información.'''

    try:
        matrizSalaVacia = MATRIZ_crear(salaSeleccionada[1],salaSeleccionada[2])
    except IndexError:
        print("!> No se pudo obtener la información completa de las salas, por favor revise la estructura del archivo \"salas.txt\"")

    butacas_sala = FUNCIONES_MESA6.cargar_sala(matrizSalaVacia)
    salaSeleccionada.append([])
    salaSeleccionada[3] = butacas_sala

def RESERVA_iniciar_reservacion(salaSeleccionada):
    '''Realizamos la reserva de butacas en la sala recibida, obteniendo del usuario la cantidad de entradas que desea'''
    butacas = salaSeleccionada[3]

    capacidadSala = FUNCIONES_MESA6.butacas_libres(butacas)
        
    print(f"■ QUEDAN {capacidadSala} ASIENTOS DISPONIBLES")
    print("■ Para realizar una reserva, ingrese la cantidad de entradas que necesita")
    mensajeErrorCapacidad = "La cantidad de entradas es inválida (recuerde que no puede superar la capacidad actual). Intente nuevamente"
    cantidadEntradas = UTILS_ingresar_entero_en_rango(1,capacidadSala,mensajeErrorCapacidad)
    
    reservaRealizada = False    
    if cantidadEntradas == 1:
        while not reservaRealizada: 
            RESERVA_intentar_reserva_individual(salaSeleccionada)
    else:
        for entrada in range(cantidadEntradas):
            print(f"■ Aún debe elegir {cantidadEntradas - entrada} entradas:")
            while not reservaRealizada: 
                reservaRealizada = RESERVA_intentar_reserva_individual(salaSeleccionada)
            reservaRealizada = False
    

def RESERVA_intentar_reserva_individual(salaSeleccionada):
    '''Intentamos reservar un asiento en particular'''

    butacas = salaSeleccionada[3]

    print("■ Digite la posición de la butaca deseada:")   
    totalButacasSala = int(salaSeleccionada[1]) * int(salaSeleccionada[2])
    mensajeErrorCapacidad = "La posición ingresada no existe en la sala"
    butacaElegida = UTILS_ingresar_entero_en_rango(0,totalButacasSala,mensajeErrorCapacidad)

    fila,columna = UTILS_transformar_butaca_en_coordenada(butacaElegida, salaSeleccionada)    
    reservaRealizada = FUNCIONES_MESA6.reservar(butacas,fila,columna)
    clear()

    print("")
    FUNCIONES_MESA6.mostrar_butacas(butacas)
    print("")

    if not (reservaRealizada):        
        print("!> La butaca que intentó reservar ya se encuentra ocupada")
    else:
        print("■ RESERVA REALIZADA!")

    return reservaRealizada


# ------------- VISUAL

def VISUAL_mostrar_mensajes_inicio():
    '''Muestro los mensajes de inicio del sistema'''

    print("■ Iniciando SIRA: (Sistema Integral de Reserva de Asientos)")
    print("■ BIENVENIDO!     (Producto registrado a nombre de CINES DEL BARRIO S.R.L)")
    print("")
    print("")



# --------------------------------
# ------------- PROGRAMA PRINCIPAL
    #TODO: UNIFICAR infoSalaSeleccionada y butacasSalaSeleccionada en una misma variable
def main():
    while True:
        clear()
        VISUAL_mostrar_mensajes_inicio()
        

        salasCine = MATRIZ_crear(3,5)
        ARCHIVO_cargar_salas(salasCine)

        salaSeleccionada = SALA_seleccionar(salasCine)
        SALA_obtener_butacas(salaSeleccionada)

        clear()
        print(f"■ SALA \"{salaSeleccionada[0]}\"")
        print("")
        FUNCIONES_MESA6.mostrar_butacas(salaSeleccionada[3])
        print("")
        
        RESERVA_iniciar_reservacion(salaSeleccionada)
        print("")
        print("■ Ha terminado con las reservas solicitadas! Se lo redigirá al sistema de facturación... Pulse una tecla para continuar­")


main()


