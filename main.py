from inflect import pl_sb_C_en_ina

datos = {}

def validacion(lista_datos, buscar):
    if buscar not in lista_datos:
        return  True
    else:
        return False




def registro_datos():
    print('\t\tBienvenido a registro de informacion')
    cantidad = int(input('Ingrese el numero de repartidores del que trabjaron hoy: '))
    for tmp in range(cantidad):
       codigo = int(input('Ingrese el codigo del trabajador: '))
       # Envio las llaves y la llave a buscar para pasar al siguiente si no lo vuelve a intentar

       while True:
           if validacion(list(datos.keys()),codigo):
               break
           else:
               print('Error se encontraron datos coincidentes por favor verificar')

       while True:
           nombre = input('Ingrese el nombre: ')
           c_paquetes = int(input('Ingrese la cantidad de paquetes: '))
           zona = input('Ingrese la zona asignada para el repartidor: ')
           if nombre!=None and c_paquetes>0 and zona!=None:
               datos[codigo] = {  # Se envian todos los datos correspondientes al diccionario
                   "Nombre": nombre,
                   "Paque": c_paquetes,
                   "Zone": zona
               }
               print('Guardado con exito!!!!')
               break
           else:
               print('Por favor revisar los datos enviados debe llenar el campo nombre, paquetes mayor a 0 y zona un nombre de zona')


def mostrar_datos():
    for llave, campo in datos.items():
        print(f'Codigo del trabajador {campo[llave]}')
        print(f'Nombre trabajador: {campo["Nombre"]}')
        print(f'cantidad paquetes: {campo["Paque"]}')
        print(f'zona: {campo["Zone"]}')

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
                mostrar_datos()
            case 3:
                print('opcion 3')
            case _:
                print('Valor incorrecto vuelva a intentarlo')

    except Exception as e:
        print('Ocrrio un error inesperado')