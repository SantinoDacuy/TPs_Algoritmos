from grafo import Graph

# se crea el grafo no dirigido

house_graph = Graph(dirigido=False)

# a) se crean los vertices (ambientes)

ambientes = ["cocina", "comedor", "cochera", "quincho", "baño 1", "baño 2",
            "habitación 1", "habitación 2", "sala de estar", "terraza", "patio"]

for ambiente in ambientes:
    house_graph.insert_vertice(ambiente)

# b) Cargar aristas para cada uno de los vértices

house_graph.insert_arista("cocina", "comedor", 5)
house_graph.insert_arista("cocina", "baño 1", 10)
house_graph.insert_arista("cocina", "terraza", 15)

house_graph.insert_arista("comedor", "cocina", 5)
house_graph.insert_arista("comedor", "sala de estar", 7)
house_graph.insert_arista("comedor", "patio", 12)

house_graph.insert_arista("cochera", "quincho", 20)
house_graph.insert_arista("cochera", "habitación 1", 25)
house_graph.insert_arista("cochera", "comedor", 18)

house_graph.insert_arista("quincho", "terraza", 8)
house_graph.insert_arista("quincho", "patio", 10)
house_graph.insert_arista("quincho", "baño 2", 15)

house_graph.insert_arista("baño 1", "habitación 1", 5)
house_graph.insert_arista("baño 1", "baño 2", 6)
house_graph.insert_arista("baño 1", "cocina", 10)

house_graph.insert_arista("baño 2", "habitación 2", 4)
house_graph.insert_arista("baño 2", "quincho", 15)
house_graph.insert_arista("baño 2", "terraza", 12)

house_graph.insert_arista("habitación 1", "habitación 2", 3)
house_graph.insert_arista("habitación 1", "baño 1", 5)
house_graph.insert_arista("habitación 1", "sala de estar", 8)

house_graph.insert_arista("habitación 2", "baño 2", 4)
house_graph.insert_arista("habitación 2", "habitación 1", 3)
house_graph.insert_arista("habitación 2", "terraza", 9)

house_graph.insert_arista("sala de estar", "comedor", 7)
house_graph.insert_arista("sala de estar", "habitación 1", 8)
house_graph.insert_arista("sala de estar", "terraza", 11)

house_graph.insert_arista("terraza", "patio", 6)
house_graph.insert_arista("terraza", "baño 2", 12)
house_graph.insert_arista("terraza", "sala de estar", 11)

house_graph.insert_arista("patio", "terraza", 6)
house_graph.insert_arista("patio", "comedor", 12)
house_graph.insert_arista("patio", "quincho", 10)

# c. obtener el árbol de expansión mínima y los metros de cables necesarios para conectar todos los ambientes
print("")
print("c)")
arbol_expansion_minima = house_graph.kruskal("cocina")

# Extraer y sumar los pesos de las aristas en el árbol de expansión mínima
distancia_total_mst = 0
for arista in arbol_expansion_minima[0].split(';'):
    if '-' in arista:
        # La distancia está en la última parte de cada sección de arista
        peso = int(arista.split('-')[-1])
        distancia_total_mst += peso

print("total de metros de cables necesarios para conectar todos los ambientes:", distancia_total_mst, "metros")
print("arbol de expansion minima:", arbol_expansion_minima)

# d) camino más corto desde la habitación 1 hasta la sala de estar para saber cuántos metros de cable de red son necesarios para conectar el router con el Smart Tv.
print("")
print("d)")
camino_mas_corto = house_graph.dijkstra("habitación 1")

distancia_total = 0

while True:
    nodo = camino_mas_corto.pop()
    if nodo is None:
        break
    if nodo[1][0] == "sala de estar":
        # Distancia acumulada hasta "sala de estar"
        distancia_total = nodo[0]
        break

print("distancia total desde habitación 1 hasta sala de estar:", distancia_total, "metros")