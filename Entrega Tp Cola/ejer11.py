from cola import Queue

#personajes de Star Wars: nombre, planeta
characters = [
    {"name": "Luke Skywalker", "planet": "Tatooine"},
    {"name": "Han Solo", "planet": "Corellia"},
    {"name": "Leia Organa", "planet": "Alderaan"},
    {"name": "Yoda", "planet": "Dagobah"},
    {"name": "Jar Jar Binks", "planet": "Naboo"},
    {"name": "Obi-Wan Kenobi", "planet": "Stewjon"},
    {"name": "Anakin Skywalker", "planet": "Tatooine"}
]

queue = Queue()

#insertar personajes en la cola
for character in characters:
    queue.arrive(character)

#a) mostrar los personajes del planeta Alderaan, Endor y Tatooine
def show_characters_by_planet(queue, planets):
    temp_queue = Queue()
    for _ in range(queue.size()):
        character = queue.attention()
        if character["planet"] in planets:
            print(f'{character["name"]} es de {character["planet"]}')
        temp_queue.arrive(character)
    
    #cargar la cola original
    while temp_queue.size() > 0:
        queue.arrive(temp_queue.attention())

#b) indicar el planeta natal de Luke Skywalker y Han Solo
def show_home_planet(queue, names):
    temp_queue = Queue()
    for _ in range(queue.size()):
        character = queue.attention()
        if character["name"] in names:
            print(f'{character["name"]} es de {character["planet"]}')
        temp_queue.arrive(character)
    
    #cargar la cola original
    while temp_queue.size() > 0:
        queue.arrive(temp_queue.attention())

#c) insertar un nuevo personaje antes del maestro Yoda
def insert_before_yoda(queue, new_character):
    temp_queue = Queue()
    inserted = False
    for _ in range(queue.size()):
        character = queue.attention()
        if character["name"] == "Yoda" and not inserted:
            temp_queue.arrive(new_character)
            inserted = True
        temp_queue.arrive(character)
    
    #cargar la cola original
    while temp_queue.size() > 0:
        queue.arrive(temp_queue.attention())

#d) eliminar el personaje ubicado después de Jar Jar Binks
def remove_after_jar_jar(queue):
    temp_queue = Queue()
    skip_next = False
    for _ in range(queue.size()):
        character = queue.attention()
        if skip_next:
            skip_next = False 
            continue
        if character["name"] == "Jar Jar Binks":
            skip_next = True
        temp_queue.arrive(character)

    #cargar la cola original
    while temp_queue.size() > 0:
        queue.arrive(temp_queue.attention())

#llamar a las funciones
planets_to_show = ["Alderaan", "Endor", "Tatooine"]
show_characters_by_planet(queue, planets_to_show)

names_to_search = ["Luke Skywalker", "Han Solo"]
show_home_planet(queue, names_to_search)

new_character = {"name": "Ahsoka Tano", "planet": "Shili"}
insert_before_yoda(queue, new_character)

remove_after_jar_jar(queue)