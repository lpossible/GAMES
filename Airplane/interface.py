"""界面"""
from tkinter import *

root = Tk()
root.title('飞机大战')
canvas = Canvas(root, width=359, height=640, cursor='circle', relief=GROOVE)
canvas.pack(side='left')
bg_img = PhotoImage(file=r'image/interface.png')
begin_button_img = PhotoImage(file='image/begin.png')
help_button_img = PhotoImage(file='image/help.png')
about_button_img = PhotoImage(file='image/about.png')
canvas.create_image(180, 320, image=bg_img)
# 开始按钮
canvas.create_window(185, 420, window=Button(root, image=begin_button_img, relief=RIDGE))
# 帮助按钮
canvas.create_window(185, 480, window=Button(root, image=help_button_img, relief=RIDGE))
# 关于按钮
canvas.create_window(185, 540, window=Button(root, image=about_button_img, relief=RIDGE))
mainloop()
