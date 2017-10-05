from tkinter import *
from PIL import Image, ImageTk
import session

#测试通过，但是没什么用...
# topdir = 'e:/python/chatroomforgit/emoji_file/'
#
# class emoji_file():
#     def get_name(self, name):
#         print(self)
#
#
#
#     def __init__(self):
#         #首先需要获取当前鼠标的位置，以此作为原点显示窗口
#         self.top = Tk()
#         self.top.geometry('400x300')
#         dic = {}
#         num = 1
#         sum = 0
#
#         #获取文件夹中表情总数
#         for parent, dirnames, filenames in os.walk(topdir):
#             for filename in filenames:
#                 sum += 1
#
#         for i in range(sum - 1):
#             dic['button%d' % i] = str(i)
#
#
#         for i, j in dic.items():
#             file = 'a_' + str(num) + '.png'
#             image = Image.open(file)
#             photo = ImageTk.PhotoImage(image)
#             setattr(self, i, Button(self.top, command=lambda: print(j)))
#             exec('self.' + i + '.config(image=photo)')
#             exec('self.' + i + '.image=photo')
#             exec('self.' + i + '.grid(row=0, column=num)')
#
#             num += 1
#
#         self.top.mainloop()
#
# emoji_file()



def emoji_toplevel():
    top = Toplevel()

    def button1(x):
        return x
    photo = ImageTk.PhotoImage(Image.open('e:/python/chatroomforgit/emoji_file/a1.png'))
    button = Button(top, image=photo, command=lambda : button1(photo))
    button.image = photo
    button.grid(row=0, column=1)


    photo = ImageTk.PhotoImage(Image.open('e:/python/chatroomforgit/emoji_file/a2.png'))
    button = Button(top, image=photo, command=lambda :'a2')
    button.image = photo
    button.grid(row=0, column=2)


    photo = ImageTk.PhotoImage(Image.open('e:/python/chatroomforgit/emoji_file/a3.png'))
    button = Button(top, image=photo, command=lambda :print('a3'))
    button.image = photo
    button.grid(row=0, column=3)


    photo = ImageTk.PhotoImage(Image.open('e:/python/chatroomforgit/emoji_file/a4.png'))
    button = Button(top, image=photo, command=lambda :print('a4'))
    button.image = photo
    button.grid(row=0, column=4)


    photo = ImageTk.PhotoImage(Image.open('e:/python/chatroomforgit/emoji_file/a5.png'))
    button = Button(top, image=photo, command=lambda :print('a5'))
    button.image = photo
    button.grid(row=0, column=5)

    photo = ImageTk.PhotoImage(Image.open('e:/python/chatroomforgit/emoji_file/a6.png'))
    button = Button(top, image=photo, command=lambda :print('a6'))
    button.image = photo
    button.grid(row=0, column=6)

    photo = ImageTk.PhotoImage(Image.open('e:/python/chatroomforgit/emoji_file/a7.png'))
    button = Button(top, image=photo, command=lambda :print('a7'))
    button.image = photo
    button.grid(row=0, column=7)

    photo = ImageTk.PhotoImage(Image.open('e:/python/chatroomforgit/emoji_file/a8.png'))
    button = Button(top, image=photo, command=lambda :print('a8'))
    button.image = photo
    button.grid(row=0, column=8)

    photo = ImageTk.PhotoImage(Image.open('e:/python/chatroomforgit/emoji_file/a9.png'))
    button = Button(top, image=photo, command=lambda :print('a9'))
    button.image = photo
    button.grid(row=0, column=9)

    photo = ImageTk.PhotoImage(Image.open('e:/python/chatroomforgit/emoji_file/a10.png'))
    button = Button(top, image=photo, command=lambda :print('a10'))
    button.image = photo
    button.grid(row=0, column=10)

    photo = ImageTk.PhotoImage(Image.open('e:/python/chatroomforgit/emoji_file/a11.png'))
    button = Button(top, image=photo, command=lambda :print('a11'))
    button.image = photo
    button.grid(row=0, column=11)

    photo = ImageTk.PhotoImage(Image.open('e:/python/chatroomforgit/emoji_file/a12.png'))
    button = Button(top, image=photo, command=lambda :print('a12'))
    button.image = photo
    button.grid(row=0, column=12)

    photo = ImageTk.PhotoImage(Image.open('e:/python/chatroomforgit/emoji_file/b1.png'))
    button = Button(top, image=photo, command=lambda :print('b1'))
    button.image = photo
    button.grid(row=1, column=1)

    photo = ImageTk.PhotoImage(Image.open('e:/python/chatroomforgit/emoji_file/b2.png'))
    button = Button(top, image=photo, command=lambda :print('b2'))
    button.image = photo
    button.grid(row=1, column=2)

    photo = ImageTk.PhotoImage(Image.open('e:/python/chatroomforgit/emoji_file/b3.png'))
    button = Button(top, image=photo, command=lambda :print('b3'))
    button.image = photo
    button.grid(row=1, column=3)

    photo = ImageTk.PhotoImage(Image.open('e:/python/chatroomforgit/emoji_file/b4.png'))
    button = Button(top, image=photo, command=lambda :print('b4'))
    button.image = photo
    button.grid(row=1, column=4)

    photo = ImageTk.PhotoImage(Image.open('e:/python/chatroomforgit/emoji_file/b5.png'))
    button = Button(top, image=photo, command=lambda :print('b5'))
    button.image = photo
    button.grid(row=1, column=5)

    photo = ImageTk.PhotoImage(Image.open('e:/python/chatroomforgit/emoji_file/b6.png'))
    button = Button(top, image=photo, command=lambda :print('b6'))
    button.image = photo
    button.grid(row=1, column=6)

    photo = ImageTk.PhotoImage(Image.open('e:/python/chatroomforgit/emoji_file/b7.png'))
    button = Button(top, image=photo, command=lambda :print('b7'))
    button.image = photo
    button.grid(row=1, column=7)

    photo = ImageTk.PhotoImage(Image.open('e:/python/chatroomforgit/emoji_file/b8.png'))
    button = Button(top, image=photo, command=lambda :print('b8'))
    button.image = photo
    button.grid(row=1, column=8)

    photo = ImageTk.PhotoImage(Image.open('e:/python/chatroomforgit/emoji_file/b9.png'))
    button = Button(top, image=photo, command=lambda :print('b9'))
    button.image = photo
    button.grid(row=1, column=9)

    photo = ImageTk.PhotoImage(Image.open('e:/python/chatroomforgit/emoji_file/b10.png'))
    button = Button(top, image=photo, command=lambda :print('b10'))
    button.image = photo
    button.grid(row=1, column=10)

    photo = ImageTk.PhotoImage(Image.open('e:/python/chatroomforgit/emoji_file/b11.png'))
    button = Button(top, image=photo, command=lambda :print('b11'))
    button.image = photo
    button.grid(row=1, column=11)

    photo = ImageTk.PhotoImage(Image.open('e:/python/chatroomforgit/emoji_file/b12.png'))
    button = Button(top, image=photo, command=lambda :print('b12'))
    button.image = photo
    button.grid(row=1, column=12)

    photo = ImageTk.PhotoImage(Image.open('e:/python/chatroomforgit/emoji_file/c1.png'))
    button = Button(top, image=photo, command=lambda :print('c1'))
    button.image = photo
    button.grid(row=2, column=1)

    photo = ImageTk.PhotoImage(Image.open('e:/python/chatroomforgit/emoji_file/c2.png'))
    button = Button(top, image=photo, command=lambda :print('c1'))
    button.image = photo
    button.grid(row=2, column=2)

    photo = ImageTk.PhotoImage(Image.open('e:/python/chatroomforgit/emoji_file/c3.png'))
    button = Button(top, image=photo, command=lambda :print('c1'))
    button.image = photo
    button.grid(row=2, column=3)

    photo = ImageTk.PhotoImage(Image.open('e:/python/chatroomforgit/emoji_file/c4.png'))
    button = Button(top, image=photo, command=lambda :print('c1'))
    button.image = photo
    button.grid(row=2, column=4)

    photo = ImageTk.PhotoImage(Image.open('e:/python/chatroomforgit/emoji_file/c5.png'))
    button = Button(top, image=photo, command=lambda :print('c1'))
    button.image = photo
    button.grid(row=2, column=5)

    photo = ImageTk.PhotoImage(Image.open('e:/python/chatroomforgit/emoji_file/c6.png'))
    button = Button(top, image=photo, command=lambda :print('c1'))
    button.image = photo
    button.grid(row=2, column=6)

    photo = ImageTk.PhotoImage(Image.open('e:/python/chatroomforgit/emoji_file/c7.png'))
    button = Button(top, image=photo, command=lambda :print('c1'))
    button.image = photo
    button.grid(row=2, column=7)

    photo = ImageTk.PhotoImage(Image.open('e:/python/chatroomforgit/emoji_file/c8.png'))
    button = Button(top, image=photo, command=lambda :print('c1'))
    button.image = photo
    button.grid(row=2, column=8)

    photo = ImageTk.PhotoImage(Image.open('e:/python/chatroomforgit/emoji_file/c9.png'))
    button = Button(top, image=photo, command=lambda :print('c1'))
    button.image = photo
    button.grid(row=2, column=9)

    photo = ImageTk.PhotoImage(Image.open('e:/python/chatroomforgit/emoji_file/c10.png'))
    button = Button(top, image=photo, command=lambda :print('c1'))
    button.image = photo
    button.grid(row=2, column=10)

    photo = ImageTk.PhotoImage(Image.open('e:/python/chatroomforgit/emoji_file/c11.png'))
    button = Button(top, image=photo, command=lambda :print('c1'))
    button.image = photo
    button.grid(row=2, column=11)

    photo = ImageTk.PhotoImage(Image.open('e:/python/chatroomforgit/emoji_file/c12.png'))
    button = Button(top, image=photo, command=lambda :print('c1'))
    button.image = photo
    button.grid(row=2, column=12)

    top.mainloop()