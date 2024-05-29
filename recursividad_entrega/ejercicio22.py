def usar_la_fuerza(mochila):
    if not mochila:
        return "No se encontro el sable de luz en la mochila"
    
    objeto = mochila.pop()

    if objeto == "sable de luz":
        print("encontraste el sable de luz en la mochila")
        return f"Se necesitaron {len(mochila)} objetos para encontrar el sable de luz en la mochila"
    else:
        return usar_la_fuerza(mochila)
    
#ejemplo
mochila = ["lapices", "cuadernillo", "sacapuntas", "sable de luz", "mate", "celular"]
print(usar_la_fuerza(mochila))

#otro ejemplo
mochila = ["lapices", "cuadernillo", "sacapuntas", "notebook", "mate", "celular"]
print(usar_la_fuerza(mochila))