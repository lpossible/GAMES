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
        self.rect.left, self.rect.top = random.randint(0, self.width - self.rect.width), random.randint(
            -6 * self.height, -4 * self.height)
        self.speed = [0, random.randint(1, 3)]
        self.active = True

    def move(self):
        """move"""
        self.rect = self.rect.move(self.speed)
        if self.rect.top > self.height:
            self.active = False

    def reset(self):
        """reset"""
        self.rect.left, self.rect.top = random.randint(0, self.width - self.rect.width), random.randint(
            -6 * self.height, -4 * self.height)
        self.speed = [0, random.randint(2, 5)]
