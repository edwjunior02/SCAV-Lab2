import os
import time

def main():
      print(f"¡Bienvenido al ejercicio 2 del lab 2 de Sistemas de Codificación de Audio y Video! \U0001F61C")
      time.sleep(1)
      print(f"Ahora vamos a realizar el cálculo del histograma YUV del video cortado en el ejercicio anterior.")
      print(f"Para ello vamos a utilizar el comando de ffmpeg que reproduce el video y a la vez, el histograma de los tres canales"
            f"Y, U, V.")
      print(f"Calculando:")
      i = 0
      while i < 10:
            print(f"\U0001F37A", end="")
            i = i + 1
            time.sleep(0.2)
      print(f"¡Histogramas listos para reproducirse!")
      time.sleep(1)
      os.system("ffplay Resistencia_BM19_cropped.mp4 -vf split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay")

main()
import main
main.lab2_main()
