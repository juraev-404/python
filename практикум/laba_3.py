import pygame
import sys

pygame.init()

# Размер окна
size = 300
screen = pygame.display.set_mode((size, size))
pygame.display.set_caption("Крестики-Нолики")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)
BLUE  = (0, 0, 255)
GREEN = (0, 128, 0)
GRAY  = (180, 180, 180)

# Игровое поле
board = [["" for _ in range(3)] for _ in range(3)]
cell = size // 3
turn = "X"
winner = None
draw = False

font = pygame.font.SysFont(None, 48)
btn_font = pygame.font.SysFont(None, 32)

# Кнопка рестарта
restart_rect = pygame.Rect(size//2 - 60, size - 60, 120, 40)

def reset_game():
    global board, turn, winner, draw
    board = [["" for _ in range(3)] for _ in range(3)]
    turn = "X"
    winner = None
    draw = False

def check_win(player):
    # строки, столбцы
    for i in range(3):
        if all(board[i][j] == player for j in range(3)): return True
        if all(board[j][i] == player for j in range(3)): return True
    # диагонали
    if all(board[i][i] == player for i in range(3)): return True
    if all(board[i][2-i] == player for i in range(3)): return True
    return False

def board_full():
    return all(board[i][j] != "" for i in range(3) for j in range(3))


running = True
while running:
    screen.fill(WHITE)

    # Рисуем сетку
    pygame.draw.line(screen, BLACK, (cell, 0), (cell, size), 3)
    pygame.draw.line(screen, BLACK, (2*cell, 0), (2*cell, size), 3)
    pygame.draw.line(screen, BLACK, (0, cell), (size, cell), 3)
    pygame.draw.line(screen, BLACK, (0, 2*cell), (size, 2*cell), 3)

    # Рисуем X и O
    for i in range(3):
        for j in range(3):
            x = j * cell
            y = i * cell
            if board[i][j] == "X":
                pygame.draw.line(screen, RED, (x+20, y+20), (x+cell-20, y+cell-20), 4)
                pygame.draw.line(screen, RED, (x+cell-20, y+20), (x+20, y+cell-20), 4)
            elif board[i][j] == "O":
                pygame.draw.circle(screen, BLUE, (x+cell//2, y+cell//2), cell//2 - 15, 4)

    # Сообщение о победе или ничьей
    if winner or draw:
        msg = f"Победил {winner}!" if winner else "Ничья!"
        text = font.render(msg, True, (255, 255, 255))
        rect = text.get_rect(center=(size//2, size//2 - 20))

        bg_rect = rect.inflate(40, 20)
        pygame.draw.rect(screen, GREEN, bg_rect, border_radius=10)
        screen.blit(text, rect)

        # Кнопка рестарта
        pygame.draw.rect(screen, GRAY, restart_rect, border_radius=8)
        btn_text = btn_font.render("Рестарт", True, BLACK)
        btn_rect = btn_text.get_rect(center=restart_rect.center)
        screen.blit(btn_text, btn_rect)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()

            # Если есть победитель или ничья → проверяем кнопку рестарта
            if winner or draw:
                if restart_rect.collidepoint(mx, my):
                    reset_game()
                continue

            # Игровые ходы
            row = my // cell
            col = mx // cell

            if board[row][col] == "":
                board[row][col] = turn

                if check_win(turn):
                    winner = turn
                elif board_full():
                    draw = True
                else:
                    turn = "O" if turn == "X" else "X"

    pygame.display.update()
