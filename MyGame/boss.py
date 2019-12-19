"""boss"""
import pygame
import random


class Boss(pygame.sprite.Sprite):
    """boss"""

    def __init__(self, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.width = width
        self.height = height
        self.image = pygame.image.load(r'image/tianxie.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.bottom = random.randint(0 + self.rect.width, self.width - self.rect.width), 0
        self.speed = [random.randint(-3, 3), random.randint(2, 5)]
        self.active = True

    def move(self):
        """move"""
        self.rect = self.rect.move(self.speed)
        if self.rect.right < 0 or self.rect.left > self.width or self.rect.top > self.height:
            self.active = False

    def reset(self):
        """reset"""
        self.rect.left, self.rect.bottom = random.randint(0, self.width - self.rect.width), 0
        self.speed = [random.randint(-10, 10), random.randint(1, 10)]
