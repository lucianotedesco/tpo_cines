#libreria utilizada en proceso de desarrollo para limpiar pantalla y facilitar lectura entre ejecucciones
from clear_screen import clear
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
    '''Obtenemos una matriz representando la ocupación de las butacas en la sala'''

    try:
        matrizSalaVacia = MATRIZ_crear(salaSeleccionada[1],salaSeleccionada[2])
    except IndexError:
        print("!> No se pudo obtener la información completa de las salas, por favor revise la estructura del archivo \"salas.txt\"")

    butacas_sala = FUNCIONES_MESA6.cargar_sala(matrizSalaVacia)
    return butacas_sala

def SALA_realizar_reserva(butacasSalaSeleccionada):
    mensajeErrorCapacidad = "La cantidad de entradas es inválida (recuerde que no puede superar la capacidad actual). Intente nuevamente"
    capacidadSala = FUNCIONES_MESA6.butacas_libres(butacasSalaSeleccionada)  #ACA DEBERIA LLAMARSE A BUTACAS LIBRES EN REALIDAD

    print(f"■ QUEDAN {capacidadSala} ASIENTOS DISPONIBLES")
    print("■ Para realizar una reserva, ingrese la cantidad de entradas que necesita")
    cantidadEntradas = UTILS_ingresar_entero_en_rango(1,capacidadSala,mensajeErrorCapacidad)

    # if cantidadEntradas == 1:
    #     FUNCIONES_MESA6.reserva(butacasSalaSeleccionada, )


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

        infoSalaSeleccionada = SALA_seleccionar(salasCine)
        butacasSalaSeleccionada = SALA_obtener_butacas(infoSalaSeleccionada)

        print(f"■ SALA \"{infoSalaSeleccionada[0]}\"")
        print("")
        FUNCIONES_MESA6.mostrar_butacas(butacasSalaSeleccionada)
        print("")

        SALA_realizar_reserva(butacasSalaSeleccionada)


main()


