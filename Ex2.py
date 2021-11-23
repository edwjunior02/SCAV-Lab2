import os
print(f"Ahora vamos a realizar el cálculo del histograma YUV del video cortado en el ejercicio anterior.")
print(f"Para ello vamos a utilizar el comando de ffmpeg que reproduce el video y a la vez, el histograma de los tres canales"
      f"Y, U, V.")
os.system("ffplay Resistencia_BM19_cropped.mp4 -vf split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay")


