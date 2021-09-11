## Diseño del programa

(msj bienvenido..)
pedir N y M al usuario (tamaño matriz)
armar matriz vacia con ceros [NxM] (main)
#cargar_sala(matriz)

1. "Pedir Cantidad"
2. comparo contra butacas_libres()

mostrar_butacas():

 - x x x x x x x x x 0 0 0 0 0
 - x 0 0 0 0 0 x x x x x x x x
 - x x x x x 0 0 0 x x x x x x
 - x 0 0 0 x 0 x x 0 0 x x x x

3 llamar a butacas_contiguas con la cantidad que ingresó.
Si hay, permitirle hacer una reseva macro:

        # 1.A1,A2,A3,A4,A5
        # 2.B6,B7,B8,B9,B10

Si no hay, le vas pidiendo que reserve una por una

        # -> a3, reservo
        # -> a7, reservo



## Funciones y Autor

def mostrar_butacas(matrizButacas) #| Rodri
'''mostrar grilla de butacas'''

def reservar(matrizButacas, butacaSeleccionada) #| Rami
'''reserva la butaca si esta disponible, sino devuelve false'''
    return True #true/false

def cargar_sala(matrizButacas) #| Gustavo
'''llena aleatoriamente la sala con algunas reservas (simula realidad)'''

def butacas_libres(matrizButacas) #| Eze
'''retorna cuantas butacas hay desocupadas'''
    return 0 #int

def butacas_contiguas(matrizButacas) #| Hernan
'''busca la cantidad mas larga de butacas vacias juntas y devuelve las coord'''
    return #[intX,intY]



## Funcionalidades extra
- Que el butaca contigua sepa divirse y buscar de a menos grupo
por ej, voy con 10 personas, tenes 5 y 5 contiguas

- mostrar_butacas muestre con colores las butacas contiguas
