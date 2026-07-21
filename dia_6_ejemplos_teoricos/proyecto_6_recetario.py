
### Recetario de cocina ###
from  os import *
from pathlib import Path

# Definición de funciones

def mostrar_categorias(ruta_base):
    contador = 1
    lista_categorias = []
    for elemento in list(ruta_base.iterdir()):
        if elemento.is_dir():
            print (f"{contador}. {elemento.name}")
            contador += 1            
            lista_categorias.append(elemento)
    return lista_categorias

def mostrar_recetas(ruta):
    contador = 1
    lista_recetas = []
    for elemento in list(ruta.glob("*.txt")):
        if elemento.is_file():
            print (f"{contador}. {elemento.name}")
            contador += 1            
            lista_recetas.append(elemento)
    return lista_recetas

# Inicio del programa

bienvenida = "Bienvenido al recetario de cocina"
print(bienvenida)

ruta_base = Path.cwd()/ "Recetas"
total_recetas = len(list(ruta_base.rglob("*.txt")))
print(f"Las recetas se encuentran en: {ruta_base}")
print(f"Total de recetas disponibles: {total_recetas}")   

opcion_menu = 0
while opcion_menu != 6:
    system("cls")
    print("\nMenú de opciones:")
    print("1. Leer receta")
    print("2. Crear receta")
    print("3. Crear categoría")
    print("4. Eliminar receta")
    print("5. Eliminar categoría")
    print("6. Finalizar")

    opcion_menu = int(input("Seleccione una opción (1-6): "))
    if opcion_menu == 1:
        mis_categorias = mostrar_categorias(ruta_base)
        index_categoria = int(input("Elige una categoría: ")) - 1
        ruta_categoria = mis_categorias[index_categoria]
        mis_recetas = mostrar_recetas(ruta_categoria)
        index_receta = int(input("Elige una receta: ")) - 1
        ruta_receta = mis_recetas[index_receta]
        receta_leida = ruta_receta.read_text()
        print("\n*** LEYENDO RECETA ***")
        print(receta_leida)      

    elif opcion_menu == 2:
        mis_categorias = mostrar_categorias(ruta_base)
        index_categoria = int(input("Elige una categoría: ")) - 1
        ruta_categoria = mis_categorias[index_categoria]
        nombre_receta = input("Elige un nombre para la nueva receta: ")
        contenido_receta = input("Escribe el contenido de la nueva receta (ingredientes, preparación): ")
        ruta_nueva_receta = Path(ruta_categoria, nombre_receta + ".txt")
        ruta_nueva_receta.write_text(contenido_receta)
        print(f"Receta '{nombre_receta}' creada exitosamente en la categoría '{ruta_categoria.name}'.")
                      
    elif opcion_menu == 3:
        nombre_categoria = input("Elige un nombre para la nueva categoría: ")
        ruta_nueva_categoria = Path(ruta_base, nombre_categoria)
        ruta_nueva_categoria.mkdir()
        print(f"Categoría '{nombre_categoria}' creada exitosamente.")

    elif opcion_menu == 4:
        mis_categorias = mostrar_categorias(ruta_base)
        index_categoria = int(input("Elige una categoría: ")) - 1
        ruta_categoria = mis_categorias[index_categoria]
        mis_recetas = mostrar_recetas(ruta_categoria)
        index_receta = int(input("Elige una receta: ")) - 1
        ruta_receta = mis_recetas[index_receta]
        ruta_receta.unlink()
        print(f"Receta '{ruta_receta.name}' eliminada exitosamente de la categoría '{ruta_categoria.name}'.")

    elif opcion_menu == 5:
        mis_categorias = mostrar_categorias(ruta_base)
        index_categoria = int(input("Elige una categoría: ")) - 1
        ruta_categoria = mis_categorias[index_categoria]
        ruta_categoria.rmdir()
        print(f"Categoría '{ruta_categoria.name}' eliminada exitosamente.")
    
    elif opcion_menu == 6:
        print("Has elegido Finalizar")
        break
    input("Presiona una tecla para continuar")
