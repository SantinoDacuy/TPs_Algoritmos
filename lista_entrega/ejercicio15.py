import random

entrenadores = [
    {
        "nombre": "Ash Ketchum",
        "torneos_ganados": 7,
        "batallas_perdidas": 50,
        "batallas_ganadas": 120
    },
    {
        "nombre": "Goh",
        "torneos_ganados": 2,
        "batallas_perdidas": 10,
        "batallas_ganadas": 40
    },
    {
        "nombre": "Leon",
        "torneos_ganados": 10,
        "batallas_perdidas": 5,
        "batallas_ganadas": 100
    },
    {
        "nombre": "Chloe",
        "torneos_ganados": 1,
        "batallas_perdidas": 8,
        "batallas_ganadas": 30
    },
    {
        "nombre": "Raihan",
        "torneos_ganados": 4,
        "batallas_perdidas": 15,
        "batallas_ganadas": 60
    }
]

pokemons = [
    {
        "nombre": "Pikachu",
        "nivel": 35,
        "tipo": "Eléctrico",
        "subtipo": None
    },
    {
        "nombre": "Charizard",
        "nivel": 40,
        "tipo": "Fuego",
        "subtipo": "Volador"
    },
    {
        "nombre": "Bulbasaur",
        "nivel": 30,
        "tipo": "Planta",
        "subtipo": "Veneno"
    },
    {
        "nombre": "Starmie",
        "nivel": 30,
        "tipo": "Agua",
        "subtipo": "Psíquico"
    },
    {
        "nombre": "Psyduck",
        "nivel": 25,
        "tipo": "Agua",
        "subtipo": None
    },
    {
        "nombre": "Gyarados",
        "nivel": 35,
        "tipo": "Agua",
        "subtipo": "Volador"
    },
    {
        "nombre": "Onix",
        "nivel": 38,
        "tipo": "Roca",
        "subtipo": "Tierra"
    },
    {
        "nombre": "Geodude",
        "nivel": 28,
        "tipo": "Roca",
        "subtipo": "Tierra"
    },
    {
        "nombre": "Vulpix",
        "nivel": 20,
        "tipo": "Fuego",
        "subtipo": None
    },
    {
        "nombre": "Blastoise",
        "nivel": 50,
        "tipo": "Agua",
        "subtipo": None
    },
    {
        "nombre": "Umbreon",
        "nivel": 45,
        "tipo": "Siniestro",
        "subtipo": None
    },
    {
        "nombre": "Nidoking",
        "nivel": 40,
        "tipo": "Veneno",
        "subtipo": "Tierra"
    }
]

# Función para asignar Pokémon aleatoriamente a los entrenadores
def asignar_pokemons_aleatorios(entrenadores, pokemons):
    for entrenador in entrenadores:
        num_pokemons = random.randint(1, 4)  # Seleccionar entre 1 y 4 Pokémon
        entrenador['pokemons'] = random.sample(pokemons, num_pokemons)  # Seleccionar Pokémon aleatoriamente

# Asignar Pokémon a los entrenadores
asignar_pokemons_aleatorios(entrenadores, pokemons)

#----------------------------------------------------------------------------------------

# a. Obtener la cantidad de Pokémons de un determinado entrenador
def cantidad_pokemons(entrenador_nombre):
    for entrenador in entrenadores:
        if entrenador['nombre'] == entrenador_nombre:
            return len(entrenador['pokemons'])
    return 0

# b. Listar los entrenadores que hayan ganado más de tres torneos
def entrenadores_con_mas_de_tres_torneos():
    return [entrenador for entrenador in entrenadores if entrenador['torneos_ganados'] > 3]

# c. El Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados
def pokemon_mayor_nivel_entrenador_mayor_torneos():
    max_torneos = max(entrenadores, key=lambda x: x['torneos_ganados'])
    return max(max_torneos['pokemons'], key=lambda x: x['nivel'])

# d. Mostrar todos los datos de un entrenador y sus Pokémons
def mostrar_datos_entrenador(entrenador_nombre):
    for entrenador in entrenadores:
        if entrenador['nombre'] == entrenador_nombre:
            return entrenador
    return None

# e. Mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79%
def entrenadores_con_alto_porcentaje_batallas():
    return [entrenador for entrenador in entrenadores if (entrenador['batallas_ganadas'] / (entrenador['batallas_ganadas'] + entrenador['batallas_perdidas'])) > 0.79]

# f. Entrenadores con Pokémons de tipo fuego y planta o agua y volador
def entrenadores_tipo_especial():
    return [entrenador for entrenador in entrenadores if any((poke['tipo'] == 'Fuego' and poke['subtipo'] == 'Planta') or (poke['tipo'] == 'Agua' and poke['subtipo'] == 'Volador') for poke in entrenador['pokemons'])]

# g. Promedio de nivel de los Pokémons de un determinado entrenador
def promedio_nivel_pokemons(entrenador_nombre):
    for entrenador in entrenadores:
        if entrenador['nombre'] == entrenador_nombre:
            pokemons = entrenador['pokemons']
            return sum(poke['nivel'] for poke in pokemons) / len(pokemons)
    return 0

# h. Determinar cuántos entrenadores tienen un determinado Pokémon
def entrenadores_con_pokemon(pokemon_nombre):
    return len([entrenador for entrenador in entrenadores if any(poke['nombre'] == pokemon_nombre for poke in entrenador['pokemons'])])

# i. Mostrar los entrenadores que tienen Pokémons repetidos
def entrenadores_con_pokemons_repetidos():
    resultado = []
    for entrenador in entrenadores:
        nombres_pokemons = [poke['nombre'] for poke in entrenador['pokemons']]
        if len(nombres_pokemons) != len(set(nombres_pokemons)):
            resultado.append(entrenador)
    return resultado

# j. Determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull
def entrenadores_con_pokemons_especificos():
    return [entrenador for entrenador in entrenadores if any(poke['nombre'] in ['Tyrantrum', 'Terrakion', 'Wingull'] for poke in entrenador['pokemons'])]

# k. Determinar si un entrenador “X” tiene al Pokémon “Y”
def entrenador_tiene_pokemon(entrenador_nombre, pokemon_nombre):
    for entrenador in entrenadores:
        if entrenador['nombre'] == entrenador_nombre:
            for poke in entrenador['pokemons']:
                if poke['nombre'] == pokemon_nombre:
                    return entrenador, poke
    return None, None

# Pruebas de las funciones
print("a. Cantidad de Pokémons de Ash:", cantidad_pokemons("Ash Ketchum"))
print("b. Entrenadores con más de tres torneos ganados:", entrenadores_con_mas_de_tres_torneos())
print("c. Pokémon de mayor nivel del entrenador con más torneos ganados:", pokemon_mayor_nivel_entrenador_mayor_torneos())
print("d. Datos de entrenador Ash:", mostrar_datos_entrenador("Ash Ketchum"))
print("e. Entrenadores con más del 79% de batallas ganadas:", entrenadores_con_alto_porcentaje_batallas())
print("f. Entrenadores con Pokémons tipo fuego/planta o agua/volador:", entrenadores_tipo_especial())
print("g. Promedio de nivel de los Pokémons de Ash:", promedio_nivel_pokemons("Ash Ketchum"))
print("h. Entrenadores con Pikachu:", entrenadores_con_pokemon("Pikachu"))
print("i. Entrenadores con Pokémons repetidos:", entrenadores_con_pokemons_repetidos())
print("j. Entrenadores con Tyrantrum, Terrakion o Wingull:", entrenadores_con_pokemons_especificos())
entrenador, pokemon = entrenador_tiene_pokemon("Ash Ketchum", "Pikachu")
print(f"k. ¿Ash tiene a Pikachu? {'Sí' if entrenador else 'No'}")
if entrenador:
    print(f"   Datos de Ash: {entrenador}")
    print(f"   Datos de Pikachu: {pokemon}")
