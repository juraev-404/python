
# ''' IMPORTS '''

# #import curses # for coloured triangulation
# import os
# import random


# # simple cross platform clear screen
# def clearScreen():
#     if os.name == 'posix':
#         os.system('clear')
#     else:
#         os.system('cls')


# # print the basic intro message
# def prIntro ():
#     clearScreen()
#     print('Time to play MAXIT!\n'
#           'Basic gameplay is as follows:\n'
#           ' - you are player 1\n'
#           ' - each player alternates turns\n'
#           ' - select element in same row or colum as current position\n'
#           ' - value of selected element gets added to player total\n'
#           ' - selected element becomes next player position\n'
#           ' - game ends once all sections on the grid have been selected\n'
#           ' - highest total score wins\n')
#     return


# # pretty print the game board
# def printBoard( mboard, msize ):
#     print('MAXIT Board Game\n')

#     if (mboard==[]):
#         print('-- empty board --\n')
#         return

#     print('   0 ||', end='')
#     for col in range(msize):
#         print('%4d |' %(col+1), end='')
#     print('\n ------', end='')
#     for col in range(msize):
#         print('------', end='')
#     for row in range(msize):
#         if (row >= 0):
#             print('\n%4d ||' %(row+1), end='')

#         for col in range(msize):
#             #form = '%' + str(max(msize)) + 's'
#             print('%4s |' %str(mboard[row][col]), end='')
#     print('\n')
#     return


# # print the current player stats
# def printStats( mplayers, mcurPlayer, mcurPos):
#     print('%s' %mplayers[0][0] + '\'s Score: %s'  %mplayers[1][0])
#     print('%s' %mplayers[0][1] + '\'s Score: %s'  %mplayers[1][1])
#     print('\nCurrent Player: ' + mplayers[0][mcurPlayer])
#     print('Current Position: [%d, ' %(mcurPos[0]) + '%d]' %(mcurPos[1]))
#     return


# # get board size
# def getSize():
#     is_legit = 0
#     while not is_legit:
#         try:
#             msize = int (input('Enter board size: ' ))
#             if msize > 30:
#                 print('Don\'t be a twat. Pick a smaller size.')
#             elif msize > 0:
#                 is_legit = 1
#         except ValueError:
#             print('Please enter board size as a number.')
#     return msize


# # setup board
# def setBoard( size ):
#     mboard = [[random.randint(-9,15) for col in range(size)] for row in range(size)]
#     return mboard


# # check for available moves
# def checkMoves( mcurPos, mboard, msize ):
#     for row in range(msize):
#         for col in range(msize):
#             print('- checking [%d, %d]', row, col)
#             if row == (mcurPos[0]-1):
#                 print(' - - testing [%d, %d]', row, col)
#                 if mboard[row][col] != '-':
#                     return 1
#             elif col == (mcurPos[1]-1):
#                 print(' - - testing [%d, %d]', row, col)
#                 if mboard[row][col] != '-':
#                     return 1
#     return 0


# # computer AI and play
# # to later be updated for different levels of difficulty
# # level 0: random next move
# # level 1: highest possible
# # level 2: highest possible mapped out combos
# def computerAI( mcurPos, mboard, msize ):
#     maxNum = -10
#     newPos = [0,0]
#     aiMoves = [[],[],[]]

#     for row in range(msize):
#         for col in range(msize):
#             if row == (mcurPos[0]-1):
#                 if mboard[row][col] != '-':
#                     if int(mboard[row][col]) > maxNum:
#                         maxNum = mboard[row][col]
#                         newPos[0] = row+1
#                         newPos[1] = col+1
#             elif col == (mcurPos[1]-1):
#                 if mboard[row][col] != '-':
#                     if int(mboard[row][col]) > maxNum:
#                         maxNum = mboard[row][col]
#                         newPos[0] = row+1
#                         newPos[1] = col+1
#     print('\nComputer chooses: [%s, ' %newPos[0] + '%d]' %newPos[1])
#     beepBoop = input('\n(press enter to continue)\n')
#     return newPos


# # return player's selected choice
# def getMove( mcurPlayer, mcurPos, mboard, msize ):
#     is_legit = 0
#     newPos = [0,0]
#     while not is_legit:
#         try:
#             if mcurPlayer == 1:
#                 return computerAI(mcurPos, mboard, msize)
#             else:
#                 newPos[0] = int(input('\nSelect row: '))
#                 newPos[1] = int(input('Select column: '))
#                 if newPos[0] == mcurPos[0]:
#                     if mboard[newPos[0]-1][newPos[1]-1] != '-':
#                         is_legit = 1
#                 elif newPos[1] == mcurPos[1]:
#                     if mboard[newPos[0]-1][newPos[1]-1] != '-':
#                         is_legit = 1
#         except ValueError:
#             print('Hint: new [row, column] must be in same row or column from current.')
#     return newPos


# # simply update players
# def updatePlayer( mcurPlayer ):
#     return ( mcurPlayer + 1 ) % 2


# # init players
# # get board size
# # build the board
# # start the game
# def mainMaxit():

#     prIntro()

#     # init players, scores, boardsize, board, current player, & position
#     players = [['Human', 'Computer'], [0, 0]]
#     size = getSize()
#     board = setBoard( size )
#     curPlayer = random.randint(0,1)
#     curPos = [random.randint(1, size), random.randint(1, size)]

#     gametime = 1

#     while gametime:
#         clearScreen()
#         printBoard(board, size)
#         printStats(players, curPlayer, curPos)
#         curPos = getMove(curPlayer, curPos, board, size)
#         players[1][curPlayer] += board[curPos[0]-1][curPos[1]-1]
#         board[curPos[0]-1][curPos[1]-1] = '-'
#         curPlayer = updatePlayer(curPlayer)

#         # check for possible moves to do.
#         gametime  = checkMoves(curPos, board, size)

#     # end game stats
#     clearScreen()
#     printBoard(board, size)
#     printStats(players, curPlayer, curPos)
#     finalize = input('\nGAME OVER!\n\n(press enter to continue)')
#     return

# def controlMaxit():
#     userChoice = 0
#     anyKey = 0
#     while (userChoice != 2) :
#         clearScreen()
#         print('Welcome to the Most Awesome Xciting Inside Terminal game (MAXIT)!\n\n'
#               'Options\n'
#               '\t1. Play Maxit\n'
#               '\t2. Exit Maxit\n')
#               #'\t3. Test Maxit\n'
#         try:
#             userChoice = int (input('Enter your choice: '))
#             if (userChoice == 1):
#                 mainMaxit()
#             elif (userChoice == 2):
#                 print('\nThanks for playing MAXIT!\n')
#                 break
#             # elif (userChoice == 3):
#             #    testmaxit.testall()
#             #    anyKey = input('Testing completed! See log for details. (press enter to continue) ')
#         except ValueError:
#             anyKey = input('Please enter a valid choice. (press enter to continue) ')

#     return

# controlMaxit()

import random

# Размер поля
board_size = int(input("Введите размер поля: "))

# Генерация случайного поля
board = [[random.randint(1, 9) for _ in range(board_size)] for _ in range(board_size)]

# Инициализация индикаторов
score = [0, 0]  # Очки для каждого игрока
current_player = 0  # Текущий игрок (0 — первый игрок, 1 — второй игрок)
is_first_turn = True  # Первый ход
row_index = 0  # Строка, на которой должен ходить второй игрок
col_index = 0  # Столбец, на котором должен ходить первый игрок

# Печать игрового поля
def print_board():
    print('   ', ' '.join(map(str, range(1, board_size+1))))
    print('   ', '- ' * board_size)
    for row_num, row in enumerate(board, start=1):
        print(f'{row_num}| ', ' '.join(map(str, row)))

# Проверка, есть ли у игрока 1 доступные ходы в его строке
def has_available_moves_in_row(row):
    return any(cell != '-' for cell in board[row])

# Проверка, есть ли у игрока 2 доступные ходы в его столбце
def has_available_moves_in_column(col):
    return any(board[row][col] != '-' for row in range(board_size))

# Проверка, завершена ли игра (нет доступных ходов ни у одного игрока)
def is_game_over():
    row_moves = any(has_available_moves_in_row(row) for row in range(board_size))
    col_moves = any(has_available_moves_in_column(col) for col in range(board_size))
    return not (row_moves or col_moves)

# Инициализация игры
print_board()
move_2 = None
# Игра продолжается, пока есть возможные ходы
while True:
    print(f'Текущие очки: Игрок 1 - {score[0]}, Игрок 2 - {score[1]}')

    if is_first_turn:
        # Первый ход: вводим два координата (строка и столбец)
        move = input("Игрок 1, введите координаты (строка столбец): ").split()
        row_index, col_index = int(move[0]) - 1, int(move[1]) - 1
        selected_value = board[row_index][col_index]
        board[row_index][col_index] = '-'
        is_first_turn = False
    else:
        if is_game_over():
            print("Игра окончена! Нет доступных ходов.")
            print(f'Финальные очки: Игрок 1 - {score[0]}, Игрок 2 - {score[1]}')
            break

        if current_player == 0:
            # Проверяем, есть ли доступные ходы в строке игрока 1
            if not has_available_moves_in_column(row_index):
                print("У Игрока 1 нет доступных ходов, ход переходит к Игроку 2.")
                current_player = 1  # Ход передается Игроку 2
                move = move_2
                continue

            # Игрок 1 вводит строку
            row_index = int(input("Игрок 1, введите координату строки: ")) - 1
            move_2 = move
            
            # Проверка доступности выбранной клетки
            if board[row_index][col_index] == '-':
                print("Эта клетка уже выбрана, ход переходит к Игроку 2.")
                current_player = 1
                continue

            selected_value = board[row_index][col_index]
            board[row_index][col_index] = '-'
        else:
            # Проверяем, есть ли доступные ходы в столбце игрока 2
            if not has_available_moves_in_row(col_index):
                print("У Игрока 2 нет доступных ходов, ход переходит к Игроку 1.")
                current_player = 0  # Ход передается Игроку 1
                move = move_2
                continue

            # Игрок 2 вводит столбец
            col_index = int(input("Игрок 2, введите координату столбца: ")) - 1
            move_2 = move 
            
            # Проверка доступности выбранной клетки
            if board[row_index][col_index] == '-':
                print("Эта клетка уже выбрана, ход переходит к Игроку 1.")
                current_player = 0
                continue

            selected_value = board[row_index][col_index]
            board[row_index][col_index] = '-'
    
    # Обновление очков текущего игрока
    score[current_player] += int(selected_value)

    # Переключение игрока
    current_player = 1 - current_player

    # Печать игрового поля после хода
    print_board()