"""小兵类"""
import pygame


class Enemy(pygame.sprite.Sprite):
    """小兵类"""

    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.image.load(r'image/enemy.png').convert_alpha()
        self.rect = self.img.get_rect()
        self.init_pos = position
        self.rect.left, self.rect.top = self.init_pos
        self.accelerate = 1
        self.speed = [0, -self.accelerate]
        self.active = True
        self.health = 500
        # 竖直
        self.status = 'UP'

    def move(self):
        """移动"""
        self.rect = self.rect.move(self.speed)
        if self.rect.top <= 448 and self.rect.left == 258:
            self.rect.top = 448
            self.status = 'R'
            self.img = pygame.transform.rotate(self.img, 270)
            self.speed = [self.accelerate, 0]
        if self.rect.top == 448 and self.rect.left >= 597:
            self.rect.left = 597
            self.status = 'UP'
            self.img = pygame.transform.rotate(self.img, 90)
            self.speed = [0, -self.accelerate]
        if 320 < self.rect.top <= 335 and self.rect.left == 597:
            self.rect.top = 335
            self.status = 'L'
            self.img = pygame.transform.rotate(self.img, 90)
            self.speed = [-self.accelerate, 0]
        if self.rect.top == 335 and self.rect.left <= 370:
            self.rect.left = 370
            self.status = 'UP'
            self.img = pygame.transform.rotate(self.img, 270)
            self.speed = [0, -self.accelerate]
        if self.rect.top <= 216 and self.rect.left == 370:
            self.rect.top = 216
            self.status = 'R'
            self.img = pygame.transform.rotate(self.img, 270)
            self.speed = [self.accelerate, 0]
        if self.rect.top == 216 and 800 > self.rect.left >= 746:
            self.rect.left = 746
            self.status = 'DW'
            self.img = pygame.transform.rotate(self.img, 270)
            self.speed = [0, self.accelerate]
        if self.rect.top >= 330 and self.rect.left == 746:
            self.rect.top = 330
            self.status = 'R'
            self.img = pygame.transform.rotate(self.img, 90)
            self.speed = [self.accelerate, 0]
        if self.rect.top == 330 and self.rect.left >= 930:
            self.rect.left = 930
            self.status = 'UP'
            self.img = pygame.transform.rotate(self.img, 90)
            self.speed = [0, -self.accelerate]
        if self.rect.top < 180:
            self.reset()

    def drawhealth(self, screen):
        """绘制血量"""
        BLACK = (0, 0, 0)
        RED = (255, 0, 0)
        GREEN = (0, 255, 0)
        health_percentage = float(self.health) / 500
        if self.status == 'UP':
            start = self.rect.left + 8
            pygame.draw.line(screen, BLACK, (start, self.rect.top - 3),
                             (start + 32, self.rect.top - 3), 4)
            if health_percentage > 0.5:
                pygame.draw.line(screen, GREEN, (start, self.rect.top - 3),
                                 (start + 32 * health_percentage, self.rect.top - 3), 4)
            else:
                pygame.draw.line(screen, RED, (start, self.rect.top - 3),
                                 (start + 32 * health_percentage, self.rect.top - 3), 4)
        elif self.status == 'DW':
            start = self.rect.left + 8
            pygame.draw.line(screen, BLACK, (start, self.rect.bottom + 3),
                             (start + 32, self.rect.bottom + 3), 4)
            if health_percentage > 0.5:
                pygame.draw.line(screen, GREEN, (start, self.rect.bottom + 3),
                                 (start + 32 * health_percentage, self.rect.bottom + 3), 4)
            else:
                pygame.draw.line(screen, RED, (start, self.rect.bottom + 3),
                                 (start + 32 * health_percentage, self.rect.bottom + 3), 4)
        elif self.status == 'R':
            start = self.rect.bottom - 8
            pygame.draw.line(screen, BLACK, (self.rect.right + 3, start),
                             (self.rect.right + 3, start - 32), 4)
            if health_percentage > 0.5:
                pygame.draw.line(screen, GREEN, (self.rect.right + 3, start),
                                 (self.rect.right + 3, start - 32 * health_percentage), 4)
            else:
                pygame.draw.line(screen, RED, (self.rect.right + 3, start),
                                 (self.rect.right + 3, start - 32 * health_percentage), 4)
        else:
            start = self.rect.bottom - 8
            pygame.draw.line(screen, BLACK, (self.rect.left - 3, start),
                             (self.rect.left - 3, start - 30), 4)
            if health_percentage > 0.5:
                pygame.draw.line(screen, GREEN, (self.rect.left - 3, start),
                                 (self.rect.left - 3, start - 30 * health_percentage), 4)
            else:
                pygame.draw.line(screen, RED, (self.rect.left - 3, start),
                                 (self.rect.left - 3, start - 30 * health_percentage), 4)

    def reset(self):
        """reset the position"""
        self.rect.left, self.rect.top = self.init_pos
