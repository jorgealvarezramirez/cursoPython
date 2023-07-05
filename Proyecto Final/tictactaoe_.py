import random


def crear_tablero():
    # Crea un tablero vacío
    tablero = []
    for _ in range(3):
        fila = [1, 2, 3]
        tablero.append(fila)
    return tablero


def imprimir_tablero(tablero):
    # Imprime el tablero en la consola
    print("+-------+-------+-------+")
    for fila in tablero:
        print("|       |       |       |")
        print(f"|   {fila[0]}   |   {fila[1]}   |   {fila[2]}   |")
        print("|       |       |       |")
        print("+-------+-------+-------+")


def obtener_movimiento_usuario(tablero):
    # Pide al usuario su movimiento y lo valida
    while True:
        movimiento = int(input("Ingresa tu movimiento: "))
        fila = (movimiento - 1) // 3
        columna = (movimiento - 1) % 3
        if 1 <= movimiento <= 9 and tablero[fila][columna] != 'O' and tablero[fila][columna] != 'X':
            return movimiento
        else:
            print("Movimiento inválido. Inténtalo de nuevo.")


def hacer_movimiento(tablero, movimiento, simbolo):
    # Realiza el movimiento en el tablero
    fila = (movimiento - 1) // 3
    columna = (movimiento - 1) % 3
    tablero[fila][columna] = simbolo


def hay_ganador(tablero, simbolo):
    # Verifica si el jugador o la máquina han ganado
    # Verificación de filas
    for fila in tablero:
        if fila.count(simbolo) == 3:
            return True
    # Verificación de columnas
    for columna in range(3):
        if tablero[0][columna] == tablero[1][columna] == tablero[2][columna] == simbolo:
            return True
    # Verificación de diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] == simbolo:
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] == simbolo:
        return True
    return False


def tablero_lleno(tablero):
    # Verifica si el tablero está lleno (empate)
    for fila in tablero:
        if any(isinstance(casilla, int) for casilla in fila):
            return False
    return True


def jugar_partida():
    tablero = crear_tablero()
    hacer_movimiento(tablero, 5, 'X')
    imprimir_tablero(tablero)

    while True:
        movimiento_usuario = obtener_movimiento_usuario(tablero)
        hacer_movimiento(tablero, movimiento_usuario, 'O')
        imprimir_tablero(tablero)

        if hay_ganador(tablero, 'O'):
            print("¡Has Ganado!")
            break

        if tablero_lleno(tablero):
            print("El juego termina en empate.")
            break

        movimiento_maquina = random.choice(
            [casilla for fila in tablero for casilla in fila if isinstance(casilla, int)])
        hacer_movimiento(tablero, movimiento_maquina, 'X')
        print("La máquina ha realizado su movimiento.")
        imprimir_tablero(tablero)

        if hay_ganador(tablero, 'X'):
            print("La máquina ha ganado.")
            break

        if tablero_lleno(tablero):
            print("El juego termina en empate.")
            break


jugar_partida()
