def xbonacci(signature, n):
    # Comprobar si la longitud de la firma es mayor que n
    if len(signature) > n:
        return signature[:n]

    # Iniciar la secuencia xbonacci con la firma
    xbonacci = signature.copy()

    # Generar la secuencia xbonacci
    for i in range(len(signature), n):
        xbonacci.append(sum(xbonacci[-len(signature):]))

    return xbonacci