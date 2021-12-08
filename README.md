# SCAV-S2
#### Eduard Puig - 194161

### EJERCICIO 1: 
En este primer ejercicio, se nos pide exportar un video en el que se puedan visualizar los vectores de movimiento y los macroblocks.
Para ello, la herramienta ffmpeg nos brinda gran ayuda ya que hay ciertas funciones que nos permiten exportar el campo vectorial de movimento e integrarlo en el video original.
El bloque de código que genera este formato es el siguiente:
```ruby
os.system("ffmpeg -flags2 +export_mvs -i Resistencia_BM19_cropped_2.mp4 -vf codecview=mv=pf+bf+bb Resistencia_mvs.mp4")
```
En este bloque de código, podemos ver como mediante ```+export_mvs``` y ```codecview=mv=pf+bf+bb```, conseguimos extraer el mapa vectorial de movimiento a partir de las predicciones de los vectores de movimiento de frames B y P.
También tenemos que destacar que cada vector tiene su origen en el centro de un macroblock. Por lo tanto, se genera una distribución de macroblocs uniforme (tienen todos el mismo tamaño).
En la siguiente imagen se muestra el resultado obtenido al ejecutar este script:

![motionvectors](https://user-images.githubusercontent.com/91899380/145307320-116b0817-ad40-41c9-be25-2e685bb674dd.png)

### EJERCICIO 2: MP4 CONTAINER
Para empezar, tenemos que crear un contenedor ```MP4``` que nos almacene diferentes tracks de audio y video.
Si tomamos nuestro video ```Resistencia_BM19_cropped.mp4``` como muestra, lo tenemos que añadir a un contenedor que:
```
- El video tenga una duración de 1 minuto.
- Tenga un track/stream MP3 estéreo.
- Tenga otro track/stream AAC con menor bitrate.
```
Primero tenemos que analizar las propiedades y componentes de nuestro video muestra. Para ello hemos hecho un
diagrama que representa nuestro video:

![ResistenciaMP4-Container](https://user-images.githubusercontent.com/91899380/144336574-d05794b0-0974-4ff1-9f40-96a73edaa4d0.png)

Y queremos convertirlo en un contenedor con estas características:

![NewContainerMP4](https://user-images.githubusercontent.com/91899380/144336594-2697ce21-8114-4fb8-828f-b205d6d0b913.png)

Precisamente con ```ffmpeg``` podemos conseguir copiar cierta información de un contenedor a otro y añadir lo que nos falta.
Primero vamos a quedarnos con solo el primer minuto del video ```Resistencia_BM19_cropped.mp4``` por razones de espacio, y vamos a copiar toda la información de este video a un nuevo container mp4 
a que llamaremos ```Resistencia_MP4_Container.mp4```.

Debido a que ```ffmpeg``` no puede sobreescribir el mismo archivo, hemos realizado el ejercicio en varios pasos:
```
1. Extraer audio original del video y convertirlo a .mp3.
2. Realizar un mapeo de los dos inputs (video muestra y audio extraido en 1) al mismo archivo .mp4
```
El código que realiza estas dos funcionalidades es el siguiente:
```ruby
    1. os.system("ffmpeg -i Resistencia_MP4_Container.mp4 -c:a mp3 -b:a 320k -ac 2 -sn -vn Resistencia_audio.mp3")
    2. os.system("ffmpeg -i Resistencia_MP4_Container.mp4 -i Resistencia_audio.mp3 -map 0:v -c:v copy -map 1:a -c:a copy -map 0:a -c:a copy Resistencia_MP4_Container_MP3.mp4")
```

Como podemos observar, en el primer paso, vemos como extraemos el canal de audio ```-c:a``` y lo extraemos a ```mp3```.
Seguidamente, importamos los dos archivos (video y audio) y con ```-map 0:v -c:v copy```, estamos copiando el video del primer input ```input #0``` y lo estamos colocando
en el ```Stream #0:0``` del nuevo archivo.
A continuación, mapeamos el audio del segundo input ```input #1```, y lo colocamos en el ```Stream #0:1``` del nuevo archivo en mp3 a 320 kbps en estéreo con el bloque ```-map 1:a -c:a copy -b:a 320k -ac 2```.
Por último, copiamos el codec de audio del archivo original (```input #0```), y lo mapeamos al ```Stream #0:2``` sin modificarlo con el bloque de código ```-map 0:a -c:a copy```.  
Si ejecutamos el siguiente comando ```ffmpeg -i media/Resistencia_MP4_Container_MP3.mp4``` obtenemos el resultado:

![Captura de pantalla 2021-12-02 a las 1 31 46](https://user-images.githubusercontent.com/91899380/144336614-ecffcf14-6c28-4ea7-bd8d-459b2db84181.png)

Para darle un poco mÁs de dinamismo al ejercicio, hemos añadido una pequeña selección de codecs de audio compatibles con el contenedor de video ```.mp4```.
Esta selección permite escoger 3 tipos de codecs de audio: 
```
1. MP3
2. AAC
3. AC-3
```
Cada uno de estos codecs, se obtendrán extrayendo préviamente el audio del archivo de entrada, convirtiendo este audio al formato deseado y, finalmente, guardándolo en un NUEVO contenedor ```.mp4```.
Este es el resultado de aplicar consecutivamente las 3 opciones disponibles en este menú:

![CONTAINER FINAL](https://user-images.githubusercontent.com/91899380/145125405-7b335d34-f9c2-430c-abdc-a51a0c2664d3.png)

### EJERCICIO 3: 
Para este ejercicio, nuestro objetivo ha sido encontrar que formatos de broadcasting son compatibles para retransmitir nuestro vídeo.
Para ello, hemos creado una estructura en formato JSON (sin exportar) que almacena todos los estándares de broadcasting que vamos a tener en cuenta:
``` ruby
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
```
Seguidamente, mediante el siguiente comando, hemos creado un archivo ```.json``` que nos permite almacenar e indexar ciertos campos que vamos a utilizar para poder compararlos posteriormente con los estándares definidos como hemos comentado antes.
```ruby
ffprobe -hide_banner -v error -show_entries stream=index,codec_type,codec_name -of default=noprint_wrappers=1 -print_format json "+str(filename)+" > format.json
```
donde ```filename``` es el nombre del archivo multimedia que queremos analizar y que se tendrá que especificar al comienzo del script:
```ruby 
filename = 'Resistencia_BM19_cropped.mp4
```
en nuestro caso y en el campo ```stream=index,codec_type,codec_name``` se especifican los campos que deseamos extraer del archivo ```.mp4```.
El bloque ```-of default=default=noprint_wrappers=1```, lo que básicamente hace es evitar imprimir cabezeras de datos innecesarias para nuestro anáisis.
Por último se exporta a ```.json``` mediante el bloque ```-print_format json "+str(filename)+" > format.json```.
El resultado de nuestro script será el siguiente:

### EJERCICIO 4: 
Este último ejercicio consiste simplemente en añadir subtítulos a nuestro vídeo. Para ello, primero hemos tenido que descargar los subtítulos del video desde internet en formato ```.srt```.
Una vez descargados y guardados en la carpeta ````media/````, podemos cargarlos en nuestro script y ejecutar el siguiente comando:
```ruby
os.system("ffmpeg -i "+str(filename)+" -vf subtitles=subtitles_resistencia.srt Resistencia_BM19_Spanish_subtitulado.mp4")
```
Que básicamente junta el video original y los subtítulos en formato ````srt````, ya que son más fáciles de interpretar.
El resultado es el siguiente:

![subtitles](https://user-images.githubusercontent.com/91899380/145307149-bbcbdada-e2c0-4100-94f6-7e83893132f0.png)
