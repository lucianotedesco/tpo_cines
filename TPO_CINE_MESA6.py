from clear_screen import clear #libreria utilizada en proceso de desarrollo para limpiar pantalla y facilitar lectura entre ejecucciones

salasCine = [
    [1,"Carlos Gardel"  ,20,30],
    [2,"Tita Merello"   ,20,30],
    [3,"Astor Piazzolla",20,30]
]

# butacasSala = [
#     0,0,0,0,0,0,0,0
#     0,0,0,0,0,0,0,0
#     0,0,0,0,0,0,0,0    
# ]

def ingresarEnteroEnRango(texto, enteroInicial, enteroFinal):
    '''Le pide al usuario ingresar un numero hasta que el mismo sea un entero, comprendido entre el rango solicitado.
       Los extremos están incluidos.'''
    while True:
        try:
            num = int(input(texto))
            if num < enteroInicial or num > enteroFinal: raise ValueError
            break
        except ValueError:
            print("!> El valor ingresado no pudo se encontrado. Por favor, ingrese un número valido")

    return num
        

def selecccionar_sala(salasCine):
    print("■ Seleccione en que sala desea realizar la reserva:")
    for sala in salasCine:
        print(f"· SALA {sala[0]} \"{sala[1]}\"")
    print("")

    numeroPrimerSala = salasCine[0][0]
    numeroUltimaSala = salasCine[len(salasCine)-1][0]
    sala = ingresarEnteroEnRango("-> ", numeroPrimerSala, numeroUltimaSala)

def inicializar_sistema():
    print("■ Iniciando SIRA: (Sistema Integral de Reserva de Asientos)")
    print("■ BIENVENIDO!     (Producto registrado a nombre de CINES DEL BARRIO S.R.L)")
    print("")
    print("")


def main():
    clear()
    inicializar_sistema()
    selecccionar_sala(salasCine)
    

main()