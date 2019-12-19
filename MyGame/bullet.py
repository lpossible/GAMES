import pygame


class Bullet(pygame.sprite.Sprite):
    """Bullet"""

    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(r'image/bullet.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.speed = 20
        self.active = True
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        self.rect.bottom -= self.speed
        if self.rect.bottom < 0:
            self.active = False

    def reset(self, position):
        self.rect.left, self.rect.top = position
        self.active = True
