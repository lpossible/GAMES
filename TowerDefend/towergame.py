"""主程序"""
from pygame.locals import *
from TowerDefend.enemy import *
import pygame

pygame.init()
size = width, height = 850, 425
screen = pygame.display.set_mode(size)
background_img = pygame.image.load(r'image/background.png').convert_alpha()
# 创建敌军类
enemy = Enemy()
# 加载暂停键
pause_img = pygame.image.load('image/pause.png').convert_alpha()
pause_rect = pause_img.get_rect()
pause_rect.left, pause_rect.top = 795, 0
# 加载血量和金币显示
health_money_img = pygame.image.load('image/health_money.png').convert_alpha()
health_money_rect = health_money_img.get_rect()
health_money_rect.left, health_money_rect.top = 0, 0
# 加载加速键
speed_img = pygame.image.load('image/speed.png').convert_alpha()
speed_rect = speed_img.get_rect()
speed_rect.left, speed_rect.top = 740, 0
# 设置循环条件
running = True
clock = pygame.time.Clock()
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    screen.blit(background_img, (0, 0))
    screen.blit(health_money_img, health_money_rect)
    screen.blit(pause_img, pause_rect)
    screen.blit(speed_img, speed_rect)
    if enemy.active:
        screen.blit(enemy.img, enemy.rect)
        enemy.move()
    pygame.display.flip()
pygame.quit()
