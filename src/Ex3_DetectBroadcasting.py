
import os
import shutil
import sys
import time
import json



#BROADCAST STANDARDS RESUME
# DVB-T ->
#   Para video tenemos MPEG2 y H.264
#   Para audio tenemos AAC, Dolby Digital (AC-3) y MP3.

# ATSC ->
#   Para video tenemos MPEG2 y H.264
#   Para audio tenemos AC-3 solo.

# DTMB ->
#   Para video tenemos AVS, AVS+, MPEG2, h.264.
#   Para audio tenemos DRA, AAC, AC-3, MP2, MP3.

# ISDB-T ->
#   Para video tenemos MPEG2 (SD channels) y H.264 (HD channels).
#   Para audio tenemos AAC
#       ISDB-Tb (Brazilian and Latam) ->
#           Para video solo H.264
#           Para audio tenemos AAC.

# Vamos a crear un diccionario JSON con todos los tipos de estándares para facilitar las comparaciones posteriores:
bs_list = {}
bs_list['broadcasting_standards'] = []
bs_list['broadcasting_standards'].append({
    'name': 'DVB-T',
    'video_codecs': ['mpeg2', 'h264'],
    'audio_codecs': ['aac', 'ac3', 'mp3']})
bs_list['broadcasting_standards'].append({
    'name': 'ATSC',
    'video_codecs': ['mpeg2', 'h264'],
    'audio_codecs': ['ac3']})
bs_list['broadcasting_standards'].append({
    'name': 'DTMB',
    'video_codecs': ['avs', 'avs+', 'mpeg2', 'h264'],
    'audio_codecs': ['dra', 'aac', 'ac3', 'mp2', 'mp3']})
bs_list['broadcasting_standards'].append({
    'name': 'ISDB-T',
    'video_codecs': ['mpeg2', 'h264'],
    'audio_codecs': ['aac']})
bs_list['broadcasting_standards'].append({
    'name': 'ISDB-Tb',
    'video_codecs': ['h264'],
    'audio_codecs': ['aac']})

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
filename = 'Resistencia_BM19_cropped.mp4'       # Aqui se debe introducir el nombre del video que se desee. Este video debe estar en la carpeta /media/ y el propio programa lo cargará en src/.
for elemento in contenidos:
    try:
        if elemento == filename:
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

# Para hacer el ejercicio, simplemente tendremos que analizar los streams de video y detectar en que estandar está.
# Luego también tendremos que analizar el audio para acabar de detectar el/los estandar/es que se podrian utilizar para
# retransmitir este archivo.

# Para realizar este ejercicio vamos a exportar ciertos datos concretos de nuestro contenedor de video.
# Estos datos nos van a servir para analizar que compatibilidades funcionan con ciertos estándares de broadcasting.
# Empezemos:
print(f"Vamos a analizar nuestro container")
os.system("ffprobe -hide_banner -v error -show_entries stream=index,codec_type,codec_name -of default=noprint_wrappers=1 -print_format json "+str(filename)+" > format.json")
time.sleep(0.5)
# Ahora tenemos los datos de nuestro archivo JSON.
# Procedemos a leerlo:
with open('format.json') as file:
    data = json.load(file)
    video_compatibilities = []
    audio_compatibilities = []
    final_compatibilities = []
    for stream in data['streams']: # FILTRAMOS POR STREAMS:
        if stream['codec_type'] == 'video': # SELECCIONAMOS LOS STREAMS DE VIDEO
            data_video_codec = stream['codec_name'] # SELECCIONAMOS EL NOMBRE DEL STREAM DE VIDEO EN ESTE CASO
            for bCast_standard in bs_list['broadcasting_standards']:    # RECORREMOS LA LISTA DE BROADCAST STANDARDS.
                bCast_video = bCast_standard['video_codecs']            # Guardamos los codecs de video del broadcast en esta iteración.
                # Ahora queremos ver si nuestro data_video_codec esta dentro de esta lista bCast_video:
                for vcodec in bCast_video:  # Recorremos cada codec de video del estándar y comparamos:
                    if vcodec == data_video_codec:
                        video_compatibilities.append(bCast_standard['name'])    # Guardamos aquellos estándares compatibles en video.
        elif stream['codec_type'] == 'audio': # SELECCIONAMOS LOS STREAMS DE AUDIO
            data_audio_codec = stream['codec_name']
            for bCast_standard in bs_list['broadcasting_standards']:    # RECORREMOS LA LISTA DE BROADCAST STANDARDS.
                bCast_audio = bCast_standard['audio_codecs']            # Guardamos los codecs de audio del broadcast en esta iteración.
                # Ahora queremos ver si nuestro data_audio_codec esta dentro de esta lista bCast_audio:
                for acodec in bCast_audio:  # Recorremos cada codec de audio del estándar y comparamos:
                    if acodec == data_audio_codec:
                        audio_compatibilities.append(bCast_standard['name'])    # Guardamos aquellos estándares compatibles en audio.
        final_compatibilities = set(video_compatibilities).intersection(audio_compatibilities)      # Seleccionamos aquellos estándares compatibles tanto en vídeo como en audio.
    if len(final_compatibilities) == 0:
        print(f"ERROR: Lo sentimos. No hemos podido detectar ningún estándarde broadcasting compatible con este formato.")
    else:
        print(f"Los estándares de broadcasting compatibles con este formato multimedia son: "+str(final_compatibilities)+".")

# ----------------------------------------------------------------------------------------------------------------------

contenidos = os.listdir(srcFolder)
for elemento in contenidos:
    try:
        if elemento.endswith(".mp4") or elemento.endswith(".json"):
            print(f"Moviendo {elemento} --> {mediaFolder} ... ", end="")
            src = os.path.join(srcFolder, elemento)  # origen
            dst = os.path.join(mediaFolder, elemento)  # destino
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




