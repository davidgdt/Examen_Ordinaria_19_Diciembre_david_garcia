from datetime import datetime

def count_mondays(cumpleaños: str, current_date: str) -> int:
    # Analizar las fechas y calcular la edad
  #%Y = año
  #%m = mes 
  #%d = dia
    cumple = datetime.strptime(birthday, "%Y-%m-%d")
    curr = datetime.strptime(current_date, "%Y-%m-%d")
    edad = (curr.year -cumple.year) - ((curr.month, curr.day) < (cumple.month, cumple.day))

    # Comprobar si la persona está en edad de trabajar
    if edad < 22 or edad > 78:
        return 0

    # Calcular el número de lunes entre el cumpleaños y la fecha actual
    num_mondays = (curr - cumple).days // 7

    return num_mondays





