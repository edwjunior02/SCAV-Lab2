
import sys
import time

def lab2_main():
    print(f"Bienvenido al LAB 1 de Sistemas de Codificación de Video.")
    print("A continuación te mostraremos el listado de ejercicios disponibles en este lab:")
    print(f"....................................")
    print(f". 1. Cortar N segundos de un video:.")
    print(f". 2. Histograma YUV:               .")
    print(f". 3. Cambio de resolución:         .")
    print(f". 4. De estéreo a mono:            .")
    print(f".                                  .")
    print(f". 5. Salir del programa:           .")
    print(f"....................................")
    ex = input("¿Que ejercicio quieres ejecutar...?")
    if ex == '5':
        option = input(f"Estas seguro que desea salir del programa? \U0001F97A [y/n]")
        if option == 'y':
            sys.exit()
        else:
            return lab2_main()
    else:
        aux = 0
        while aux == 0:
            if ex == '1':
                import Ex1
                Ex1.main()
            elif ex == '2':
                import Ex2
                Ex2.main()
            elif ex == '3':
                import Ex3
                Ex3.main()
            elif ex == '4':
                import Ex4
                Ex4.main()
            else:
                time.sleep(1)
                print("\nNúmero de ejercicio incorrecto \U00002620. Introduce uno de las 5 opciones disponibles:')\n")
                return lab2_main()


lab2_main()
sys.exit()

