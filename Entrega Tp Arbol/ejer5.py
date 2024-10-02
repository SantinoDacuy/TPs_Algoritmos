from cola import Queue
from arbol import BinaryTree

#creamos el árbol original
arbol = BinaryTree()

#a) inserción de personajes con campo booleano
arbol.insert_node("Iron Man", {"is_hero": True})
arbol.insert_node("Captain America", {"is_hero": True})
arbol.insert_node("Thanos", {"is_hero": False})
arbol.insert_node("Doctor Strange", {"is_hero": True})
arbol.insert_node("Loki", {"is_hero": False})
arbol.insert_node("Black Widow", {"is_hero": True})
arbol.insert_node("Red Skull", {"is_hero": False})

#b) listar los villanos ordenados alfabéticamente
print("b) Villanos ordenados alfabéticamente:")
arbol.inorden_villanos()

#c) mostrar todos los superhéroes que empiezan con la letra C
print("")
print("c) Superhéroes que empiezan con 'C':")
arbol.inorden_superheros_start_with("C")

#d) determinar cuántos superhéroes hay en el árbol
num_heroes = arbol.contar_super_heroes()
print("")
print(f"d) Número total de superhéroes: {num_heroes}")

#e) Doctor Strange está mal cargado. Usar búsqueda por proximidad para encontrarlo y modificar su nombre
nodo_dr_strange = arbol.search("Doctor Strange")

if not nodo_dr_strange:
    #si no se encuentra exactamente "Doctor Strange", recorremos el árbol para buscar por proximidad
    print("")
    print("e) Búsqueda por proximidad para encontrar Doctor Strange y modificar su nombre:")
    
    #realizar un recorrido inorden manual para encontrar el nombre que contiene "Doctor"
    def recorrer_proximidad(nodo, keyword):
        if nodo is not None:
            recorrer_proximidad(nodo.left, keyword)
            if keyword.lower() in nodo.value.lower():
                print(f"Coincidencia encontrada: {nodo.value}")
                return nodo
            recorrer_proximidad(nodo.right, keyword)
    
    nodo_dr_strange = recorrer_proximidad(arbol.root, "Doctor")

#si encontramos el nodo, modificamos el valor
if nodo_dr_strange:
    nodo_dr_strange.value = "Doctor Stephen Strange"
    print(f"Nombre modificado a: {nodo_dr_strange.value}")


#f) listar los superhéroes ordenados de manera descendente
print("")
print("f) Superhéroes en orden descendente:")
def inorden_superheroes_descendente(root):
    if root is not None:
        inorden_superheroes_descendente(root.right)
        if root.other_value.get('is_hero') is True:
            print(root.value)
        inorden_superheroes_descendente(root.left)

inorden_superheroes_descendente(arbol.root)

#g) generar un bosque a partir de este árbol (uno con superhéroes y otro con villanos)
heroes_tree = BinaryTree()
villanos_tree = BinaryTree()

def separar_bosque(root, heroes_tree, villanos_tree):
    if root is not None:
        if root.other_value.get('is_hero') is True:
            heroes_tree.insert_node(root.value, root.other_value)
        else:
            villanos_tree.insert_node(root.value, root.other_value)
        separar_bosque(root.left, heroes_tree, villanos_tree)
        separar_bosque(root.right, heroes_tree, villanos_tree)

separar_bosque(arbol.root, heroes_tree, villanos_tree)

#g-I) determinar cuántos nodos tiene cada árbol
def contar_nodos(root):
    if root is None:
        return 0
    return 1 + contar_nodos(root.left) + contar_nodos(root.right)

num_heroes_arbol = contar_nodos(heroes_tree.root)
num_villanos_arbol = contar_nodos(villanos_tree.root)

print("")
print(f"g.I) El árbol de superhéroes tiene {num_heroes_arbol} nodos.")
print(f"El árbol de villanos tiene {num_villanos_arbol} nodos.")

#g-II) barrido ordenado alfabéticamente de cada árbol
print("")
print("g-II) Superhéroes en orden alfabético:")
heroes_tree.inorden()

print("Villanos en orden alfabético:")
villanos_tree.inorden_villanos()