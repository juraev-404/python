import pygame
import math

class Bullet:
    def __init__(self, x, y, angle, image):
        self.image = image
        self.x = x
        self.y = y
        self.angle = angle
        rad = math.radians(angle)
        self.dx = 12 * math.sin(rad)
        self.dy = -12 * math.cos(rad)
        self.rect = self.image.get_rect(center=(x, y))
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.rect.center = (self.x, self.y)

    def draw(self, screen):
        rotated = pygame.transform.rotate(self.image, self.angle)
        rect = rotated.get_rect(center=self.rect.center)
        screen.blit(rotated, rect)
