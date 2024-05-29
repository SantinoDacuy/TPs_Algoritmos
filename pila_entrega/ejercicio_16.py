# Ejercicio 16
#Se tienen dos pilas con personajes de Star Wars, en una los del episodio V de “The empirestrikes back” y la 
#otra los del episodio VII “The force awakens”. Desarrollar un algoritmo que permita obtener
#la intersección de ambas pilas, es decir los personajes que aparecen en ambos episodios.
from pila import Stack

#creamos las dos pilas con los personajes de Star Wars por un lado episodio V y por el otro episodio VII
episodio_V = Stack()
episodio_V.push("Luke Skywalker")
episodio_V.push("Darth Vader")
episodio_V.push("Leia Organa")
episodio_V.push("Han Solo")
episodio_V.push("Yoda")

episodio_VII = Stack()
episodio_VII.push("Rey")
episodio_VII.push("Kylo Ren")
episodio_VII.push("Finn")
episodio_VII.push("Luke Skywalker")
episodio_VII.push("Leia Organa")

#definimos la función para obtener la intersección de las dos pilas
def interseccion_pilas(pila1, pila2):
    pila_aux1 = Stack()
    pila_aux2 = Stack()
    interseccion = Stack()
    
    #pasamos todos los elementos de pila1 a una pila auxiliar
    while pila1.size() > 0:
        elemento = pila1.pop()
        pila_aux1.push(elemento)
    
    #pasamos todos los elementos de pila2 a una pila auxiliar
    while pila2.size() > 0:
        elemento = pila2.pop()
        pila_aux2.push(elemento)
    
    #comparamos los elementos de ambas pilas
    while pila_aux1.size() > 0:
        elemento1 = pila_aux1.pop()
        pila_aux2_copia = Stack()
        
        while pila_aux2.size() > 0:
            elemento2 = pila_aux2.pop()
            pila_aux2_copia.push(elemento2)
            
            if elemento1 == elemento2:
                interseccion.push(elemento1)
        
        #restauramos la pila2 auxiliar
        while pila_aux2_copia.size() > 0:
            pila_aux2.push(pila_aux2_copia.pop())
    
    #restauramos las pilas originales
    while pila_aux1.size() > 0:
        pila1.push(pila_aux1.pop())
    
    while pila_aux2.size() > 0:
        pila2.push(pila_aux2.pop())
    
    return interseccion

#obtenemos la intersección de las pilas de personajes
personajes_ambos_episodios = interseccion_pilas(episodio_V, episodio_VII)

#por ultimo mostramos los personajes que aparecen en ambos episodios
print("Personajes que estan en ambos episodios:")
while personajes_ambos_episodios.size() > 0:
    print(personajes_ambos_episodios.pop())