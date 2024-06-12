from jedi import jedis

def por_nombre(jedi):
    return jedi['name']

def por_especie(jedi):
    especie = jedi['species']
    if especie is None:
        return ''
    else:
        return especie

def buscar(lista_jedis, criterio, valor):
    for indice, elemento in enumerate(lista_jedis):
        if elemento[criterio] == valor:
            return indice

def eliminar(lista_jedis, criterio, valor):
    indice = buscar(lista_jedis, criterio, valor)
    if indice is not None:
        return lista_jedis.pop(indice)

def listar_jedis_ordenados(lista_jedis):
    lista_jedis_ordenada = sorted(lista_jedis, key=lambda x: (por_nombre(x), por_especie(x)))
    return lista_jedis_ordenada

# Función para mostrar información de Ahsoka Tano y Kit Fisto
def mostrar_info_jedis(lista_jedis, nombres):
    for nombre in nombres:
        indice = buscar(lista_jedis, 'name', nombre)
        if indice is not None:
            print(lista_jedis[indice])

# Función para mostrar padawan de Yoda y Luke Skywalker
def mostrar_padawan_yoda_luke(lista_jedis, maestros):
    padawans = []
    for maestro in maestros:
        for jedi in lista_jedis:
            if jedi['master'] == maestro and jedi['rank'] == 'Padawan':
                padawans.append(jedi)
    return padawans

#a,b,c
jedis_ordenados = listar_jedis_ordenados(jedis)
print("a) Listado ordenado por nombre y especie:")
for jedi in jedis_ordenados:
    print(jedi)
print('\n\n')

print("b) Información de Ahsoka Tano y Kit Fisto:")
mostrar_info_jedis(jedis, ["Ahsoka Tano", "Kit Fisto"])
print('\n\n')

print("c) Padawan de Yoda y Luke Skywalker:")
padawans = mostrar_padawan_yoda_luke(jedis, ["Yoda", "Luke Skywalker"])
for padawan in padawans:
    print(padawan)
print('\n\n')

# Función para mostrar los Jedi de especie humana y twi'lek
def mostrar_jedis_especie(lista_jedis, especies):
    jedis_especies = []
    for especie in especies:
        for jedi in lista_jedis:
            if jedi['species'] == especie:
                jedis_especies.append(jedi)
    return jedis_especies

# Función para listar todos los Jedi que comienzan con A
def listar_jedis_comienzan_con(lista_jedis, letra):
    jedis_comienzan_con = []
    for jedi in lista_jedis:
        if jedi['name'].startswith(letra):
            jedis_comienzan_con.append(jedi)
    return jedis_comienzan_con

# Actividades d) y e)
print("d) Jedi de especie humana y twi'lek:")
jedis_especies = mostrar_jedis_especie(jedis, ["Human", "Twi'lek"])
for jedi in jedis_especies:
    print(jedi)
print('\n\n')

print("e) Jedi cuyos nombres comienzan con A:")
jedis_letra_a = listar_jedis_comienzan_con(jedis, 'A')
for jedi in jedis_letra_a:
    print(jedi)
print('\n\n')

# Función para indicar los Jedi que utilizaron sable de luz amarillo o violeta
def mostrar_jedis_colores_especificos(lista_jedis, colores):
    jedis_colores_especificos = []
    for jedi in lista_jedis:
        if jedi['lightsaber_color'] is not None:
            colores_jedi = jedi['lightsaber_color'].split('/')
            for color in colores:
                if color in colores_jedi:
                    jedis_colores_especificos.append(jedi['name'])
                    break
    return jedis_colores_especificos

# Función para mostrar los Jedi que usaron sable de luz de más de un color
def mostrar_jedis_mas_de_un_color(lista_jedis):
    jedis_mas_de_un_color = []
    for jedi in lista_jedis:
        if jedi['lightsaber_color'] is not None:
            colores = jedi['lightsaber_color'].split('/')
            if len(colores) > 1:
                jedis_mas_de_un_color.append(jedi)
    return jedis_mas_de_un_color

# Actividad f)
print("f) Jedi que usaron sable de luz de más de un color:")
jedis_mas_de_un_color = mostrar_jedis_mas_de_un_color(jedis)
for jedi in jedis_mas_de_un_color:
    print(jedi)
print('\n\n')

# Actividad g)
print("g) Jedi que utilizaron sable de luz amarillo o violeta:")
jedis_colores_especificos = mostrar_jedis_colores_especificos(jedis, ["Yellow", "Purple"])
for jedi in jedis_colores_especificos:
    print(jedi)
print('\n\n')

# Función para indicar los nombres de los padawans de Qui-Gon Jinn y Mace Windu, si los tuvieron
def mostrar_padawans_maestros(lista_jedis, maestros):
    padawans = {}
    for maestro in maestros:
        padawans[maestro] = []
        for jedi in lista_jedis:
            if jedi['master'] is not None and maestro in jedi['master']:
                padawans[maestro].append(jedi['name'])
    return padawans

# Actividad h)
print("h) Nombres de los padawans de Qui-Gon Jinn y Mace Windu:")
padawans = mostrar_padawans_maestros(jedis, ["Qui-Gon Jinn", "Mace Windu"])
for maestro, padawan_list in padawans.items():
    if padawan_list:
        print(f"Padawans de {maestro}: {', '.join(padawan_list)}")
    else:
        print(f"{maestro} no tuvo padawans.")
print('\n\n')

# Función para mostrar todos los Jedi que tengan el ranking de Grand Master
def mostrar_grand_masters(lista_jedis):
    grand_masters = []
    for jedi in lista_jedis:
        if jedi['master'] is None:
            grand_masters.append(jedi)
    return grand_masters

# Actividad i)
print("i) Jedi que tienen el ranking de Grand Master:")
grand_masters = mostrar_grand_masters(jedis)
for jedi in grand_masters:
    print(jedi)