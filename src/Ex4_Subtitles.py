import os
import time
import shutil

# Nuestra línea de comando de FFMPEG solo lee imágenes que estén en el mismo directorio que el script en el que se lance la petición.
#Para ello, haremos una copia de media/Resistencia_BM19_cropped_2.mp4 y la pasaremos al directorio src/.
#Aquí debe introducir el directorio
srcFolder = ("/Users/edwjunior/Documents/UNIVERSIDAD/4o CURSO/1r TRIMESTRE/SISTEMES DE CODIFICACIÓ D'ÀUDIO I VIDEO"
                "/SEMINARS/SEMINAR 2/src")
mediaFolder = ("/Users/edwjunior/Documents/UNIVERSIDAD/4o CURSO/1r TRIMESTRE/SISTEMES DE CODIFICACIÓ D'ÀUDIO I VIDEO"
                "/SEMINARS/SEMINAR 2/media")

if not os.path.isdir(mediaFolder):
    print('la primera carpeta no existe')
elif not os.path.isdir(srcFolder):
    print('la segunda carpeta no existe')


contenidos = os.listdir(mediaFolder)
filename = 'Resistencia_BM19.mp4'       # Aqui se debe introducir el nombre del video que se desee. Este video debe estar en la carpeta /media/ y el propio programa lo cargará en src/.
for elemento in contenidos:
    try:
        if elemento == filename or elemento.endswith(".srt"):
            print(f"Copiando {elemento} --> {srcFolder} ... ", end="")
            src = os.path.join(mediaFolder, elemento)  # origen
            dst = os.path.join(srcFolder, elemento)  # destino
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

os.system("ffmpeg -i "+str(filename)+" -vf subtitles=subtitles_resistencia.srt Resistencia_BM19_Spanish_subtitulado.mp4")

# ----------------------------------------------------------------------------------------------------------------------