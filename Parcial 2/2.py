from grafo import Graph

# Creación del grafo no dirigido
grafo = Graph(dirigido=False)

# Consigna d: Cargar los personajes específicos como vértices
personajes = [
    "Luke Skywalker", "Darth Vader", "Yoda", "Boba Fett", "C-3PO",
    "Leia", "Rey", "Kylo Ren", "Chewbacca", "Han Solo", "R2-D2", "BB-8"
]

for personaje in personajes:
    grafo.insert_vertice(personaje)

# Cargar las aristas con la cantidad de episodios compartidos
# Ejemplo de carga, en un caso real se debe llenar con todos los personajes relevantes
grafo.insert_arista("Luke Skywalker", "Darth Vader", 3)
grafo.insert_arista("Luke Skywalker", "Leia", 5)
grafo.insert_arista("Yoda", "Luke Skywalker", 2)
grafo.insert_arista("Yoda", "Chewbacca", 2)
grafo.insert_arista("Leia", "Han Solo", 4)
grafo.insert_arista("Rey", "Kylo Ren", 3)
grafo.insert_arista("C-3PO", "R2-D2", 6)
grafo.insert_arista("BB-8", "Rey", 2)

# Parte b: Hallar el árbol de expansión mínimo y verificar si incluye a Yoda
arbol_minimo = grafo.kruskal("Luke Skywalker")
contiene_yoda = any("Yoda" in arbol for arbol in arbol_minimo)
print("b) Árbol de expansión mínimo:", arbol_minimo)
print("b) ¿El árbol de expansión mínimo contiene a Yoda?", "Sí" if contiene_yoda else "No")

# Parte c: Determinar el número máximo de episodios compartidos y los personajes
max_episodios = 0
personajes_max_episodios = (None, None)

for nodo in grafo.elements:
    for arista in nodo['aristas']:
        if arista['peso'] > max_episodios:
            max_episodios = arista['peso']
            personajes_max_episodios = (nodo['value'], arista['value'])

print("c) Máximo de episodios compartidos:", max_episodios)
print("c) Personajes que comparten el máximo de episodios:", personajes_max_episodios)
