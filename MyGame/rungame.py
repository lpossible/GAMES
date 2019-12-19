"""运行函数"""
from pygame.locals import *
from MyGame.plane import *
from MyGame.bullet import *
from MyGame.enemy import *
from MyGame.boss import *
import pygame


def run():
    """主函数"""
    bg_size = 900, 515
    pygame.display.set_caption('My_game')
    screen = pygame.display.set_mode(bg_size)
    bg_image = pygame.image.load(r'image/background.png').convert_alpha()
    # 爆炸图片
    boom_image = pygame.image.load(r'image/boom.png').convert_alpha()
    # 调用背景音乐
    pygame.mixer.set_num_channels(5)
    bg_music = pygame.mixer.music
    bg_music.load(r'media/bg_music.mp3')
    bg_music.set_volume(10)
    # 设置
    # 射击声音
    shoot_music = pygame.mixer.Sound(r'media/shoot2.wav')
    shoot_music.set_volume(0.2)
    # 爆炸声音
    boom_music = pygame.mixer.Sound(r'media/boom.wav')
    boom_music.set_volume(0.2)
    plane = Plane()
    clock = pygame.time.Clock()
    # 生成子弹
    bullet_list = []
    bullet_index = 0
    bullet_num = 8
    for i in range(bullet_num):
        bullet_list.append(Bullet(plane.rect.midtop))
    # 创建敌机
    enemies = pygame.sprite.Group()
    enemies_num = 5
    for i in range(enemies_num):
        enemies.add(Enemy(bg_size[0], bg_size[1]))
    # 创建boos敌机
    enemies_death_num = 0
    boss = Boss(bg_size[0], bg_size[1])
    # 播放b背景音乐
    if not bg_music.get_busy():
        bg_music.play()
    # 延迟
    delay = 100
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        # 检测用户键盘操作
        key_pressed = pygame.key.get_pressed()
        if key_pressed[K_w] or key_pressed[K_UP]:
            plane.moveUp()
        if key_pressed[K_s] or key_pressed[K_DOWN]:
            plane.moveDown()
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            plane.moveLeft()
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            plane.moveRight()
        screen.blit(bg_image, (0, 0))
        screen.blit(plane.image, plane.rect)
        position = plane.rect.midtop
        position = (position[0] - 3, position[1])
        # 每过一定时间重置出界子弹和敌机
        if not (delay % 6):
            bullet_list[bullet_index].reset(position)
            bullet_index = (bullet_index + 1) % bullet_num
            for each in enemies:
                if not each.active:
                    each.reset()
                    each.active = True
                    enemies_death_num += 1
        if enemies_death_num > 20 and boss.active:
            screen.blit(boss.image, boss.rect)
            boss.move()
        # 对于子弹列表，若存活，便绘制
        for each in bullet_list:
            if each.active:
                collide_enemies = pygame.sprite.spritecollide(each, enemies, False, pygame.sprite.collide_mask)
                if collide_enemies:
                    boom_music.play()
                    screen.blit(boom_image, each.rect)
                    each.active = False
                    for enemy in collide_enemies:
                        enemy.active = False
                else:
                    each.move()
                    screen.blit(each.image, each.rect)
        # 若敌机存在则绘制
        for each in enemies:
            if each.active:
                screen.blit(each.image, each.rect)
                each.move()
        if enemies_death_num > 50:
            enemies_death_num = 0
            boss.active = True
            boss.reset()
        if delay:
            delay -= 1
        else:
            delay = 100
        clock.tick(30)
        pygame.display.flip()
    pygame.quit()
