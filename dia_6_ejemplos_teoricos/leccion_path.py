
from pathlib import Path

base = Path.home()
guia = Path(base,
            "Europa", "España",
            Path("Barcelona", "Sagrada Familia.txt"))

print(guia.parent.parent)

###

guia = Path(Path.home() / "Europa")
for txt in Path(guia).glob("*.txt"):

    print(txt)

'''
Almacena en la variable ruta_base, un objeto Path que señale el directorio base del usuario.
Recuerda importar Path del módulo pathlib, y utilizar el método home()

'''
from pathlib import Path
ruta_base = Path(Path.home())

'''
Implementa y crea una ruta relativa que nos permita llegar al archivo "practicas_path.py" a partir de la siguiente estructura de carpetas:
Almacena el directorio obtenido en la variable ruta. No olvides importar Path.

'''
from pathlib import Path
ruta = Path("Curso Python","Día 6", "practicas_path.py")

print(ruta.parent.parent)

'''
Implementa y crea una ruta absoluta que nos permita llegar al archivo "practicas_path.py" a partir de la siguiente estructura de carpetas:
Almacena el directorio obtenido en la variable ruta. No olvides importar Path, 
y de concatenar el objeto Path que refiere a la carpeta base del usuario.

'''

ruta = Path(Path.home() / "Curso Python" / "Día 6" / "practicas_path.py")