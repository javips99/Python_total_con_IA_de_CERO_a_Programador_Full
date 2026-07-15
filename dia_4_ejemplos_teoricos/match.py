
serie = "N-02"

'''
if serie == "N-01":
    print("Samsung")
elif serie == "N-02":
    print("Nokia")
elif serie == "N-03":
    print("Motorola")
else:
    print("No se encontró")

'''
# mismo resultado utilizando match
match serie:
    case "N-01":
        print("Samsung")
    case "N-02":
        print("Nokia")
    case "N-03":
        print("Motorola")
    case _:
        print("No se encontró")


### ejemplo

cliente = {"nombre": "Francisco Javier",
           "edad": 39,
           "ocupacion": "programador"}

pelicula = {"titulo": "Matrix",
            "ficha_tecnica": {"protagonista": "Keanu Reeves",
                               "director": "Lana y Lily Wachowski"}}

libro = {"titulo": "1984",
         "autor": "George Orwell"}

elementos = [cliente, pelicula, libro]

for e in elementos:
    match e:
        case {"nombre": nombre,
             "edad": edad,
             "ocupacion": ocupacion}:
            print("Este es un cliente")
            print(nombre, edad, ocupacion)
            
        case {"titulo": titulo,
              "ficha_tecnica": {"protagonista": protagonista,
                                "director": director}}:
            print("Este es una pelicula")
            print(titulo, protagonista, director)

        case _:
            print("No se que es esto")    
