from collections import deque

# Convierte una posición de notación algebraica a coordenadas (fila, columna)
# en un tablero de 8x8.
def algebraica_a_coordenada(position):
    column = ord(position[0]) - ord('a') + 1
    row = int(position[1])
    return row, column

# Convierte coordenadas (fila, columna) en un tablero de 8x8 a notación algebraica.
def coordinadas_a_algebraica(row, column):
    column = chr(column - 1 + ord('a'))
    return column + str(row)

# Devuelve una lista de las posiciones a las que el caballo puede moverse
# desde una posición dada en un tablero de 8x8.
def movimientos_validos(row, column):
    moves = []
    moves.append((row + 2, column + 1))
    moves.append((row + 2, column - 1))
    moves.append((row - 2, column + 1))
    moves.append((row - 2, column - 1))
    moves.append((row + 1, column + 2))
    moves.append((row + 1, column - 2))
    moves.append((row - 1, column + 2))
    moves.append((row - 1, column - 2))

    # Filtrar movimientos inválidos (fuera del tablero)
    movimientosvalidos = [move for move in moves if move[0] >= 1 and move[0] <= 8 and move[1] >= 1 and move[1] <= 8]

    return valid_moves

# Devuelve el menor número de movimientos que le tomaría a un caballo pasar de
# una posición a otra en un tablero de ajedrez. Las posiciones se pasan en

def knight(position1, position2):
    # Convertir posiciones a coordenadas
    start_row, start_column = algebraica_a_coordenada(position1)
    end_row, end_column = algebraica_a_coordenada(position2)

    # Crear matriz de 8x8 que representa el tablero de ajedrez
    board = [[-1 for _ in range(8)] for _ in range(8)]
    board[start_row - 1][start_column - 1] = 0

    # Realizar búsqueda BFS
    queue = deque()
    queue.append((start_row, start_column))
    while queue:
        row, column = queue.popleft()
        if row == end_row and column == end_column:
            break

        # Generar movimientos válidos del caballo y marcarlos en la matriz
        for move in movimientos_validos(row, column):
