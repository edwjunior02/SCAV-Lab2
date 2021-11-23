# SCAV-Lab2

En este repositorio encontraremos varios scripts en Python que realizan diferentes funciones acorde al enunciado de la práctica 2 de Sistemas de Codificación de Audio y Video (SCAV). 🐥

## EJERCICIO 1:  Cortar N segundos de un video.
Para este ejercicio tomaremos el script llamado Ex1.py y el video Resistencia_BM19.mp4 adjunto en el repositorio.
Este script esta dividido en dos métodos principales:
```ruby
1. def main_Nseconds():
2. def main_improved():
```
###### 1.1 BLOQUE ESTÁNDARD: main_Nseconds()
El primer método ejecuta un bloque de código que básicamente implementa un "crop" del video en N segundos. Estos N segundos son reclamados al usuario por terminal talque:
```ruby
N = input(f"Por favor, introduce la cantidad N de segundos del principio del video que quieres recortar:")
```
Como podemos comprovar, se le pide al usuario los segundos que quiere recortar del video y estos se recortaran del comienzo del video. Es decir, el video empezará en el segundo N y el contenido previo a este frame se eliminará.

Antes de ejecutar nada, se comprueba que esta N sea un número lógico. Con esto queremos decir que N no sobrepasa la duración total del video (04:28 min - 268 segundos).
De ser así, se le pide al usuario que vuelva a introducir este valor.
```ruby
  if int(N) > 268:
      print(f"\nHas introducido un número de segundos que excede la duración del video.")
      print(f"\nPor favor, introduce un N mas pequeño que 268s (04:28min):\n")
      return main_Nseconds()
```
Una vez verificado el valor de N, se procede a cortar el video N segundos mediante FFMPEG llamado por terminal:
```ruby
str_out = ("ffmpeg -ss " + str(N) + " -i Resistencia_BM19.mp4 -vcodec copy -acodec copy Resistencia_BM19_cropped.mp4")
os.system(str_out)
```
A FFMPEG se le pasa como parámetros:
```
-ss + str(N): Básicamente nos indica el punt donde vamos a empezar el recorte del video. En este caso en el segundo N.
-i: Se indica la ruta del fichero que queremos recortar.
-vcodec copy: El video recortado mantiene el mismo codec de video que el video original.
-acodec copy: El video recortado mantiene el mismo codec de audio que el video original.
Resistencia_BM19_cropped.mp4: Nombre del video recortado.
``` 
Esta seria la parte facil. Ahora veamos la parte mas interesante 😈
###### 1.2 BLOQUE MEJORADO: main_improved()
En este bloque hemos mejorado la versión estándar y simple de recortar un video a partir de N segundos como entrada de usuario.
Para ello, hemos decidido que el usuario permita escoger desde que momento inicial hasta que momento final desea recortar el video(algo más útil en la mayoria de situaciones).
En el siguiente bloque de código, se le pide al usuario que entre el inicio y el final del crop:
```ruby
print(f"Por favor introduce en formato 'horas:minutos:segundos', el momento que quieras iniciar el corte:")
init = input()
init = extract_time(init)
print(f"Muy bien, ahora introduce en formato 'horas:minutos:segundos', el momento que quieras terminar el corte")
out = input()
out = extract_time(out)
```
La función: ```extract_time(init/out)```, nos comprueba si el formato introducido es correcto y lógico.
Con esto de lógico queremos decir que respeta la duración del video y los estándares de tiempo (una hora son 60 minutos y un minuto son 60 segundos).
Y finalmente se llama a FFMPEG para que realize el crop en el intérvalo de tiempo introducido por el usuario:
```ruby
str2_out = ("ffmpeg -i Resistencia_BM19.mp4 -ss " + str(init) + " -to " + str(out) + " -c copy Resistencia_BM19_cropped_2.mp4")
os.system(str2_out)
```
Como en el subapartado anterior, el bloque ```-c copy Resistencia_BM19_cropped_2.mp4``` copia tanto los codecs de audio cmo los de video del fichero original en el fichero recortado, sin transcodificar.

## EJERCICIO 2: Histograma YUV
Para este ejercicio, no hemos mareado mucho la perdiz. FFMPEG es una herramienta muy potente que permite hacer prácticamente cualquier tipo de manipulación, codificación o transformación de archivos de audio y video. Una de sus funcionalidades es generar histogramas YUV de ciertos fotogramas y hacer un 'overlay' para que se vea tanto la secuencia de frames (es decir, el video) como la secuencia de histogramas (es decir, una especie de video de histogramas).
En el script ```Ex2.py```utilizaremos el video recortado del ejercicio anterior. El bloque que se lanza desde terminal utilizando FFMPEG es:
```ruby
os.system("ffplay Resistencia_BM19_cropped.mp4 -vf split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay")
```
Esto genera un overlay entre los histogramas de cada canal Y,U,V y el video en si:

![Captura de pantalla 2021-11-23 a las 22 20 50](https://user-images.githubusercontent.com/91899380/143131022-95cd069d-90a8-483a-8f4e-7eb5be5fd166.png)

## EJERCICIO 3: Cambio de resolución
En el siguiente ejercicio, hemos creado un script llamado ```Ex3.py```, que básicamente modifica la resolución del video. Así de facil.
Para que sea mas agradable, se ha creado un menú básico y simple en el que se le pedirá al usuario una de las opciones disponibles que representan cada una de las diferentes resoluciones a las que se puede cambiar:

![Captura de pantalla 2021-11-23 a las 22 24 37](https://user-images.githubusercontent.com/91899380/143131532-b9f7159f-e84c-446d-86f8-74c5874f3ad6.png)

En este menú se le da al usuario 5 opciones entre las cuales solo podrá esoger 1. Esta opción seleccionada será almacenada en la variable ```res```y según el valor de esta variable, se ejecutará el bloque que implemente FFMPEG hacia la terminal:
```ruby
os.system("ffmpeg -i Resistencia_BM19_cropped.mp4 -vf scale=____:____ videos/[720p]Resistencia_BM19_cropped.mp4")
```
La parte mas importante de la línea de código anterior, es la parte del ```-vf scale=____:_____```, que es la que se encarga de cambiar la resolución del video.
Si por ejemplo, el usuario seleccionara la opción ```1. 720p:```el comando ffmpeg correspondiente sería ```-vf scale=1280:720```.

## EJERCICIO 4: DE ESTÉREO A MONO
Este script, básicamente nos cambia los canales de audio de nuestro video (estéreo) y los agrupa en uno solo (mono). Para ello utiliza la siguiente comanda:
```ruby
os.system("ffmpeg -i Resistencia_BM19.mp4 -ac 1 Resistencia_BM19_mono.mp4")
```
En el que podemos ver que bloque de código que genera este cambio es ```-ac 1```, que nos contrae el audio en un único canal de salida.

## MENÚ PRINCIPAL (MAIN)
Y por último pero no menos importante, tenemos un último script llamado ```main.py```, que básicamente tiene un menú interactivo en el que se plantean todas las opciones posibles para ejecutar el programa. En la siguiente imagen podemos ver el menú que aparece por consola:

![Captura de pantalla 2021-11-23 a las 23 57 13](https://user-images.githubusercontent.com/91899380/143142020-ec36583e-6612-4834-ae3f-0e43ad0148f7.png)

Las decisiones se valoran en un bucle ```while``` donde dependiendo de la opción tomada por el usuario se llama al script correspondiente.
```ruby
while aux == 0:
    if ex == '1':
        import Ex1
        Ex1.main()
```
Y cada script contiene una llamada a su vez al método ```main()```del script principal ```main.py```, de manera que se llama recursivamente a este menú hasta que se elija la opción ```5. Salir del programa:```.
Esta opción volverá a pedir si se desea finalmente salir del programa que: 
```
En caso negativo, se llamará de nuevo al menú (bucle while) i volveremos a empezar.
En caso afirmativo, se llamará a sys.exit() que cerrara por completo el programa.
````
Eso es todo. 
Muchas gracias y disfruten del programa 😆







