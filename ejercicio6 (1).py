import math

def longitud_maxima_cuerda(diametro, percentage, ancho_cuerda):
  # Calcular el radio 
  radio = diametro / 2
  
  # Calcular el área  de hierba
  area = math.pi * radio**2
  
  # Calcular el área que queremos proteger
  area_protegida = area * percentage
  
  # Calcular la longitud máxima de la cuerda necesaria 
  longitud_cuerda = area_protegida / ancho_cuerda
  
  # Redondear la longitud de la cuerda al entero más cercano y devolverlo como resultado
  return round(longitud_cuerda)
