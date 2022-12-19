# la función "numbersOfLetters" que toma un entero como entrada y devuelve una lista de cadenas.

#variable "result" que sea una lista vacía sirve para almacenar la ruta desde 0 hasta el equilibrio.

#Mientras el número entero no sea igual a cuatro,Convertir el entero a una cadena de caracteres y almacenar el resultado en una variable "str_num". Agregar la cadena "str_num" al final de la lista "result". Calcular el número de letras en "str_num" y almacénelo en una variable "num_letters". Si "num_letters" es igual a cuatro, se termina el bucle. sino, convertir "num_letters" a un entero y almacenarlo en la variable "num".

#4:Después del bucle, devolver la lista "result"

def numbersOfLetters(num):
    result = []
    while num != 4:
        str_num = str(num)
        result.append(str_num)
        num_letters = len(str_num)
        if num_letters == 4:
            break
        num = int(num_letters)
    return result

print(numbersOfLetters(60))  # debe imprimir ["sixzero", "seven", "five", "four"]
print(numbersOfLetters(1))   # debe imprimir ["one", "three", "five", "four"]