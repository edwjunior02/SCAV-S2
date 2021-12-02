import os.path
import time
import shutil

# Nuestra línea de comando de FFMPEG solo lee imágenes que estén en el mismo directorio que el script en el que se lance la petición.
#Para ello, haremos una copia de media/Resistencia_BM19_cropped_2.mp4 y la pasaremos al directorio src/.
pathCarpeta = ("/Users/edwjunior/Documents/UNIVERSIDAD/4o CURSO/1r TRIMESTRE/SISTEMES DE CODIFICACIÓ D'ÀUDIO I VIDEO"
               "/LABS/LAB2-VideoPart")
pathCarpeta2 = ("/Users/edwjunior/Documents/UNIVERSIDAD/4o CURSO/1r TRIMESTRE/SISTEMES DE CODIFICACIÓ D'ÀUDIO I VIDEO"
                "/SEMINARS/SEMINAR 2/src")
pathCarpetaDest = ("/Users/edwjunior/Documents/UNIVERSIDAD/4o CURSO/1r TRIMESTRE/SISTEMES DE CODIFICACIÓ D'ÀUDIO I VIDEO"
                "/SEMINARS/SEMINAR 2/media")

if not os.path.isdir(pathCarpeta):
    print('la primera carpeta no existe')
elif not os.path.isdir(pathCarpeta2):
    print('la segunda carpeta no existe')
elif not os.path.isdir(pathCarpetaDest):
    print('la tercera carpeta no existe')

contenidos = os.listdir(pathCarpeta)
for elemento in contenidos:
    try:
        if elemento == 'Resistencia_BM19_cropped.mp4':
            print(f"Copiando {elemento} --> {pathCarpeta2} ... ", end="")
            src = os.path.join(pathCarpeta, elemento)  # origen
            dst = os.path.join(pathCarpeta2, elemento)  # destino
            shutil.copy(src, dst)
            time.sleep(2)
            print("Correcto")
        else:
            continue
    except:
        print("Falló")
        print("Error, no se pudo copiar el archivo. Verifique los permisos de escritura")

print(f"Se han importado los archivos correctamente.")
time.sleep(2)

# CORE DEL EJERCICIO:---------------------------------------------------------------------------------------------------

print(f"1. Recortando el video al primer minuto...")
os.system("ffmpeg -ss 60 -i Resistencia_BM19_cropped.mp4 -vcodec copy -acodec copy Resistencia_MP4_Container.mp4") # Recorta los primeros 60 segundos del video.
time.sleep(2)
print(f"¡Recortado correctamente!")
aux = True
print(f"Genial. Ahora vamos a crear un container MP4 que tenga diferentes tracks de audio.")
while aux == True:
    count = 0
    print(f"Selecciona el codec de audio que quieres asignar al nuevo track del container:")
    print(f"....................................")
    print(f". 1. MP3:                          .")
    print(f". 2. AAC:                          .")
    print(f". 3. WAV:                          .")
    print(f". 4. FLAC:                         .")
    print(f".                                  .")
    print(f". 5. No quiero asignar nada:       .")
    print(f"....................................")
    res = input()
    if res == '1':
        print(f"Has decidido codificar el nuevo audio track en formato MP3.")
        print(f"Añadiendo codec MP3 al container:")
        i = 0
        while i < 10:
            print(f"\U0001F37A", end="")
            i = i + 1
            time.sleep(0.2)
        # os.system("ffmpeg -i Resistencia_MP4_Container.mp4 -c:v copy -map 0:0 -c:a copy -map 0:1 -c:a mp3 -b:a 320k -ac 2 -sn -map 0:2 Resistencia_MP4_Container.mp4")
        os.system("ffmpeg -i Resistencia_MP4_Container.mp4 -c:a mp3 -b:a 320k -ac 2 -sn -vn Resistencia_audio.mp3")
        os.system("ffmpeg -i Resistencia_MP4_Container.mp4 -i Resistencia_audio.mp3 -map 0:v -c:v copy -map 1:a -c:a copy -map 0:a -c:a copy Resistencia_MP4_Container_MP3.mp4")
        print(f"¡Convertido correctamente!")
        time.sleep(1)
        count += 1
        continue
    elif res == '2':
        print(f"Has decidido codificar el audio en formato AAC.")
        print(f"Convirtiendo a AAC:")
        i = 0
        while i < 10:
            print(f"\U0001F37A", end="")
            i = i + 1
            time.sleep(0.2)
        # os.system("ffmpeg -i Resistencia_BM19_cropped.mp4 -c:a libfdk_aac -profile:a aac_he_v2 -b:a 20k -ar 44100 -ac 2 Resistencia_BM19_cropped.m4a")
        os.system("ffmpeg -i Resistencia_BM19_cropped.mp4 -vn -acodec aac Resistencia_BM19_cropped.aac")
        print(f"¡Convertido correctamente!")
        time.sleep(1)
        count += 1
        continue
    elif res == '3':
        print(f"Has decidido codificar el audio en formato WAV.")
        print(f"Convirtiendo a WAV:")
        i = 0
        while i < 10:
            print(f"\U0001F37A", end="")
            i = i + 1
            time.sleep(0.2)
        os.system("ffmpeg -i Resistencia_BM19_cropped.mp4 -ac 2 Resistencia_BM19_cropped.wav")
        print(f"¡Convertido correctamente!")
        time.sleep(1)
        count += 1
        continue
    elif res == '4':
        print(f"Has decidido codificar el audio en formato FLAC.")
        print(f"Convirtiendo a FLAC:")
        i = 0
        while i < 10:
            print(f"\U0001F37A", end="")
            i = i + 1
            time.sleep(0.2)
        os.system("ffmpeg -i Resistencia_BM19_cropped.mp4 -c:a flac -compression_level 12 Resistencia_BM19_cropped.flac")
        print(f"¡Convertido correctamente!")
        time.sleep(1)
        count += 1
        continue
    elif res == '5':
        option = input(f"Estas seguro que desea salir del programa? \U0001F62D [y/n]")
        if option == 'y':
            aux = False
            continue
        else:
            aux = True
            continue
    else:
        print(f"La opción introducida no es correcta!")
        continue

# ----------------------------------------------------------------------------------------------------------------------
contenidos = os.listdir(pathCarpeta2)
for elemento in contenidos:
    try:
        if elemento.startswith("Resistencia_") or elemento.endswith(".mp4"):
            print(f"Moviendo {elemento} --> {pathCarpetaDest} ... ", end="")
            src = os.path.join(pathCarpeta2, elemento)  # origen
            dst = os.path.join(pathCarpetaDest, elemento)  # destino
            shutil.move(src, dst)       # Ahora utilizamos move en vez de copy, ya que lo queremos mover de aquí.
            time.sleep(2)
            print("Correcto")
        else:
            continue
    except:
        print("Falló")
        print("Error, no se pudo copiar el archivo. Verifique los permisos de escritura")

time.sleep(2)
print(f"Se han movido los archivos correctamente.")