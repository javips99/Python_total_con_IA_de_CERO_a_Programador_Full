
import zipfile
import shutil

# Crear un archivo comprimido en formato ZIP
mi_zip = zipfile.ZipFile("archivo_comprimido.zip", "w")
mi_zip.write("mi_texto_A.txt")
mi_zip.write("mi_texto_B.txt")
mi_zip.close()

# Abrir un archivo comprimido en formato ZIP
mi_zip = zipfile.ZipFile("archivo_comprimido.zip", "r")
mi_zip.extractall()
mi_zip.close()


# otra forma de comprimir usando shutil

carpeta_origen = "directorio_a_comprimir"
carpeta_destino = "archivo_comprimido_shutil.zip"
shutil.make_archive(carpeta_destino, 'zip', carpeta_origen)

# para descomprimir usando shutil
shutil.unpack_archive(carpeta_destino, "directorio_descomprimido", "zip")
