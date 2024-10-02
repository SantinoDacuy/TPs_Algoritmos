from cola import Queue
from arbol_avl import BinaryTree

#creamos el arbol avl
tree = BinaryTree()

#inserción de nodos con la información
data = [
    ('Ceto', {'derrotado_por': 'Teseo'}),
    ('Tifón', {'derrotado_por': 'Zeus'}),
    ('Equidna', {'derrotado_por': 'Teseo'}),
    ('Dino', {'derrotado_por': 'Atalanta'}),
    ('Pefredo', {'derrotado_por': 'Carcinos'}),
    ('Enio', {'derrotado_por': 'Gerión'}),
    ('Escila', {'derrotado_por': 'Cloto'}),
    ('Caribdis', {'derrotado_por': 'Láquesis'}),
    ('Euríale', {'derrotado_por': 'Átropos'}),
    ('Esteno', {'derrotado_por': 'Minotauro de Creta'}),
    ('Medusa', {'derrotado_por': 'Perseo'}),
    ('Harpías', {'derrotado_por': 'Ladón'}),
    ('Águila del Cáucaso', {'derrotado_por': 'Argos Panoptes'}),
    ('Quimera', {'derrotado_por': 'Belerofonte'}),
    ('Hidra de Lerna', {'derrotado_por': 'Heracles'}),
    ('León de Nemea', {'derrotado_por': 'Heracles'}),
    ('Esfinge', {'derrotado_por': 'Edipo'}),
    ('Dragón de la Cólquida', {'derrotado_por': 'Pitón'}),
    ('Cerbero', {'derrotado_por': 'Heracles'}),
    ('Jabalí de Erimanto', {'derrotado_por': 'Heracles'}),
    ('Cierva de Cerinea', {'derrotado_por': 'Heracles'}),
    ('Toro de Creta', {'derrotado_por': 'Teseo'}),
    ('Aves del Estínfalo', {'derrotado_por': 'Heracles'}),
    ('Ladón', {'derrotado_por': 'Heracles'}),
    ('Sirenas', {'derrotado_por': 'Heracles'}),
    ('Basilisco', {'derrotado_por': ''}),
    ('Talos', {'derrotado_por': 'Medea'})
]

#insertamos nodos en el árbol
for name, info in data:
    tree.insert_node(name, other_value=info)

#a) listado inorden de las criaturas y quienes la derrotaron
print("a) Listado inorden de las criaturas y quienes la derrotaron:")
tree.inorden()

#b) cargar una breve descripción sobre cada criatura
#se puede hacer al insertar los nodos con la información de las criaturas en el campo 'other_value'

#c) mostrar toda la información de la criatura Talos
talos = tree.search('Talos')
if talos:
    print("")
    print("c) Información de la criatura Talos:")
    print(talos.value, talos.other_value)

#d) determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas
def heroes_with_most_defeats(tree):
    from collections import Counter

    def count_defeats(root, counter):
        if root:
            derrotado_por = root.other_value.get('derrotado_por')
            if derrotado_por:
                counter[derrotado_por] += 1
            count_defeats(root.left, counter)
            count_defeats(root.right, counter)
    
    counter = Counter()
    count_defeats(tree.root, counter)
    most_common = counter.most_common(3)
    print("")
    print("d) Top 3 héroes o dioses que derrotaron mayor cantidad de criaturas:")
    for hero, count in most_common:
        print(f"{hero}: {count} criaturas")

heroes_with_most_defeats(tree)

#e) listar las criaturas derrotadas por Heracles
print("")
print("e) Criaturas derrotadas por Heracles:")
def list_defeated_by_heracles(root):
    if root:
        if root.other_value.get('derrotado_por') == 'Heracles':
            print(root.value)
        list_defeated_by_heracles(root.left)
        list_defeated_by_heracles(root.right)

list_defeated_by_heracles(tree.root)

#f) listar las criaturas que no han sido derrotadas
print("")
print("f) Criaturas que no han sido derrotadas:")
def list_undefeated(root):
    if root:
        if not root.other_value.get('derrotado_por'):
            print(root.value)
        list_undefeated(root.left)
        list_undefeated(root.right)

list_undefeated(tree.root)

#g) cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe o dios que la capturó
def update_captured_field(tree, creature_name, captured_by):
    node = tree.search(creature_name)
    if node:
        node.other_value['capturada'] = captured_by

update_captured_field(tree, 'Cerbero', 'Heracles')
update_captured_field(tree, 'Toro de Creta', 'Heracles')
update_captured_field(tree, 'Cierva de Cerinea', 'Heracles')
update_captured_field(tree, 'Jabalí de Erimanto', 'Heracles')

#h) modificar los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de Erimanto indicando que Heracles las atrapó
# se hizo en el ejercicio g

#i) se debe permitir búsquedas por coincidencia
print("")
print("i) Búsquedas por coincidencia de 'Aves':")
tree.proximity_search('Aves')

#j) eliminar al Basilisco y a las Sirenas
print("")
print("j) Eliminar Basilisco y Sirenas:")
print("Eliminado Basilisco:", tree.delete_node('Basilisco'))
print("Eliminado Sirenas:", tree.delete_node('Sirenas'))

#k) modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles derrotó a varias
node = tree.search('Aves del Estínfalo')
if node:
    node.other_value['derrotado_por'] = 'Heracles, varias veces'
    print("")
    print("k) Heracles derrotó a varias Aves del Estínfalo")

#l) modificar el nombre de la criatura Ladón por Dragón Ladón
def update_creature_name(tree, old_name, new_name):
    node = tree.search(old_name)
    if node:
        node.value = new_name

update_creature_name(tree, 'Ladón', 'Dragón Ladón')
print("")
print("l) La criatura Ladón ahora lleva el nombre de Dragón Ladón")

#m) realizar un listado por nivel del árbol
print("")
print("m) Listado por nivel del árbol:")
tree.by_level()

#n) mostrar las criaturas capturadas por Heracles
print("")
print("n) Criaturas capturadas por Heracles:")
def list_captured_by_heracles(root):
    if root:
        if root.other_value.get('capturada') == 'Heracles':
            print(root.value)
        list_captured_by_heracles(root.left)
        list_captured_by_heracles(root.right)

list_captured_by_heracles(tree.root)