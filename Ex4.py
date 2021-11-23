import os.path

print(f"Selecciona el codec de video que desee:")
print(f"...........................................")
print(f". 1. MP4:                                 .")
print(f". 2. DIVX:                                .")
print(f". 3. H.264:                               .")
print(f". 4. H.265/HEVC:                          .")
print(f". 5. AVI:                                 .")
print(f". 6. No quiero cambiar el codec de video: .")
print(f"...........................................")
vcodec_label = input()
if vcodec_label == '6':
    vcodec = 'copy'
elif vcodec_label == '1':
    vcodec = '.mp4'
elif vcodec_label == '2':
    vcodec = '.divx'
elif vcodec_label == '3':
    vcodec = '.h264'
elif vcodec_label == '4':
    vcodec = '.h265'
elif vcodec_label == '5':
    vcodec = '.avi'

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
    acodec = '.mp3'
elif acodec_label == '2':
    acodec = '.wma'
elif acodec_label == '3':
    acodec = '.wav'
elif acodec_label == '4':
    acodec = '.aiff'
elif acodec_label == '5':
    acodec = '.flac'

os.system("ffmpeg -i Resistencia_BM19.mp4 -acodec "+str(acodec)+" -vcodec "+str(vcodec)+" Resistencia_BM19."+str(vcodec)+"")
