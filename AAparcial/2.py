from pila import Stack
from dino import dinosaurios

pila_dinosaurios = Stack()
for dino in dinosaurios:
    pila_dinosaurios.push(dino)

# a) Contar cuantas especies hay
especies = set()
for dino in dinosaurios:
    especies.add(dino["especie"])
print("A: Cantidad de especies:", len(especies))

# b) Determinar cuantos descubridores distintos hay
descubridores = set()
for dino in dinosaurios:
    descubridores.add(dino["descubridor"])
print("B: Cantidad de descubridores distintos:", len(descubridores))

# c) Mostrar todos los dinosaurios que empiecen con T
print("C: Dinosaurios que empiezan con T:")
pila_aux = Stack()
while pila_dinosaurios.size() > 0:
    dino = pila_dinosaurios.pop()
    if dino["nombre"].startswith("T"):
        print(dino["nombre"])
    pila_aux.push(dino)

# Restaurar la pila original
while pila_aux.size() > 0:
    pila_dinosaurios.push(pila_aux.pop())

# d) Mostrar todos los dinosaurios que pesen menos de 275 Kg
print("D: Dinosaurios que pesan menos de 275 kg:")
while pila_dinosaurios.size() > 0:
    dino = pila_dinosaurios.pop()
    peso_kg = int(dino["peso"].split()[0])
    if peso_kg < 275:
        print(dino["nombre"])
    pila_aux.push(dino)

# Restaurar la pila original
while pila_aux.size() > 0:
    pila_dinosaurios.push(pila_aux.pop())

# e) Dejar en una pila aparte todos los dinosaurios que comienzan con A, Q, S
pila_aqs = Stack()
while pila_dinosaurios.size() > 0:
    dino = pila_dinosaurios.pop()
    if dino["nombre"][0] in ['A', 'Q', 'S']:
        pila_aqs.push(dino)
    else:
        pila_aux.push(dino)

# Mostrar dinosaurios en la pila AQS
print("E: Dinosaurios que comienzan con A, Q, S:")
while pila_aqs.size() > 0:
    dino = pila_aqs.pop()
    print(dino["nombre"])
    pila_aux.push(dino)

# Restaurar la pila original
while pila_aux.size() > 0:
    pila_dinosaurios.push(pila_aux.pop())
