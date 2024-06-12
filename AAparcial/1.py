import random
def listar_inversa(lista):
    if len(lista) <= 1:
        return lista
    else:
        return listar_inversa(lista[1:]) + [lista[0]]

longitud = random.randint(1, 10) 
lista_aleatoria = [random.randint(1, 100) for _ in range(longitud)]

print("Lista original:", lista_aleatoria)
print("Lista invertida:", listar_inversa(lista_aleatoria))
