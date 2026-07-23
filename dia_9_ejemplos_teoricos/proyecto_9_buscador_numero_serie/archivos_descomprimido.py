import zipfile

mi_zip = zipfile.ZipFile("Proyecto+Dia+9.zip", "r")
mi_zip.extractall()
mi_zip.close()