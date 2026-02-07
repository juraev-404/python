import pygame
import math
from settings import SHIP_SPEED

class Ship:
    def __init__(self, x, y, image):
        self.original_image = image
        self.image = image
        self.x = x
        self.y = y
        self.angle = 0  # угол в градусах, 0 — вверх
        self.rect = self.image.get_rect(center=(x, y))
        self.mask = pygame.mask.from_surface(self.image)
        self.velocity_x = 0
        self.velocity_y = 0

    def rotate(self, direction):
        """ direction = +1 вправо, -1 влево """
        self.angle += direction
        self.angle %= 360
        self.image = pygame.transform.rotate(self.original_image, self.angle*(-1))
        self.rect = self.image.get_rect(center=self.rect.center)
        self.mask = pygame.mask.from_surface(self.image)

    def move_forward(self):
        rad = math.radians(self.angle)
        self.velocity_x = SHIP_SPEED * math.sin(rad)
        self.velocity_y = -SHIP_SPEED * math.cos(rad)
        self.x += self.velocity_x
        self.y += self.velocity_y

        # Тороида
        if self.x < 0: self.x = 800
        if self.x > 800: self.x = 0
        if self.y < 0: self.y = 600
        if self.y > 600: self.y = 0

        self.rect.center = (self.x, self.y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def get_nose(self):
        """Возвращает координаты носа корабля для стрельбы"""
        rad = math.radians(self.angle)
        length = max(self.rect.width, self.rect.height) // 2
        nose_x = self.x + math.sin(rad) * length
        nose_y = self.y - math.cos(rad) * length
        return nose_x, nose_y
