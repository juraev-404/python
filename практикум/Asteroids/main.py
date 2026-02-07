# main.py
import pygame, sys
from settings import *
from ship import Ship
from asteroid import Asteroid
from bullet import Bullet
from explosion import Explosion
import os

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Asteroids")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

# Фон и спрайты (или временные фигуры)
# Загружаем изображения
def load_image(name, folder='images'):
    path = os.path.join(folder, name)
    return pygame.image.load(path).convert_alpha()

bg = load_image("background.png")
ship_img = load_image("ship.png")
bullet_img = load_image("bullet.png")
asteroid_img = load_image("asteroid.png")
explosion_imgs = [load_image(f"explosion{i}.png") for i in range(1,4)]

# Объекты игры
ship = Ship(WIDTH//2, HEIGHT//2, ship_img)
bullets = []
asteroids = [Asteroid(asteroid_img) for _ in range(6)]
explosions = []

score = 0
lives = LIVES
game_over = False

# Кнопка рестарта
restart_rect = pygame.Rect(WIDTH//2-60, HEIGHT//2+60, 120, 40)

running = True
while running:
    screen.blit(bg, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if not game_over and event.key == pygame.K_SPACE:
                nx, ny = ship.get_nose()
                bullets.append(Bullet(nx, ny, ship.angle, bullet_img))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_over and restart_rect.collidepoint(event.pos):
                # сброс игры
                lives = LIVES
                score = 0
                ship.x, ship.y = WIDTH//2, HEIGHT//2
                ship.rect.center = (ship.x, ship.y)
                bullets.clear()
                asteroids.clear()
                asteroids.extend([Asteroid(asteroid_img) for _ in range(6)])
                explosions.clear()
                game_over = False

    keys = pygame.key.get_pressed()
    if not game_over:
        if keys[pygame.K_LEFT]:
            ship.rotate(-5)
        if keys[pygame.K_RIGHT]:
            ship.rotate(5)
        if keys[pygame.K_UP]:
            ship.move_forward()

        # Обновление пуль
        for bullet in bullets[:]:
            bullet.update()
            if bullet.x < 0 or bullet.x > WIDTH or bullet.y < 0 or bullet.y > HEIGHT:
                bullets.remove(bullet)
 

        # Обновление астероидов
        for asteroid in asteroids:
            asteroid.update()

        # Проверка столкновений пуль с астероидами
        for bullet in bullets[:]:
            for asteroid in asteroids[:]:
                offset = (int(asteroid.rect.x - bullet.rect.x), int(asteroid.rect.y - bullet.rect.y))
                if bullet.mask.overlap(asteroid.mask, offset):
                    bullets.remove(bullet)
                    asteroids.remove(asteroid)
                    asteroids.append(Asteroid(asteroid_img))
                    explosions.append(Explosion(asteroid.x, asteroid.y, explosion_imgs))
                    score += 1
                    break

        # Проверка столкновений корабля с астероидами
        for asteroid in asteroids:
            offset = (int(asteroid.rect.x - ship.rect.x), int(asteroid.rect.y - ship.rect.y))
            if ship.mask.overlap(asteroid.mask, offset):
                explosions.append(Explosion(ship.x, ship.y, explosion_imgs))
                lives -= 1
                ship.x, ship.y = WIDTH//2, HEIGHT//2
                ship.rect.center = (ship.x, ship.y)
                if lives <= 0:
                    game_over = True

    # Рисуем объекты
    if not game_over:
        ship.draw(screen)
        for bullet in bullets:
            bullet.draw(screen)
        for asteroid in asteroids:
            asteroid.draw(screen)
    for exp in explosions[:]:
        exp.update()
        exp.draw(screen)
        if exp.done:
            explosions.remove(exp)

    # Счет и жизни
    score_text = font.render(f"Score: {score}", True, SCORE_COLOR)
    lives_text = font.render(f"Lives: {lives}", True, FONT_COLOR)
    screen.blit(score_text, (WIDTH-120,10))
    screen.blit(lives_text, (10,10))

    # Если игра окончена — показываем Game Over и кнопку Рестарт
    if game_over:
        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.set_alpha(180)
        overlay.fill((0,0,0))
        screen.blit(overlay, (0,0))

        go_font = pygame.font.SysFont(None, 60)
        go_text = go_font.render("GAME OVER", True, (255,0,0))
        go_rect = go_text.get_rect(center=(WIDTH//2, HEIGHT//2))
        screen.blit(go_text, go_rect)

        pygame.draw.rect(screen, (180,180,180), restart_rect, border_radius=8)
        btn_text = pygame.font.SysFont(None, 32).render("RESTART", True, (0,0,0))
        btn_rect = btn_text.get_rect(center=restart_rect.center)
        screen.blit(btn_text, btn_rect)

    pygame.display.update()
    clock.tick(FPS)
