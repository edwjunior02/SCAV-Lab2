import os.path
import time
from os import remove
from datetime import datetime

def main_Nseconds():
    # Comprovar si existen los outputs para evitar sobreescribir:
    if os.path.isfile('Resistencia_BM19_cropped.mp4'):
        remove('Resistencia_BM19_cropped.mp4')

    # Comenzemos con el ejercicio
    print(f"¡Bienvenido al ejercicio 1 del lab 2 de Sistemas de Codificación de Audio y Video! \U0001F61C")
    print(f"En este ejercicio vamos a proceder a recortar un video en N segundos")
    print(f"IMPORTANTE: EL VIDEO SOLO DURA 04:28 min.")
    N = input(f"Por favor, introduce la cantidad N de segundos del principio del video que quieres recortar:")

    # COMPROVACIÓN N
    if int(N) > 268:
        print(f"\nHas introducido un número de segundos que excede la duración del video.")
        print(f"\nPor favor, introduce un N mas pequeño que 268s (04:28min):\n")
        return main_Nseconds()

    print(f"Recortando:")
    i = 0
    while i < 10:
        print(f"\U0001F37A", end="")
        i = i + 1
        time.sleep(0.2)

    str_out = ("ffmpeg -ss " + str(N) + " -i Resistencia_BM19.mp4 -vcodec copy -acodec copy Resistencia_BM19_cropped.mp4")
    os.system(str_out)
    print(f"¡Video recortado correctamente!")
    time.sleep(0.5)
    print(f"Muy poco interesante verdad...?")
    time.sleep(2)
    print(f"Vamos a complicarlo un poco mas:")


def main_improved():

    # Comprovar si existen los outputs para evitar sobreescribir:
    if os.path.isfile('Resistencia_BM19_cropped_2.mp4'):
        remove('Resistencia_BM19_cropped_2.mp4')

    print(f"Por favor introduce en formato 'horas:minutos:segundos', el momento que quieras iniciar el corte:")
    init = input()
    init = extract_time(init)
    print(f"Muy bien, ahora introduce en formato 'horas:minutos:segundos', el momento que quieras terminar el corte")
    out = input()
    out = extract_time(out)

    print(f"Se recortará el video desde:"+str(init)+" hasta "+str(out)+". Desea continuar? [y/n]")
    resp = input()

    if resp == 'y':
        print(f"Recortando:")
        i = 0
        while i < 10:
            print(f"\U0001F37A", end="")
            i = i + 1
            time.sleep(0.2)
        str2_out = ("ffmpeg -i Resistencia_BM19.mp4 -ss " + str(
            init) + " -to " + str(
            out) + " -c copy Resistencia_BM19_cropped_2.mp4")
        os.system(str2_out)
        print(f"¡Video recortado correctamente!")
    else:
        return main_improved()
def extract_time(string):
    #Pasamos a enteros para manipular y operar con ellos.
    h = string[0:2]
    hour = int(h)
    m = string[3:5]
    minute = int(m)
    s = string[6:8]
    second = int(s)

    while hour > 0 or minute > 4 or second > 59:
        if hour > 0:
            hour = 0
            print(f"Se ha introducido una hora que no es correcta. El valor de hora se reseteará a 0: horas = "+str(hour)+".")

        if minute > 4:
                minute = minute % 4
                print(f"Se ha introducido una hora que no es correcta. El valor de minutos se reseteará dentro del rango [0,4]. "
                      f"Su valor quedará como: 0"+str(hour)+":0"+str(minute)+":"+str(second)+".")

        if second > 60:
            c, r = divmod(second, 60)  #Para que los segundos esten entre 0 y 59. En c se guarda el cociente y en r se guarda el resto.
            minute = minute + c
            second = r
            print(f"Se ha introducido una hora que no es correcta. El valor de segundos es superior a 60. "
                  f"Se sumarán "+str(c)+"minutos y finalmente su valor quedara como: "+str(hour)+":"+str(minute)+":"+str(second)+".")

    #Convertimos a string el resultado final
    output = ("0"+str(hour)+":0"+str(minute)+":"+str(second))
    return output
def main():
    main_Nseconds()
    print(f"Quiere mejorar el resultado?[y/n]")
    resp = input()
    if resp == 'y':
        main_improved()
        import main
        main.lab2_main()
    else:
        import main
        main.lab2_main()

main()


