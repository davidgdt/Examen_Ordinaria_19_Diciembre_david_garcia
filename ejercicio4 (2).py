import math

def do_math(s: str) -> int:
    # Separar la cadena en una lista de números
    nums = s.split()
    
    # Crear un diccionario para almacenar los números y las letras
    d = {}
    

    for num in nums:
        for c in num:
            if c.isalpha():
                d[c] = int(num)
                break
    
    # Ordenar el diccionario según las letras del alfabeto
    sorted_nums = [d[k] for k in sorted(d)]
    
    # Realizar los cálculos especificados en el enunciado utilizando los números ordenados del diccionario
    result = sorted_nums[0]
    for i in range(1, len(sorted_nums), 2):
        result += sorted_nums[i]
    for i in range(2, len(sorted_nums), 2):
        result -= sorted_nums[i]
    for i in range(3, len(sorted_nums), 4):
        result *= sorted_nums[i]
    for i in range(4, len(sorted_nums), 4):
        result = math.floor(result / sorted_nums[i])
    
    # Redondear el resultado final al entero más cercano
    return round(result)
