from heap import HeapMax, HeapMin

#personajes de MCU: nombre, superhéroe, género
mcu_characters = [
    {"name": "Tony Stark", "hero": "Iron Man", "gender": "M"},
    {"name": "Steve Rogers", "hero": "Capitán América", "gender": "M"},
    {"name": "Natasha Romanoff", "hero": "Black Widow", "gender": "F"},
    {"name": "Carol Danvers", "hero": "Capitana Marvel", "gender": "F"},
    {"name": "Scott Lang", "hero": "Ant-Man", "gender": "M"},
    {"name": "Thor Odinson", "hero": "Thor", "gender": "M"}
]

#crear el heap min para mantener los personajes organizados por nombre
heap_min = HeapMin()

#insertar los personajes en el heap con prioridad según el nombre del personaje (alfabéticamente)
for character in mcu_characters:
    heap_min.arrive(character, ord(character["name"][0]))

#a) determinar el nombre del personaje de la superhéroe Capitana Marvel
def find_character_by_hero(heap, hero_name):
    for element in heap.elements:
        if element[1]["hero"] == hero_name:
            return element[1]["name"]
    return None

#b) mostrar los nombres de los superhéroes femeninos
def show_female_heroes(heap):
    for element in heap.elements:
        if element[1]["gender"] == "F":
            print(f'{element[1]["hero"]} es femenina')

#c) mostrar los nombres de los personajes masculinos
def show_male_characters(heap):
    for element in heap.elements:
        if element[1]["gender"] == "M":
            print(f'{element[1]["name"]} es masculino')

#d) determinar el nombre del superhéroe del personaje Scott Lang
def find_hero_by_character(heap, character_name):
    for element in heap.elements:
        if element[1]["name"] == character_name:
            return element[1]["hero"]
    return None

#e) mostrar todos los datos de los superhéroes o personajes cuyos nombres comienzan con 'S'
def show_characters_by_initial(heap, initial):
    for element in heap.elements:
        if element[1]["name"].startswith(initial) or element[1]["hero"].startswith(initial):
            print(element[1])

#f) determinar si Carol Danvers está en el heap e indicar su superhéroe
def find_carol(heap):
    for element in heap.elements:
        if element[1]["name"] == "Carol Danvers":
            return element[1]["hero"]
    return None

#llamar a las funciones

print("a. Personaje de Capitana Marvel:", find_character_by_hero(heap_min, "Capitana Marvel"))

print("\nb. Superhéroes femeninos:")
show_female_heroes(heap_min)

print("\nc. Personajes masculinos:")
show_male_characters(heap_min)

print("\nd. Superhéroe de Scott Lang:", find_hero_by_character(heap_min, "Scott Lang"))

print("\ne. Personajes y superhéroes que comienzan con 'S':")
show_characters_by_initial(heap_min, 'S')

print("\nf. Superhéroe de Carol Danvers:", find_carol(heap_min))
