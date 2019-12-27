"""初始化炮塔可占据的位置"""
import pygame


class Position(pygame.sprite.Sprite):
    """pos"""

    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('image/pt.png')
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = pos
