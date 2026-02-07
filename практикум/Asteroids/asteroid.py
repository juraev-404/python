# asteroid.py
import pygame
import random
from settings import WIDTH, HEIGHT, ASTEROID_SPEED_MIN, ASTEROID_SPEED_MAX

class Asteroid:
    def __init__(self, image):
        self.image = image
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.speed_x = random.uniform(ASTEROID_SPEED_MIN, ASTEROID_SPEED_MAX) * random.choice([-1,1])
        self.speed_y = random.uniform(ASTEROID_SPEED_MIN, ASTEROID_SPEED_MAX) * random.choice([-1,1])
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y

        # Тороида
        if self.x < 0: self.x = 800
        if self.x > 800: self.x = 0
        if self.y < 0: self.y = 600
        if self.y > 600: self.y = 0

        self.rect.center = (self.x, self.y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
