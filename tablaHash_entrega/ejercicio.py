from collections import defaultdict

# a. Definir funciones hash para cada tabla

def hash_tipo(pokemon):
    # Función hash para el tipo de Pokémon
    return pokemon['tipo']

def hash_numero(pokemon):
    # Función hash para el último dígito del número del Pokémon
    return pokemon['numero'] % 10

def hash_nivel(pokemon):
    # Función hash para repartir los niveles en 10 posiciones
    return pokemon['nivel'] // 10

# b. Inicializar tablas hash abiertas con listas como estructura secundaria

tabla_tipo = defaultdict(list)
tabla_numero = defaultdict(list)
tabla_nivel = defaultdict(list)

# d. Función para cargar un Pokémon en las tablas hash

def cargar_pokemon(numero, nombre, tipos, nivel):
    pokemon = {'numero': numero, 'nombre': nombre, 'tipo': tipos, 'nivel': nivel}
    
    # c. Si el Pokémon es de más de un tipo, cargarlo en cada tabla correspondiente
    for tipo in tipos:
        tabla_tipo[tipo].append(pokemon)
        
    tabla_numero[hash_numero(pokemon)].append(pokemon)
    tabla_nivel[hash_nivel(pokemon)].append(pokemon)

# e. Función para mostrar Pokémons cuyos números terminan en 3, 7 y 9

def mostrar_pokemon_por_numero():
    numeros = [3, 7, 9]
    for numero in numeros:
        print(f"Pokémons cuyo número termina en {numero}:")
        for pokemon in tabla_numero[numero]:
            print(pokemon)

# f. Función para mostrar Pokémons cuyos niveles son múltiplos de 2, 5 y 10

def mostrar_pokemon_por_nivel():
    niveles = [2, 5, 10]
    for nivel in niveles:
        print(f"Pokémons cuyo nivel es múltiplo de {nivel}:")
        for pokemon in tabla_nivel[nivel // 10]:
            if pokemon['nivel'] % nivel == 0:
                print(pokemon)

# g. Función para mostrar Pokémons de tipos específicos

def mostrar_pokemon_por_tipo():
    tipos = ['Acero', 'Fuego', 'Electrico', 'Hielo']
    for tipo in tipos:
        print(f"Pokémons del tipo {tipo}:")
        for pokemon in tabla_tipo[tipo]:
            print(pokemon)

# Ejemplo de carga de Pokémons (d. cargar Pokémons)

cargar_pokemon(1, 'Bulbasaur', ['Planta', 'Veneno'], 5)
cargar_pokemon(4, 'Charmander', ['Fuego'], 5)
cargar_pokemon(7, 'Squirtle', ['Agua'], 5)
cargar_pokemon(25, 'Pikachu', ['Electrico'], 10)
cargar_pokemon(37, 'Vulpix', ['Fuego'], 15)
cargar_pokemon(63, 'Abra', ['Psiquico'], 20)
cargar_pokemon(87, 'Dewgong', ['Agua', 'Hielo'], 30)
cargar_pokemon(99, 'Kingler', ['Agua'], 35)
cargar_pokemon(133, 'Eevee', ['Normal'], 40)
cargar_pokemon(147, 'Dratini', ['Dragon'], 45)
cargar_pokemon(203, 'Girafarig', ['Normal', 'Psiquico'], 50)
cargar_pokemon(218, 'Slugma', ['Fuego'], 55)
cargar_pokemon(250, 'Ho-Oh', ['Fuego', 'Volador'], 70)
cargar_pokemon(303, 'Mawile', ['Acero', 'Hada'], 100)
cargar_pokemon(393, 'Piplup', ['Agua'], 90)
cargar_pokemon(460, 'Abomasnow', ['Planta', 'Hielo'], 60)

# Mostrar resultados (e, f, g)

print("=== Pokémons cuyos números terminan en 3, 7 y 9 ===")
mostrar_pokemon_por_numero()
print()

print("=== Pokémons cuyos niveles son múltiplos de 2, 5 y 10 ===")
mostrar_pokemon_por_nivel()
print()

print("=== Pokémons de tipos específicos: Acero, Fuego, Electrico, Hielo ===")
mostrar_pokemon_por_tipo()