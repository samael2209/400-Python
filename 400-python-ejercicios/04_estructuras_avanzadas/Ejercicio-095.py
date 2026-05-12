# Diseña un programa que almacene información sobre películas en un diccionario, 
# donde cada película tiene un título, 
# una lista de actores principales y 
# una tupla con la fecha de lanzamiento y la duración



peliculas = {
    "pelicula_1": {
        "titulo": "Interstellar",

        "actores_principales": [
            "Matthew McConaughey",
            "Anne Hathaway",
            "Jessica Chastain"
        ],

        "informacion": (
            "2014-11-07",   # fecha de lanzamiento
            169             # duración en minutos
        )
    },

    "pelicula_2": {
        "titulo": "The Matrix",

        "actores_principales": [
            "Keanu Reeves",
            "Laurence Fishburne",
            "Carrie-Anne Moss"
        ],

        "informacion": (
            "1999-03-31",
            136
        )
    },

    "pelicula_3": {
        "titulo": "Inception",

        "actores_principales": [
            "Leonardo DiCaprio",
            "Joseph Gordon-Levitt",
            "Elliot Page"
        ],

        "informacion": (
            "2010-07-16",
            148
        )
    }
}

def agregar_pelicula(peliculas:dict, titulo:str, actores_principales:list, informacion:tuple)->dict:
    numero_pelicula = f"pelicula_{len(peliculas) + 1}"
        
    peliculas[numero_pelicula] = {
        "titulo" : titulo,
        "actores_principales" : actores_principales,
        "informacio" : informacion
    }
    
    return peliculas

agregar_pelicula(
    peliculas,
    "Interstellar",
    ["Matthew McConaughey", "Anne Hathaway"],
    ("2014-11-07", 169)
)

print(peliculas)