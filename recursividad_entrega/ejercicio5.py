#5 numeros romanos 
def romano_a_decimal(romano):
    # Diccionario de valores de los números romanos
    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    # Caso base: si la cadena está vacía, el número es 0
    if not romano:
        return 0
    
    # Caso base: si la cadena tiene un solo carácter, devolver su valor
    if len(romano) == 1:
        return valores[romano[0]]
    
    # Obtener el valor del primer carácter
    primer_valor = valores[romano[0]]
    # Obtener el valor del segundo carácter
    segundo_valor = valores[romano[1]]
    
    # Si el primer valor es mayor o igual al segundo, sumar el primer valor y continuar con el resto
    if primer_valor >= segundo_valor:
        return primer_valor + romano_a_decimal(romano[1:])
    # Si el primer valor es menor que el segundo, restar el primer valor y continuar con el resto
    else:
        return -primer_valor + romano_a_decimal(romano[1:])

# Ejemplo de uso
numero_romano = "MCMXCIV"
numero_decimal = romano_a_decimal(numero_romano)
print(f"El número romano {numero_romano} es {numero_decimal} en decimal.")