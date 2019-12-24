"""小兵类"""
import pygame


class Enemy:
    """小兵类"""

    def __init__(self):
        self.img = pygame.image.load(r'image/car.png').convert_alpha()
        self.rect = self.img.get_rect()
        self.rect.left, self.rect.top = 190, 405
        self.speed = [0, -1]
        self.active = True
        self.health = 100

    def move(self):
        """移动"""
        self.rect = self.rect.move(self.speed)
        if self.rect.top == 321 and self.rect.left == 190:
            self.img = pygame.transform.rotate(self.img, 270)
            self.speed = [1, 0]
        if self.rect.top == 321 and self.rect.left == 430:
            self.img = pygame.transform.rotate(self.img, 270)
            self.speed = [0, -1]
        if self.rect.top == 242 and self.rect.left == 430:
            self.img = pygame.transform.rotate(self.img, 90)
            self.speed = [-1, 0]
        if self.rect.top == 242 and self.rect.left == 270:
            self.img = pygame.transform.rotate(self.img, 270)
            self.speed = [0, -1]
        if self.rect.top == 160 and self.rect.left == 270:
            self.img = pygame.transform.rotate(self.img, 270)
            self.speed = [1, 0]
        if self.rect.top == 160 and self.rect.left == 535:
            self.img = pygame.transform.rotate(self.img, 270)
            self.speed = [0, 1]
        if self.rect.top == 243 and self.rect.left == 535:
            self.img = pygame.transform.rotate(self.img, 270)
            self.speed = [1, 0]
        if self.rect.top == 243 and self.rect.left == 668:
            self.img = pygame.transform.rotate(self.img, 270)
            self.speed = [0, -1]
        if self.rect.top < 103:
            self.active = False
