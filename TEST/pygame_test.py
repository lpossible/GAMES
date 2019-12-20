import pygame
import sys

# 初始化pygame
pygame.init()
# 设置名字
pygame.display.set_caption('New Game')
# 设置屏幕的大小
size = width, height = 640, 480
# 设置背景颜色
bg = (255, 255, 255)
# 添加屏幕大小,并返回屏幕的surface对象
screen = pygame.display.set_mode(size)

# 设置图标,若不支持则需要在设置屏幕之前设置图标
# pygame.display.set_icon()


# pygame鼠标方法
# pygame.mouse.set_cursor(pygame.cursors.arrow)

# 创建新的声音对象
# music = pygame.mixer.Sound(r'C:\Users\asus\Desktop\music\Sammi Sanchez - TALK.mp3')
# # 创建一个用于控制播放的通道对象
# music_line = pygame.mixer.Channel(music)
# 特殊的流媒体通道
flow_music = pygame.mixer.music
# 音乐路径
flow_music.load('Sammi Sanchez - TALK.mp3')
flow_music.set_volume(20)
while True:
    screen.fill(bg)
    # 如果通道不忙,播放音乐
    if not flow_music.get_busy():
        flow_music.play()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flow_music.stop()
            sys.exit()

    pygame.display.update()  # 此更新方法与flip()
    # # 更新界面
    # pygame.display.flip()
    # 设置延迟
    pygame.time.delay(10)
    # 设置帧率大小
    # pygame.time.Clock().tick(0)
