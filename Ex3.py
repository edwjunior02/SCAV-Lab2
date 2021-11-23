import os
import sys
import time

print(f"Bienvenido al ejercicio 3!")
print(f"Ahora vamos a proceder a cambiar de resolución nuestro video de la resistencia \U0001F61D")
aux = True
while aux == True:
    print(f"Selecciona la resolución que desea aplicar al video:")
    print(f"....................................")
    print(f". 1. 720p:                         .")
    print(f". 2. 480p:                         .")
    print(f". 3. 360x240:                      .")
    print(f". 4. 160x120:                      .")
    print(f".                                  .")
    print(f". 5. Quiero pirarme de aqui:       .")
    print(f"....................................")
    res = input()
    if res == '5':
        option = input(f"Estas seguro que desea salir del programa? \U0001F62D [y/n]")
        if option == 'y':
            aux = False
            sys.exit()
        else:
            continue
    elif res == '1':
        print(f"Convirtiendo a 720p:")
        i = 0
        while i < 10:
            print(f"\U0001F37A", end="")
            i = i + 1
            time.sleep(0.2)
        os.system("ffmpeg -i Resistencia_BM19_cropped.mp4 -vf scale=1280:720 videos/[720p]Resistencia_BM19_cropped.mp4")
        print(f"¡Convertido correctamente!")
        continue

    elif res == '2':
        print(f"Convirtiendo a 480p:")
        i = 0
        while i < 10:
            print(f"\U0001F37A", end="")
            i = i + 1
            time.sleep(0.2)
        os.system("ffmpeg -i Resistencia_BM19_cropped.mp4 -vf scale=720:480 videos/[480p]Resistencia_BM19_cropped.mp4")
        print(f"¡Convertido correctamente!")
        continue

    elif res == '3':
        print(f"Convirtiendo a 360x240:")
        i = 0
        while i < 10:
            print(f"\U0001F37A", end="")
            i = i + 1
            time.sleep(0.2)
        os.system("ffmpeg -i Resistencia_BM19_cropped.mp4 -vf scale=360:240 videos/[360x240]Resistencia_BM19_cropped.mp4")
        print(f"¡Convertido correctamente!")
        continue

    elif res == '4':
        print(f"Convirtiendo a 160x120:")
        i = 0
        while i < 10:
            print(f"\U0001F37A", end="")
            i = i + 1
            time.sleep(0.2)
        os.system("ffmpeg -i Resistencia_BM19_cropped.mp4 -vf scale=160:120 videos/[160x120]Resistencia_BM19_cropped.mp4")
        print(f"¡Convertido correctamente!")
        continue



