import random


def create_board():
    # Crea un tablero vacío
    board = []
    for _ in range(3):
        row = [1, 2, 3]
        board.append(row)
    return board


def print_board(board):
    # Imprime el tablero en la consola
    print("+-------+-------+-------+")
    for row in board:
        print("|       |       |       |")
        print(f"|   {row[0]}   |   {row[1]}   |   {row[2]}   |")
        print("|       |       |       |")
        print("+-------+-------+-------+")


def get_user_move(board):
    # Pide al usuario su movimiento y lo valida
    while True:
        move = int(input("Ingresa tu movimiento: "))
        row = (move - 1) // 3
        col = (move - 1) % 3
        if 1 <= move <= 9 and board[row][col] != 'O' and board[row][col] != 'X':
            return move
        else:
            print("Movimiento inválido. Inténtalo de nuevo.")


def make_move(board, move, symbol):
    # Realiza el movimiento en el tablero
    row = (move - 1) // 3
    col = (move - 1) % 3
    board[row][col] = symbol


def is_winner(board, symbol):
    # Verifica si el jugador o la máquina han ganado
    # Verificación de filas
    for row in board:
        if row.count(symbol) == 3:
            return True
    # Verificación de columnas
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == symbol:
            return True
    # Verificación de diagonales
    if board[0][0] == board[1][1] == board[2][2] == symbol:
        return True
    if board[0][2] == board[1][1] == board[2][0] == symbol:
        return True
    return False


def is_board_full(board):
    # Verifica si el tablero está lleno (empate)
    for row in board:
        if any(isinstance(cell, int) for cell in row):
            return False
    return True


def play_game():
    board = create_board()
    make_move(board, 5, 'X')
    print_board(board)

    while True:
        user_move = get_user_move(board)
        make_move(board, user_move, 'O')
        print_board(board)

        if is_winner(board, 'O'):
            print("¡Has Ganado!")
            break

        if is_board_full(board):
            print("El juego termina en empate.")
            break

        machine_move = random.choice(
            [cell for row in board for cell in row if isinstance(cell, int)])
        make_move(board, machine_move, 'X')
        print("La máquina ha realizado su movimiento.")
        print_board(board)

        if is_winner(board, 'X'):
            print("La máquina ha ganado.")
            break

        if is_board_full(board):
            print("El juego termina en empate.")
            break


play_game()
