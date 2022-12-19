import re
#gracias a re.IGNORECASE) nos lee independientemente de si están escritas en minúsculas o mayúsculas. La barra vertical (|) es un operador OR que indica que se deben buscar cualquiera de las tres opciones.
def encontrar(text: str) -> bool:
    # Usar una expresión regular para buscar "tree fiddy", "3.50" , "tres cincuenta" 
    match = re.search(r"tree fiddy|3\.50|three fifty", texto, re.IGNORECASE)
    if match:
        return True
    return False

texto =  "¿cuánto suele dar propina la gente por algo como esto? El artista mira hacia arriba. Siempre va a tratarse de Tree Fiddy.¡Fue entonces cuando te das cuenta de que el músico era una bestia de 400 pies de altura de la era paleolítica. ¡El Monstruo del Lago Ness casi te engaña!" 
#Output: True
print(encontrar(texto))

texto = "¿cuánto suele dar propina la gente por algo como esto? El artista mira hacia arriba. Siempre va a tratarse de Tree Fiddo.¡Fue entonces cuando te das cuenta de que el músico era una bestia de 400 pies de altura de la era paleolítica. ¡El Monstruo del Lago Ness casi te engaña!"
print(encontrar(texto))  # Output: False
