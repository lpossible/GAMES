import pygame


class Plane(pygame.sprite.Sprite):
    """Plane"""

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(r'image/plane.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = 397, 432
        self.speed = 10
        self.mask = pygame.mask.from_surface(self.image)

    def moveUp(self):
        if self.rect.top > 0:
            self.rect.top -= self.speed
        else:
            self.rect.top = 0

    def moveDown(self):
        if self.rect.bottom < 515:
            self.rect.top += self.speed
        else:
            self.rect.bottom = 515

    def moveLeft(self):
        if self.rect.left > 0:
            self.rect.left -= self.speed
        else:
            self.rect.left = 0

    def moveRight(self):
        if self.rect.right < 900:
            self.rect.right += self.speed
        else:
            self.rect.right = 900
