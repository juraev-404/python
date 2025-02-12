# BOARD_SIZE = 8

# def initialize_board():
#     return [['x'] * BOARD_SIZE for _ in range(BOARD_SIZE)]

# def print_board(board):
#     print("Текущее состояние поля:")
#     for row in board:
#         print(" ".join(str(cell) for cell in row))
#     print()

# def game_over(board):
#     return all(cell == 0 for row in board for cell in row)

# def remove_chips(board, line, is_row):
#     if is_row:
#         board[line] = [' '] * BOARD_SIZE
#     else:
#         for i in range(BOARD_SIZE):
#             board[i][line] = ' '

# def get_move(board, player):
#     while True:
#         print(f"Игрок {player}, выберите строку или столбец для снятия фишек.")
#         choice = input("Введите 'r <номер строки>' или 'c <номер столбца>': ").strip().split()

#         if len(choice) != 2:
#             print("Неверный ввод! Попробуйте снова.")
#             continue

#         move_type, index = choice
#         if move_type not in ['r', 'c']:
#             print("Неверный выбор! Используйте 'r' для строки или 'c' для столбца.")
#             continue

#         try:
#             index = int(index)
#         except ValueError:
#             print("Неверный номер! Попробуйте снова.")
#             continue

#         if index < 0 or index >= BOARD_SIZE:
#             print("Неверный номер строки или столбца! Он должен быть от 0 до 7.")
#             continue

#         if move_type == 'r' and any(board[index]):
#             return index, True
#         elif move_type == 'c' and any(board[i][index] for i in range(BOARD_SIZE)):
#             return index, False
#         else:
#             print("Выбрана линия без фишек! Попробуйте снова.")

# def play_game():
#     board = initialize_board()
#     player = 1

#     while not game_over(board):
#         print_board(board)
#         line, is_row = get_move(board, player)
#         remove_chips(board, line, is_row)

#         if game_over(board):
#             print_board(board)
#             print(f"Игрок {player} победил!")
#             break

#         player = 3 - player

# # if name == "__main__":
# play_game()

import random

BOARD_SIZE = 8

def initialize_board():
    board = [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)]
    num_chips = random.randint(1, BOARD_SIZE * BOARD_SIZE)  # Случайное количество фишек
    for _ in range(num_chips):
        while True:
            row = random.randint(0, BOARD_SIZE - 1)
            col = random.randint(0, BOARD_SIZE - 1)
            if board[row][col] == 0:  # Размещаем фишку, если ячейка свободна
                board[row][col] = 1
                break
    return board

def print_board(board):
    print("Текущее состояние поля:")
    for row in board:
        print(" ".join(str(cell) for cell in row))
    print()

def game_over(board):
    return all(cell == 0 for row in board for cell in row)

def remove_chips(board, line, is_row):
    if is_row:
        board[line] = [0] * BOARD_SIZE
    else:
        for i in range(BOARD_SIZE):
            board[i][line] = 0

def get_move(board, player):
    while True:
        print(f"Игрок {player}, выберите строку или столбец для снятия фишек.")
        choice = input("Введите 'r <номер строки>' или 'c <номер столбца>': ").strip().split()

        if len(choice) != 2:
            print("Неверный ввод! Попробуйте снова.")
            continue

        move_type, index = choice
        if move_type not in ['r', 'c']:
            print("Неверный выбор! Используйте 'r' для строки или 'c' для столбца.")
            continue

        try:
            index = int(index)
        except ValueError:
            print("Неверный номер! Попробуйте снова.")
            continue

        if index < 0 or index >= BOARD_SIZE:
            print("Неверный номер строки или столбца! Он должен быть от 0 до 7.")
            continue

        if move_type == 'r' and any(board[index]):
            return index, True
        elif move_type == 'c' and any(board[i][index] for i in range(BOARD_SIZE)):
            return index, False
        else:
            print("Выбрана линия без фишек! Попробуйте снова.")

def play_game():
    board = initialize_board()
    player = 1

    while not game_over(board):
        print_board(board)
        line, is_row = get_move(board, player)
        remove_chips(board, line, is_row)

        if game_over(board):
            print_board(board)
            print(f"Игрок {player} победил!")
            break

        player = 3 - player

play_game()