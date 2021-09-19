import math
import FUNCIONES_MESA6
from os import system

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

def UTILS_transformar_butaca_en_coordenada(numeroButaca, salaSeleccionada):
    '''Devuelve la coordenada en la matriz de butacas de la sala que corresponde al numero del asiento ingresado'''
    longitudFilas = int(salaSeleccionada[2])

    fila = math.floor(numeroButaca / longitudFilas)
    columna = numeroButaca % longitudFilas
    return fila, columna         

def UTILS_transformar_coordenada_en_butaca(fila, columna, cantidadColumnas):
    '''Devuelve el numero de butaca correspondiente a la coordenada recibida de la matriz de asientos de la sala'''
    numeroButaca = (fila * cantidadColumnas) + columna
    return numeroButaca



# ------------- SALAS

def SALA_seleccionar(salasCine):
    '''Permito que el usuario seleccione una sala, y devuelvo el registro correspondiente'''

    print("■ Seleccione en que sala desea realizar la reserva:")
    for index, sala in enumerate(salasCine):
        print(f"· SALA {index + 1} \"{sala[0]}\"")
    print("")

    #obtenemos el rango de salas posibles para poder llamar a ingresar_entero    
    numeroPrimerSala = 1
    numeroUltimaSala = len(salasCine)
    mensajeErrorSalaNoEncontrada = "La sala ingresada no fue encontrada, intente nuevamente"
    indiceSala = UTILS_ingresar_entero_en_rango(numeroPrimerSala, numeroUltimaSala, mensajeErrorSalaNoEncontrada)

    return salasCine[indiceSala - 1]

def SALA_obtener_butacas(registroSalaSeleccionada):
    '''Obtenemos una matriz representando la ocupación de las butacas en la sala, y la anexamos al registro de sala recibido.'''

    try:
        matrizSalaVacia = MATRIZ_crear(registroSalaSeleccionada[1],registroSalaSeleccionada[2])
    except IndexError:
        print("!> No se pudo obtener la información completa de las salas, por favor revise la estructura del archivo \"salas.txt\"")

    #simulamos el llenado de butacas utilizando cargar_sala y anexamos dicha matriz de butacas para tener un solo registro que consumir
    butacas_sala = FUNCIONES_MESA6.cargar_sala(matrizSalaVacia)
    registroSalaSeleccionada.append([])
    registroSalaSeleccionada[3] = butacas_sala

def SALA_mayor_cantidad_butacas_contiguas(salaSeleccionada):
    '''Devuelve la mayor cantidad de butacas contiguas que se encuentren en toda la la sala, no solo en una fila particular'''

    #iteramos el llamado de butacas_contiguas para buscar el mayor espacio disponible en la sala
    mayorCantidadButacasJuntas = 0
    for fila in range(int(salaSeleccionada[1])):
        columna,cantidadButacas = FUNCIONES_MESA6.butacas_contiguas(salaSeleccionada[3], fila)
        if cantidadButacas > mayorCantidadButacasJuntas:
            mayorCantidadButacasJuntas = cantidadButacas
            filaButacaContigua = fila
            columnaButacaContigua = columna
   
    return filaButacaContigua, columnaButacaContigua, mayorCantidadButacasJuntas 



# ------------- RESERVAS

def RESERVA_intentar_reserva_individual(salaSeleccionada):
    '''Intentamos reservar un asiento en particular'''

    butacas = salaSeleccionada[3]

    print("■ Digite la posición de la butaca deseada:")   
    totalButacasSala = int(salaSeleccionada[1]) * int(salaSeleccionada[2])
    mensajeErrorCapacidad = "La posición ingresada no existe en la sala"
    butacaElegida = UTILS_ingresar_entero_en_rango(0,totalButacasSala,mensajeErrorCapacidad)

    fila,columna = UTILS_transformar_butaca_en_coordenada(butacaElegida, salaSeleccionada)    
    reservaRealizada = FUNCIONES_MESA6.reservar(butacas,fila,columna)
    system('cls')
    FUNCIONES_MESA6.mostrar_butacas(butacas)

    if not (reservaRealizada):        
        print("!> La butaca que intentó reservar ya se encuentra ocupada")
    else:
        print("■ RESERVADA!")

    return reservaRealizada

def RESERVA_realizar_reserva_multiple(salaSeleccionada, fila, columnaInicial, cantidadReservas):
    '''Inicia la reserva multiple de entradas iterando sobre el metodo de reserva convencional'''
    butacas = salaSeleccionada[3]
    columna = columnaInicial

    for reserva in range(cantidadReservas):            
        #no me interesa evaluar si la reserva fue realizada ya que butacas_contiguas me aseguró antes que esos lugares estan disponibles
        #si el sistema se ejecutara en varios equipos y editaran una misma base/archivo, si deberia cotejar.
        FUNCIONES_MESA6.reservar(butacas,fila,columna)
        columna += 1      

def RESERVA_iniciar_reservacion(salaSeleccionada):
    '''Realizamos la reserva de butacas en la sala recibida, obteniendo del usuario la cantidad de entradas que desea'''
    butacas = salaSeleccionada[3] #obtenemos la matriz en una variable de butacas para mayor legibilidad
    capacidadSala = FUNCIONES_MESA6.butacas_libres(butacas)
        
    #obtenemos la cantidad de entradas que desea el usuario
    print(f"■ QUEDAN {capacidadSala} ASIENTOS DISPONIBLES")
    print("■ Para realizar una reserva, ingrese la cantidad de entradas que necesita")
    mensajeErrorCapacidad = "La cantidad de entradas es inválida (recuerde que no puede superar la capacidad actual). Intente nuevamente"
    cantidadEntradas = UTILS_ingresar_entero_en_rango(1,capacidadSala,mensajeErrorCapacidad)
    
    #el sistema busca butacas contiguas para sugerir si se solicitan 2 o mas entradas

    #primero obtiene las coordenadas de lugares juntos, de acuerdo a la cantidad
    filaButacaContigua,columnaButacaContigua,cantidadButacas  = SALA_mayor_cantidad_butacas_contiguas(salaSeleccionada)
    #luego transformaa esas coordenadas en la butaca, a fin de informar al usuario la posición de manera mas amigable
    numeroButaca = UTILS_transformar_coordenada_en_butaca(filaButacaContigua, columnaButacaContigua, int(salaSeleccionada[2]))

    resevaMultipleRealizada = False
    if (cantidadEntradas > 1):        
        if (cantidadButacas >= cantidadEntradas):
            print("")
            print(f"■ SUGERENCIA DE RESERVA: Puede reservar las {cantidadEntradas} juntas, desde la {numeroButaca} a la {numeroButaca + cantidadEntradas - 1}.")
            print(f"■ Digite \"R\" para llevar a cabo la reserva. Caso contrario, pulse cualquier tecla")
            respuestaUsuario = input("> ")
            if (respuestaUsuario.lower() == "r"):            
                RESERVA_realizar_reserva_multiple(salaSeleccionada, filaButacaContigua, columnaButacaContigua, cantidadEntradas)
                resevaMultipleRealizada = True            
                system('cls')
                reservaRealizada = FUNCIONES_MESA6.mostrar_butacas(butacas)

    if not resevaMultipleRealizada:
        print("")
        print("■ INICIANDO RESERVA MANUAL:")
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

    print("")
    print("■ RESERVA/S FINALIZADAS! Se lo redigirá al sistema de facturación... Pulse una tecla para continuar­")
    input("")


# ------------- SISTEMA

def SISTEMA_carga_inicial():
    '''Muestro los mensajes de inicio del sistema y obtengo la sala (junto a sus butacas) en la cual quiero realizar la reserva'''

    system('cls')     
    print("■ Iniciando SIRA: (Sistema Integral de Reserva de Asientos)")
    print("■ BIENVENIDO!     (Producto registrado a nombre de CINES DEL BARRIO S.R.L)")
    print("")
    print("")

    salasCine = MATRIZ_crear(3,5)
    ARCHIVO_cargar_salas(salasCine)

    salaSeleccionada = SALA_seleccionar(salasCine)
    SALA_obtener_butacas(salaSeleccionada)

    system('cls')
    print(f"■ SALA \"{salaSeleccionada[0]}\"")
    return salaSeleccionada




# --------------------------------
# ------------- PROGRAMA PRINCIPAL

# ESTRUCTURA DEL REGISTRO DE SALA:

# salaSeleccionada[0] = Nombre de la sala
# salaSeleccionada[1] = Filas de butacas que posee
# salaSeleccionada[2] = Columnas de butacas que posee
# salaSeleccionada[3] = Matriz donde se puede visualizar el estado actual de reservas

def main():
    salaSeleccionada = SISTEMA_carga_inicial()   
    butacas = salaSeleccionada[3] 
    FUNCIONES_MESA6.mostrar_butacas(butacas)
    RESERVA_iniciar_reservacion(salaSeleccionada)

main()