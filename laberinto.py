
from collections import deque

# Laberinto: 0 = pared
laberinto = [
    [1, 1, 1, 3, 0, 1, 1, 1, 4],
    [3, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 3, 1, 1],
    [3, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 3, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 4],
    [1, 1, 3, 1, 0, 1, 1, 1, 1]
]

inicio = (8, 0)
final = (0, 0)

# Arriba, derecha, abajo, izquierda
movimientos = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def mostrar_original():
    print("LABERINTO ORIGINAL")
    for i in range(9):
        fila = []
        for j in range(9):
            if (i, j) == inicio:
                fila.append(" I")
            elif (i, j) == final:
                fila.append(" F")
            else:
                fila.append(f"{laberinto[i][j]:2}")
        print(" ".join(fila))


def buscar_camino():
    # Cada estado contiene posición, puntos y camino recorrido
    cola = deque()
    cola.append((inicio, 1, [inicio]))

    # Guarda la mejor puntuación alcanzada en cada posición
    mejores = {inicio: 1}

    while cola:
        posicion, puntos, camino = cola.popleft()
        fila, columna = posicion

        # Comprobar si llegamos al final
        if posicion == final:
            if puntos >= 23:
                return camino, puntos
            continue

        for df, dc in movimientos:
            nf = fila + df
            nc = columna + dc
            nueva = (nf, nc)

            # Verificar límites y paredes
            if not (0 <= nf < 9 and 0 <= nc < 9):
                continue

            if laberinto[nf][nc] == 0:
                continue

            nuevos_puntos = puntos + laberinto[nf][nc]

            # Evitar estados que no mejoran la puntuación
            if nuevos_puntos <= mejores.get(nueva, -1):
                continue

            mejores[nueva] = nuevos_puntos
            nuevo_camino = camino + [nueva]
            cola.append((nueva, nuevos_puntos, nuevo_camino))

    return None, 0


def mostrar_resultado(camino, puntos):
    print("\nMATRIZ DEL CAMINO")
    conjunto = set(camino)

    for i in range(9):
        fila = []
        for j in range(9):
            pos = (i, j)

            if pos == inicio:
                fila.append(" I")
            elif pos == final:
                fila.append(" F")
            elif pos in conjunto:
                fila.append(" *")
            elif laberinto[i][j] == 0:
                fila.append(" 0")
            else:
                fila.append(" .")

        print(" ".join(fila))

    print("\nPuntos acumulados:", puntos)
    print("Camino:", camino)


# Programa principal
mostrar_original()

camino, puntos = buscar_camino()

if camino is not None:
    print("\n¡Se encontró una salida válida!")
    mostrar_resultado(camino, puntos)
else:
    print("\nNo se encontró una salida con 23 puntos o más.")
