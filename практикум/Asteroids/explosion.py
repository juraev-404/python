# explosion.py
import pygame

class Explosion:
    def __init__(self, x, y, images):
        self.images = images
        self.index = 0
        self.image = self.images[self.index]
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(center=(x, y))
        self.counter = 0
        self.done = False

    def update(self):
        self.counter += 1
        if self.counter % 5 == 0:
            self.index += 1
            if self.index < len(self.images):
                self.image = self.images[self.index]
            else:
                self.done = True

    def draw(self, screen):
        screen.blit(self.image, self.rect)
