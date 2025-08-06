from inflect import pl_sb_C_en_ina

datos = {}

def registro_datos():
    print('\t\tBienvenido a registro de informacion')
    cantidad = int(input('Ingrese el numero de repartidores del que trabjaaron hoy: '))
    for tmp in range(cantidad):
       codigo = int(input('Ingrese el codigo del trabajador: '))
       nombre = input('Ingrese el nombre: ')
       c_paquetes = int(input('Ingrese la cantidad de paquetes: '))
       zona = input('Ingrese la zona asignadaa para el repartidor: ')
       datos[codigo]={ #Se envian todos los datos correspondientes al diccionario
           "Nombre" : nombre,
           "Cantidad_p" : c_paquetes,
           "Zone" : zona
       }



fin_menu = True

while fin_menu:
    try:
        print('\t\t===Bienvenido admin===:')
        print('1.Registro de datos\n2.Ordenamiento de datos\n3.Salir')
        opcion = int(input('Ingrese la opcion que desea ingresar: '))
        match opcion:
            case 1:
                registro_datos()
            case 2:
                print('opcion 2')
            case 3:
                print('opcion 3')
            case _:
                print('Valor incorrecto vuelva a intentarlo')

    except Exception as e:
        print('Ocrrio un error inesperado')