import os.path
import time

def main():
    print(f"¡Bienvenido al ejercicio 4 del lab 2 de Sistemas de Codificación de Audio y Video! \U0001F61C")
    print(f"Primero de todo vamos a codificar el sonido de un video y extraerlo en un único canal (mono):")
    print(f"Convirtiendo a mono:")
    i = 0
    while i < 10:
        print(f"\U0001F37A", end="")
        i = i + 1
        time.sleep(0.2)
    os.system("ffmpeg -i Resistencia_BM19.mp4 -ac 1 Resistencia_BM19_mono.mp4")
    print(f"Convertido correctamente!")

    #NO FUNCIONA!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    '''
    print(f"Genial! Ahora selecciona el codec de audio que desee:")
    print(f"...........................................")
    print(f". 1. MP3                                  .")
    print(f". 2. WMA:                                 .")
    print(f". 3. WAV:                                 .")
    print(f". 4. AIFF:                                .")
    print(f". 5. FLAC:                                .")
    print(f". 6. No quiero cambiar el codec de audio: .")
    print(f"...........................................")
    acodec_label = input()
    if acodec_label == '6':
        acodec = 'copy'
    elif acodec_label == '1':
        acodec = 'mp3'
    elif acodec_label == '2':
        acodec = 'wma'
    elif acodec_label == '3':
        acodec = 'wav'
    elif acodec_label == '4':
        acodec = 'aiff'
    elif acodec_label == '5':
        acodec = 'flac'

    os.system("ffmpeg -i Resistencia_BM19_mono.mp4 -acodec "+str(acodec)+" -vcodec copy Resistencia_BM19_"+str(acodec)+".mp4")
    '''
main()
import main
main.lab2_main()