"""主程序"""
from pygame.locals import *
from TowerDefend.enemy import *
from TowerDefend.towerposSet import *
from TowerDefend.tower import *
import pygame


def run():
    pygame.init()
    size = width, height = 1200, 600
    screen = pygame.display.set_mode(size)
    background_img = pygame.image.load(r'image/background.png').convert_alpha()
    background_img = pygame.transform.scale(background_img, (width, height))
    # 创建背景音乐
    bg_music = pygame.mixer.music
    bg_music.load('media/bg.mp3')
    bg_music.set_volume(2)
    # 创建敌军类
    enemies = pygame.sprite.Group()
    ENEMY_NUM = 5
    position = [[258, 600], [258, 670], [258, 740], [258, 810], [258, 880]]
    for i in range(ENEMY_NUM):
        enemies.add(Enemy(position[i]))
    # 创建炮塔
    towers = pygame.sprite.Group()
    # 加载暂停键
    pause_img = pygame.image.load('image/pause.png').convert_alpha()
    pause_rect = pause_img.get_rect()
    pause_rect.left, pause_rect.top = 1145, 0
    # 加载血量和金币显示
    health_money_img = pygame.image.load('image/health_money.png').convert_alpha()
    health_money_rect = health_money_img.get_rect()
    health_money_rect.left, health_money_rect.top = 0, 0
    # 加载加速键
    speed_img = pygame.image.load('image/speed.png').convert_alpha()
    speed_rect = speed_img.get_rect()
    speed_rect.left, speed_rect.top = 1090, 0
    # 设置炮塔位置
    towers_pos = pygame.sprite.Group()
    position_list = [[225, 495], [264, 428], [312, 428], [362, 428], [410, 428], [460, 428], [508, 428], [561, 428],
                     [561, 373], [377, 373]]
    for i in range(len(position_list)):
        towers_pos.add(Position(position_list[i]))
    # 设置循环条件
    running = True
    clock = pygame.time.Clock()
    paused = False
    # 播放音乐
    if not bg_music.get_busy():
        bg_music.play(-1)
    while running:
        clock.tick(100)
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if speed_rect.collidepoint(event.pos):
                        for each in enemies:
                            each.accelerate *= 2
                    if pause_rect.collidepoint(event.pos):
                        paused = not paused
                    for each in towers_pos:
                        if each.rect.collidepoint(event.pos):
                            tower = Tower([each.rect.left, each.rect.top])
                            towers.add(tower)
                            towers_pos.remove(each)
        if not paused:
            for enemy in enemies:
                if enemy.active:
                    enemy.move()
        # 绘制界面设置
        screen.blit(background_img, (0, 0))
        screen.blit(health_money_img, health_money_rect)
        screen.blit(pause_img, pause_rect)
        screen.blit(speed_img, speed_rect)
        # 绘制炮塔
        for each in towers:
            each.draw(screen)
            each.hit(enemies)
        # 绘制炮塔位置
        towers_pos.draw(screen)
        # 敌军若存活则绘制其和血量
        for enemy in enemies:
            if enemy.active:
                screen.blit(enemy.img, enemy.rect)
                enemy.drawhealth(screen)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    run()
