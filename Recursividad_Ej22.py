#ejercicio 22
def usar_la_fuerza(mochila):
    #Caso:si la mochila esta vacía, devuelve -1
    if not mochila:
        return "No se encontró el sable de luz"

    #sacar un objeto de la mochila
    objeto = mochila.pop()

    #si el objeto es un sable de luz, devuelve el numero de objetos sacados
    if objeto == "sable de luz":
        print("¡encontraste el sable de luz!")
        return f"se necesitaron {len(mochila)} objetos para encontrar el sable de luz"
    else:
        return usar_la_fuerza(mochila)

#prueba de funcion
mochila = ["celu", "lapiz", "cartuchera", "sable de luz", "carpeta"] #vector
print(usar_la_fuerza(mochila))