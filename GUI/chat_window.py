import threading
import time
import tkinter.filedialog
from tkinter import *
import tkinter.messagebox
from PIL import Image, ImageTk
import cilent_recv_file
import file_client
import session


class chat():
    def send(self):
        message = self.textpad.get(1.0, END)
        print(message)
        try:
            session.chat_tcpCliSock.send(message.encode('utf-8'))
        except:
            tkinter.messagebox.showerror('错误', '发送消息失败')

    def receive_message(self):
        while True:
            try:
                message = session.chat_tcpCliSock.recv(1024)
                if not message:
                    break

                elif message.decode('utf-8').split('/')[0] == 'emoji:..':#接收到图片
                    file = message.decode('utf-8').split(':')[-1]#文件路径
                    print(file)
                    try:
                        self.show_message.config(state=NORMAL)
                        self.show_message.insert(self.mark, '[' + time.strftime('%H:%M:%S', time.localtime()) + ']  ', 'time_color')
                        _emoji = ImageTk.PhotoImage(Image.open(file))
                        self.show_message.image_create(self.mark, image=_emoji)
                        self.show_message.insert(self.mark, '\n\n', 'time_color')
                        self.show_message.config(state=DISABLED)
                    except Exception as e:
                        print(e)
                        print('显示表情出错')


                else:  # 接收到了消息，在这里进行处理，显示
                    print(message.decode('utf-8'))
                    self.show_message.config(state=NORMAL)
                    self.textpad.tag_config(self.time_color, background='green')
                    self.show_message.insert(self.mark, '[' + time.strftime('%H:%M:%S', time.localtime()) + ']  ', 'time_color')
                    self.show_message.insert(self.mark, message.decode('utf-8') + '\n\n')
                    self.show_message.config(state=DISABLED)

            except:
                print('与服务器的连接已断开')
                time.sleep(3)
                break


    def send_file(self):
        filename = tkinter.filedialog.askopenfile()  # defaultextension='.txt'
        file_client.send_file(filename.name, session.file_tcpCliSock)


    def receive_file(self):
        cilent_recv_file.recv()

    def emoji(self):
        #取得当前光标位置，插入图片
        #这条语句可以实现插入图片，但是不能得到current
        #button = Button(top, image=photo1, command=lambda :print(self.textpad.image_create('mark', image=photo1)))

        top = Toplevel()

        def send_emoji(photo):
            #构造发送语句
            text = 'emoji:' + photo
            try:
                session.chat_tcpCliSock.send(text.encode('utf-8'))
            except:
                print('表情发送失败')

        photo1 = ImageTk.PhotoImage(Image.open(self.rootdir + 'a1.png'))
        button = Button(top, image=photo1, command=lambda: send_emoji(self.rootdir + 'a1.png'))
        print(self.textpad.mark_names())
        button.image = photo1
        button.grid(row=0, column=1)

        photo = ImageTk.PhotoImage(Image.open(self.rootdir + 'a2.png'))
        button = Button(top, image=photo, command=lambda: 'a2')
        button.image = photo
        button.grid(row=0, column=2)

        photo = ImageTk.PhotoImage(Image.open(self.rootdir + 'a3.png'))
        button = Button(top, image=photo, command=lambda: print('a3'))
        button.image = photo
        button.grid(row=0, column=3)

        photo = ImageTk.PhotoImage(Image.open(self.rootdir + 'a4.png'))
        button = Button(top, image=photo, command=lambda: print('a4'))
        button.image = photo
        button.grid(row=0, column=4)

        photo = ImageTk.PhotoImage(Image.open(self.rootdir + 'a5.png'))
        button = Button(top, image=photo, command=lambda: print('a5'))
        button.image = photo
        button.grid(row=0, column=5)

        photo = ImageTk.PhotoImage(Image.open(self.rootdir + 'a6.png'))
        button = Button(top, image=photo, command=lambda: print('a6'))
        button.image = photo
        button.grid(row=0, column=6)

        photo = ImageTk.PhotoImage(Image.open(self.rootdir + 'a7.png'))
        button = Button(top, image=photo, command=lambda: print('a7'))
        button.image = photo
        button.grid(row=0, column=7)

        photo = ImageTk.PhotoImage(Image.open(self.rootdir + 'a8.png'))
        button = Button(top, image=photo, command=lambda: print('a8'))
        button.image = photo
        button.grid(row=0, column=8)

        photo = ImageTk.PhotoImage(Image.open(self.rootdir + 'a9.png'))
        button = Button(top, image=photo, command=lambda: print('a9'))
        button.image = photo
        button.grid(row=0, column=9)

        photo = ImageTk.PhotoImage(Image.open(self.rootdir + 'a10.png'))
        button = Button(top, image=photo, command=lambda: print('a10'))
        button.image = photo
        button.grid(row=0, column=10)

        photo = ImageTk.PhotoImage(Image.open(self.rootdir + 'a11.png'))
        button = Button(top, image=photo, command=lambda: print('a11'))
        button.image = photo
        button.grid(row=0, column=11)

        photo = ImageTk.PhotoImage(Image.open(self.rootdir + 'a12.png'))
        button = Button(top, image=photo, command=lambda: print('a12'))
        button.image = photo
        button.grid(row=0, column=12)

        photo = ImageTk.PhotoImage(Image.open(self.rootdir + 'b1.png'))
        button = Button(top, image=photo, command=lambda: print('b1'))
        button.image = photo
        button.grid(row=1, column=1)

        photo = ImageTk.PhotoImage(Image.open(self.rootdir + 'b2.png'))
        button = Button(top, image=photo, command=lambda: print('b2'))
        button.image = photo
        button.grid(row=1, column=2)

        photo = ImageTk.PhotoImage(Image.open(self.rootdir + 'b3.png'))
        button = Button(top, image=photo, command=lambda: print('b3'))
        button.image = photo
        button.grid(row=1, column=3)

        photo = ImageTk.PhotoImage(Image.open(self.rootdir + 'b4.png'))
        button = Button(top, image=photo, command=lambda: print('b4'))
        button.image = photo
        button.grid(row=1, column=4)

        photo = ImageTk.PhotoImage(Image.open(self.rootdir + 'b5.png'))
        button = Button(top, image=photo, command=lambda: print('b5'))
        button.image = photo
        button.grid(row=1, column=5)

        photo = ImageTk.PhotoImage(Image.open(self.rootdir + 'b6.png'))
        button = Button(top, image=photo, command=lambda: print('b6'))
        button.image = photo
        button.grid(row=1, column=6)

        photo = ImageTk.PhotoImage(Image.open(self.rootdir + 'b7.png'))
        button = Button(top, image=photo, command=lambda: print('b7'))
        button.image = photo
        button.grid(row=1, column=7)

        photo = ImageTk.PhotoImage(Image.open(self.rootdir + 'b8.png'))
        button = Button(top, image=photo, command=lambda: print('b8'))
        button.image = photo
        button.grid(row=1, column=8)

        photo = ImageTk.PhotoImage(Image.open(self.rootdir + 'b9.png'))
        button = Button(top, image=photo, command=lambda: print('b9'))
        button.image = photo
        button.grid(row=1, column=9)

        photo = ImageTk.PhotoImage(Image.open(self.rootdir + 'b10.png'))
        button = Button(top, image=photo, command=lambda: print('b10'))
        button.image = photo
        button.grid(row=1, column=10)

        photo = ImageTk.PhotoImage(Image.open(self.rootdir + 'b11.png'))
        button = Button(top, image=photo, command=lambda: print('b11'))
        button.image = photo
        button.grid(row=1, column=11)

        photo = ImageTk.PhotoImage(Image.open(self.rootdir + 'b12.png'))
        button = Button(top, image=photo, command=lambda: print('b12'))
        button.image = photo
        button.grid(row=1, column=12)

        photo = ImageTk.PhotoImage(Image.open(self.rootdir + 'c1.png'))
        button = Button(top, image=photo, command=lambda: print('c1'))
        button.image = photo
        button.grid(row=2, column=1)

        photo = ImageTk.PhotoImage(Image.open(self.rootdir + 'c2.png'))
        button = Button(top, image=photo, command=lambda: print('c1'))
        button.image = photo
        button.grid(row=2, column=2)

        photo = ImageTk.PhotoImage(Image.open(self.rootdir + 'c3.png'))
        button = Button(top, image=photo, command=lambda: print('c1'))
        button.image = photo
        button.grid(row=2, column=3)

        photo = ImageTk.PhotoImage(Image.open(self.rootdir + 'c4.png'))
        button = Button(top, image=photo, command=lambda: print('c1'))
        button.image = photo
        button.grid(row=2, column=4)

        photo = ImageTk.PhotoImage(Image.open(self.rootdir + 'c5.png'))
        button = Button(top, image=photo, command=lambda: print('c1'))
        button.image = photo
        button.grid(row=2, column=5)

        photo = ImageTk.PhotoImage(Image.open(self.rootdir + 'c6.png'))
        button = Button(top, image=photo, command=lambda: print('c1'))
        button.image = photo
        button.grid(row=2, column=6)

        photo = ImageTk.PhotoImage(Image.open(self.rootdir + 'c7.png'))
        button = Button(top, image=photo, command=lambda: print('c1'))
        button.image = photo
        button.grid(row=2, column=7)

        photo = ImageTk.PhotoImage(Image.open(self.rootdir + 'c8.png'))
        button = Button(top, image=photo, command=lambda: print('c1'))
        button.image = photo
        button.grid(row=2, column=8)

        photo = ImageTk.PhotoImage(Image.open(self.rootdir + 'c9.png'))
        button = Button(top, image=photo, command=lambda: print('c1'))
        button.image = photo
        button.grid(row=2, column=9)

        photo = ImageTk.PhotoImage(Image.open(self.rootdir + 'c10.png'))
        button = Button(top, image=photo, command=lambda: print('c1'))
        button.image = photo
        button.grid(row=2, column=10)

        photo = ImageTk.PhotoImage(Image.open(self.rootdir + 'c11.png'))
        button = Button(top, image=photo, command=lambda: print('c1'))
        button.image = photo
        button.grid(row=2, column=11)

        photo = ImageTk.PhotoImage(Image.open(self.rootdir + 'c12.png'))
        button = Button(top, image=photo, command=lambda: print('c1'))
        button.image = photo
        button.grid(row=2, column=12)

        top.mainloop()


    def __init__(self):
        #self.rootdir ='e:/python/chatroomforgit/emoji_file/'
        self.rootdir = '../emoji_file/'
        self.time_color = 'time_color'

        # 向服务器发送第一条消息，使用格式userid:friendid
        userid_friendid = session.USER_ID + ':' + session.FRIEND_ID
        try:
            session.chat_tcpCliSock.send(userid_friendid.encode('utf-8'))
            session.file_tcpCliSock.send(userid_friendid.encode('utf-8'))
        except Exception as e:
            print(e)
            print('发送好友名称出错')

        # 创建接受消息线程
        self.thread_receive = threading.Thread(target=self.receive_message, args=(), name=session.FRIEND_NAME)
        self.thread_receive.start()

        self.root = Toplevel()
        self.root.geometry('600x450+450+250')
        self.root.title(session.FRIEND_NAME)

        # 上方——好友信息
        self.label_info = Label(self.root, text='个人信息', relief=SUNKEN, anchor=W, bd=1)  # W是West对齐，即左对齐;bd是border
        self.label_info.pack(side=TOP, fill=X, ipady=20)

        # 中部——聊天信息框
        self.frame = Frame(self.root, bg='green')
        self.frame.pack(side=TOP, fill=X, ipady=50)

        self.show_message = Text(self.frame, bd=1, height=10)
        # self.show_message.config(state=DISABLED)#这行在添加之后在写
        self.show_message.pack(fill=BOTH, expand=1)
        self.mark = 'mark'
        self.show_message.mark_set(self.mark, CURRENT + ' lineend')

        # 下部——输入框部分
        self.frame_buttom = Frame(self.root, bg='black')
        self.frame_buttom.pack(side=BOTTOM, fill=BOTH, ipady=30)

        # 表情——文件栏
        self.lable_function = Label(self.frame_buttom, bd=1, bg='yellow')
        self.lable_function.pack(side=TOP, ipady=5, fill=BOTH)

        # 输入框
        self.textpad = Text(self.frame_buttom, bd=1)
        self.textpad.pack(side=TOP, fill=X, ipady=25)
        self.textpad.focus_set()

        #mark,tag
        self.textpad.mark_set('mark', CURRENT)

        # 添加表情、文件、发送按钮
        self.button_emoji = Button(self.lable_function, text='表情', bd=1, bg='red', command=self.emoji)
        # self.button_emoji.grid(row=0, column=1)
        self.button_emoji.pack(side=LEFT, fill=Y)

        self.button_file = Button(self.lable_function, text='文件', bd=1, bg='white', command=self.send_file)
        # self.button_file.grid(row=0, column=2)
        self.button_file.pack(side=LEFT, fill=Y)

        self.button_send = Button(self.lable_function, text='发送', bd=1, bg='blue', command=self.send)
        # self.button_send.grid(row=0, column=3, sticky='E')
        self.button_send.pack(side=RIGHT, fill=Y)

        # #发送标签,有时间再调整吧，妈个鸡
        # self.lable_send = Label(self.frame_buttom, bg='black', bd=1)
        # self.lable_send.pack(side=BOTTOM, fill=BOTH, ipady=5)



        self.root.mainloop()
