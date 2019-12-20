"""运行函数"""
from pygame.locals import *
from MyGame.plane import *
from MyGame.bullet import *
from MyGame.enemy import *
from MyGame.boss import *
import pygame


def run():
    """主函数"""
    pygame.init()
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
    # 添加我方主机
    plane = Plane()
    # 游戏帧率设置
    clock = pygame.time.Clock()
    # 血量
    health_image = pygame.image.load(r'image/health.png').convert_alpha()
    # 分数图片
    score_image = []
    for i in range(10):
        path = 'image/' + str(i) + '.png'
        number_image = pygame.image.load(path)
        score_image.append(number_image)
    # 生成子弹
    bullet_list = []
    bullet_index = 0
    BULLET_NUM = 6
    for i in range(BULLET_NUM):
        bullet_list.append(Bullet(plane.rect.midtop))
    # 设置敌机生成延迟
    # 创建敌机
    enemies = pygame.sprite.Group()
    ENEMY_NUM = 10
    for i in range(ENEMY_NUM):
        enemies.add(Enemy(bg_size[0], bg_size[1]))
    # 创建boos敌机
    boss = Boss(bg_size[0], bg_size[1])
    enemies.add(boss)
    # 创建暂停按钮
    pause_image = pygame.image.load('image/pause.png').convert_alpha()
    pause_rect = pause_image.get_rect()
    # 播放b背景音乐
    if not bg_music.get_busy():
        bg_music.play(-1)
    # 延迟
    delay = 100
    # 设置位置
    score_position = 850
    # 设置暂停
    pause = False
    # 设置是否允许程序
    running = True
    while running:
        key_pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            # 判断是否发生暂停
            elif key_pressed[K_SPACE]:
                pause = not pause
        # 如果未暂停
        if not pause:
            # 检测用户键盘操作
            if key_pressed[K_w] or key_pressed[K_UP]:
                plane.moveUp()
            if key_pressed[K_s] or key_pressed[K_DOWN]:
                plane.moveDown()
            if key_pressed[K_a] or key_pressed[K_LEFT]:
                plane.moveLeft()
            if key_pressed[K_d] or key_pressed[K_RIGHT]:
                plane.moveRight()
            position = plane.rect.midtop
            position = (position[0] - 3, position[1])
            # 每过一定时间重置出界子弹
            if not (delay % 6):
                bullet_list[bullet_index].reset(position)
                bullet_index = (bullet_index + 1) % BULLET_NUM
                for each in enemies:
                    if not each.active:
                        each.reset()
                        each.active = True
            # 对于子弹列表，若存活，便绘制
            for each in bullet_list:
                if each.active:
                    collide_enemies = pygame.sprite.spritecollide(each, enemies, False, pygame.sprite.collide_mask)
                    if collide_enemies:
                        plane.score += 1
                        boom_music.play()
                        screen.blit(boom_image, each.rect)
                        each.active = False
                        for enemy in collide_enemies:
                            enemy.active = False
                    else:
                        each.move()
                        screen.blit(each.image, each.rect)
            # 若敌机存活，则移动
            for each in enemies:
                each.move()
            if delay:
                delay -= 1
            else:
                delay = 100
        # 绘制背景，血量，分数和暂停,飞机
        screen.blit(bg_image, (0, 0))
        screen.blit(health_image, (0, 0))
        screen.blit(pause_image, (870, 0))
        screen.blit(plane.image, plane.rect)
        # 绘制分数
        score = str(plane.score)
        score = score[::-1]
        for number in score:
            screen.blit(score_image[int(number)], (score_position, 0))
            score_position -= 20
        score_position = 850
        # 若敌机存在则绘制
        for each in enemies:
            if each.active:
                screen.blit(each.image, each.rect)
        # 对于子弹列表，若存活，便绘制
        for each in bullet_list:
            if each.active:
                screen.blit(each.image, each.rect)
        clock.tick(60)
        pygame.display.flip()
    pygame.quit()
