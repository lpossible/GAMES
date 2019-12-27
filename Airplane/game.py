"""主文件"""
from tkinter import *
from Airplane.rungame import *
import pygame


def main():
    """main函数"""
    pygame.init()
    bg_music = pygame.mixer.music
    bg_music.load(r'media/interface.mp3')
    bg_music.set_volume(20)
    root = Tk()
    root.title('飞机大战')
    root.resizable(0, 0)
    canvas = Canvas(root, width=359, height=640, cursor='circle', relief=GROOVE)
    canvas.pack(side='left')
    # 加载相关图片
    bg_img = PhotoImage(file=r'image/interface.png')
    begin_button_img = PhotoImage(file='image/begin.png')
    help_button_img = PhotoImage(file='image/help.png')
    about_button_img = PhotoImage(file='image/about.png')
    canvas.create_image(180, 320, image=bg_img)
    # 开始按钮
    canvas.create_window(180, 422, window=Button(root, image=begin_button_img, relief=RIDGE, command=run))
    # 帮助按钮
    canvas.create_window(180, 482, window=Button(root, image=help_button_img, relief=RIDGE))
    # 关于按钮
    canvas.create_window(180, 542, window=Button(root, image=about_button_img, relief=RIDGE))
    if not bg_music.get_busy():
        bg_music.play()
    mainloop()


if __name__ == '__main__':
    main()
