"""TOWER"""
import pygame
import math


class Tower(pygame.sprite.Sprite):
    """tower"""

    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.img0 = pygame.image.load('image/tower0.png')
        self.img1 = pygame.image.load('image/tower1.png')
        self.img2 = pygame.image.load('image/tower2.png')
        self.rect = self.img0.get_rect()
        self.rect.left, self.rect.top = pos
        self.count = 1

    def draw(self, screen):
        """绘制"""
        if self.count > 90:
            self.count = 1
        if 1 <= self.count < 30:
            screen.blit(self.img0, self.rect)
        elif 30 <= self.count < 60:
            screen.blit(self.img1, self.rect)
        else:
            screen.blit(self.img2, self.rect)
        self.count += 1

    def hit(self, enemies):
        """攻击"""
        for enemy in enemies:
            distance = math.sqrt(
                math.pow((self.rect.left - enemy.rect.left), 2) + math.pow((self.rect.top - enemy.rect.top), 2))
            if distance < 50:
                enemy.health -= 1
            if enemy.health == 0:
                enemy.active = False
