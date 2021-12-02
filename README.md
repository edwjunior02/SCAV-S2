# SCAV-S2
#### Eduard Puig - 194161

### EJERCICIO 1: ...



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

![](IMAGENES README/ResistenciaMP4-Container.png)

Y queremos convertirlo en un contenedor con estas características:

![](IMAGENES README/NewContainerMP4.png)

Precisamente con ```ffmpeg``` podemos conseguir copiar cierta información de un contenedor a otro y añadir lo que nos falta.
Primero vamos quedarnos con solo el primer minuto del video ```Resistencia_BM19_cropped.mp4``` por razones de espacio, y vamos a copiar toda la información de este video a un nuevo container mp4 
a que llamaremos ```Resistencia_MP4_Container.mp4```.

Debido a que ```ffmpeg``` no puede sobreescribir el mismo archivo, hemos realizado el ejercicio en varios pasos:
```
1. Extraer audio original del video y convertirlo a .mp3.
2. Realizar un mapeo de los dos inputs (video muestra y audio extraido en 1) al mismo archivo .mp4
```
El código que realiza estas dos funcionalidades es el siguiente:
```ruby
    1. os.system("ffmpeg -i Resistencia_MP4_Container.mp4 -c:a mp3 -vn Resistencia_audio.mp3")
    2. os.system("ffmpeg -i Resistencia_MP4_Container.mp4 -i Resistencia_audio.mp3 -map 0:v -c:v copy -map 1:a -c:a copy -b:a 320k -ac 2 -map 0:a -c:a copy Resistencia_MP4_Container_MP3.mp4")
```

Como podemos observar, en el primer paso, vemos como extraemos el canal de audio ```-c:a``` y lo extraemos a ```mp3```.
Seguidamente, importamos los dos archivos (video y audio) y con ```-map 0:v -c:v copy```, estamos copiando el video del primer input ```input #0``` y lo estamos colocando
en el ```Stream #0:0``` del nuevo archivo.
A continuación, mapeamos el audio del segundo input ```input #1```, y lo colocamos en el ```Stream #0:1``` del nuevo archivo en mp3 a 320 kbps en estéreo con el bloque ```-map 1:a -c:a copy -b:a 320k -ac 2```.
Por último, copiamos el codec de audio del archivo original (```input #0```), y lo mapeamos al ```Stream #0:2``` sin modificarlo con el bloque de código ```-map 0:a -c:a copy```.  
Si ejecutamos el siguiente comando ```ffmpeg -i media/Resistencia_MP4_Container_MP3.mp4``` obtenemos el resultado:
![](IMAGENES README/Captura de pantalla 2021-12-02 a las 1.31.46.png)