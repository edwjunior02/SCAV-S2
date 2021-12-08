import os.path
import time
import shutil

def Ex1_main():
    # Nuestra línea de comando de FFMPEG solo lee imágenes que estén en el mismo directorio que el script en el que se lance la petición.
    # Para ello, haremos una copia de media/Resistencia_BM19_cropped_2.mp4 y la pasaremos al directorio src/.
    pathCarpeta = (
        "/Users/edwjunior/Documents/UNIVERSIDAD/4o CURSO/1r TRIMESTRE/SISTEMES DE CODIFICACIÓ D'ÀUDIO I VIDEO"
        "/SEMINARS/SEMINAR 2/media/")
    pathCarpeta2 = (
        "/Users/edwjunior/Documents/UNIVERSIDAD/4o CURSO/1r TRIMESTRE/SISTEMES DE CODIFICACIÓ D'ÀUDIO I VIDEO"
        "/SEMINARS/SEMINAR 2/src")

    if not os.path.isdir(pathCarpeta):
        print('la primera carpeta no existe')
    elif not os.path.isdir(pathCarpeta2):
        print('la segunda carpeta no existe')

    contenidos = os.listdir(pathCarpeta)
    for elemento in contenidos:
        try:
            if elemento == 'Resistencia_BM19_cropped_2.mp4':
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

    os.system(
        "ffmpeg -flags2 +export_mvs -i Resistencia_BM19_cropped_2.mp4 -vf codecview=mv=pf+bf+bb Resistencia_mvs.mp4")
    print("Reproduciendo video...")
    time.sleep(2)
    os.system("ffplay -flags2 +export_mvs -i Resistencia_BM19_cropped_2.mp4 -vf codecview=mv=pf+bf+bb")

    # ----------------------------------------------------------------------------------------------------------------------

    contenidos = os.listdir(pathCarpeta2)
    for elemento in contenidos:
        try:
            if elemento.endswith(".mp4"):
                print(f"Moviendo {elemento} --> {pathCarpeta} ... ", end="")
                src = os.path.join(pathCarpeta2, elemento)  # origen
                dst = os.path.join(pathCarpeta, elemento)  # destino
                shutil.move(src, dst)  # Ahora utilizamos move en vez de copy, ya que lo queremos mover de aquí.
                time.sleep(2)
                print("Correcto")
            else:
                continue
        except:
            print("Falló")
            print("Error, no se pudo copiar el archivo. Verifique los permisos de escritura")

    time.sleep(2)
    print(f"Se han movido los archivos correctamente.")

Ex1_main()
import main
main.s2_main()

