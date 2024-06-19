# Segunda Práctica de Pilas asignada en la clase 8
# Implementación de una pila con objetos enlazados

from Producto import Producto
from Pila import Pila

pila = Pila()

opcion = 0
def intinput(string):
    bandera = False
    while not bandera:
        try:
            entero = int(input(string))
            bandera = True
        except ValueError:
            print("No es un entero válido")
    return entero

while opcion !=6:
    opcion= intinput("Digite la opcion que requiera: \n"
                      "1. Apilar \n"
                      "2. Desapilar \n"
                      "3. Está vacía \n"
                      "4. Mostrar el primer objeto \n"
                      "5. Ordenar de menor a mayor\n"
                      "6. Salir \n: ")
    match opcion:
        case 1:
            nombre = input("Ingrese el nombre del producto que desea apilar: ")
            precio = intinput("Ingrese el precio del producto: ")
            pila.push(Producto(nombre,precio))          
        case 2:
            print(pila.pop())
        case 3:
            if pila.esta_vacia():
                print("La pila está vacía")
            else:
                print("La pila NO está vacía")
        case 4:
            print(pila.top())
        case 5:
            pila.inOrder()
        case 6:
            print("Saliendo del programa... ")
        case _:
            print("Opción inválida")