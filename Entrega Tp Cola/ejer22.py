from cola import Queue

#personajes de MCU: nombre, superhéroe, género
mcu_characters = [
    {"name": "Tony Stark", "hero": "Iron Man", "gender": "M"},
    {"name": "Steve Rogers", "hero": "Capitán América", "gender": "M"},
    {"name": "Natasha Romanoff", "hero": "Black Widow", "gender": "F"},
    {"name": "Carol Danvers", "hero": "Capitana Marvel", "gender": "F"},
    {"name": "Scott Lang", "hero": "Ant-Man", "gender": "M"},
    {"name": "Thor Odinson", "hero": "Thor", "gender": "M"}
]

queue = Queue()

#insertar personajes en la cola
for character in mcu_characters:
    queue.arrive(character)

#a) determinar el nombre del personaje de la superhéroe Capitana Marvel
def find_character_by_hero(queue, hero_name):
    temp_queue = Queue()
    result = None
    for _ in range(queue.size()):
        character = queue.attention()
        if character["hero"] == hero_name:
            result = character["name"]
        temp_queue.arrive(character)

    #cargar la cola original
    while temp_queue.size() > 0:
        queue.arrive(temp_queue.attention())
    
    return result

#b) mostrar los nombres de los superhéroes femeninos
def show_female_heroes(queue):
    temp_queue = Queue()
    for _ in range(queue.size()):
        character = queue.attention()
        if character["gender"] == "F":
            print(f'{character["hero"]} es femenina')
        temp_queue.arrive(character)

    #cargar la cola original
    while temp_queue.size() > 0:
        queue.arrive(temp_queue.attention())

#c) mostrar los nombres de los personajes masculinos
def show_male_characters(queue):
    temp_queue = Queue()
    for _ in range(queue.size()):
        character = queue.attention()
        if character["gender"] == "M":
            print(f'{character["name"]} es masculino')
        temp_queue.arrive(character)

    #cargar la cola original
    while temp_queue.size() > 0:
        queue.arrive(temp_queue.attention())

#d) determinar el nombre del superhéroe del personaje Scott Lang
def find_hero_by_character(queue, character_name):
    temp_queue = Queue()
    result = None
    for _ in range(queue.size()):
        character = queue.attention()
        if character["name"] == character_name:
            result = character["hero"]
        temp_queue.arrive(character)

    #cargar la cola original
    while temp_queue.size() > 0:
        queue.arrive(temp_queue.attention())

    return result

#e) mostrar todos los datos de los superhéroes o personajes cuyos nombres comienzan con 'S'
def show_characters_by_initial(queue, initial):
    temp_queue = Queue()
    for _ in range(queue.size()):
        character = queue.attention()
        if character["name"].startswith(initial) or character["hero"].startswith(initial):
            print(character)
        temp_queue.arrive(character)

    #cargar la cola original
    while temp_queue.size() > 0:
        queue.arrive(temp_queue.attention())

#f) determinar si Carol Danvers está en la cola e indicar su superhéroe
def find_carol(queue):
    temp_queue = Queue()
    result = None
    for _ in range(queue.size()):
        character = queue.attention()
        if character["name"] == "Carol Danvers":
            result = character["hero"]
        temp_queue.arrive(character)

    #cargar la cola original
    while temp_queue.size() > 0:
        queue.arrive(temp_queue.attention())

    return result

#llamar a las funciones
print("a) personaje de Capitana Marvel:", find_character_by_hero(queue, "Capitana Marvel"))
print("")
print("b) superhéroes femeninos:")
show_female_heroes(queue)

print("")
print("c) personajes masculinos:")
show_male_characters(queue)

print("")
print("d) superhéroe de Scott Lang:", find_hero_by_character(queue, "Scott Lang"))

print("")
print("e) personajes y superhéroes que comienzan con 'S':")
show_characters_by_initial(queue, 'S')

print("")
print("f) superhéroe de Carol Danvers:", find_carol(queue))