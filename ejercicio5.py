import sys
#creo la funcion que dependa de la altura
def  funcion_hollow_triangle (altura):

    if altura == 0:
        return []
    if altura == 1:
        return ["#"]
    if altura == 2:
        return ["##", "#_#"]

    triangulo = ["_" * (2 * altura - 1)]
    for i in range(1, altura - 1):
        triangulo.append("" * (altura - i - 1) + "#" + "" * (2 * i - 1) + "#" + "_" * (altura - i - 1))
    triangulo.append("#" * (2 * altura - 1))

    return triangulo