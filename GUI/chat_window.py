from tkinter import *
import tkinter.filedialog
import threading
import session
from socket import *
import time
import file_client


class chat():
    def send(self):
        message = self.textpad.get(1.0, END)
        print(message)
        try:
            self.tcpCliSock.send(message.encode('utf-8'))
        except:
            print('发送消息失败')

    def receive(self):
        while True:
            try:
                message = self.tcpCliSock.recv(1024)
                if not message:
                    break
                else:  # 接收到了消息，在这里进行处理，显示
                    print(message.decode('utf-8'))
                    self.show_message.config(state=NORMAL)
                    self.show_message.insert(self.mark, '[' + time.ctime() + ']' + message.decode('utf-8') + '\n')
                    self.show_message.config(state=DISABLED)

            except Exception as e:

                print(e)
                print('与服务器的连接已断开')
                time.sleep(3)
                break


    def file(self):#传送文件，调用file_client的内容
        filename = tkinter.filedialog.askopenfilename()#defaultextension='.txt'
        file_client.send_file(filename.name, self.tcpCliSock)

    def __init__(self):
        HOST = '127.0.0.1'
        PORT = 44444
        BUFFERSIZE = 1024
        ADDR = (HOST, PORT)

        try:
            self.tcpCliSock = socket(AF_INET, SOCK_STREAM)
            self.tcpCliSock.connect(ADDR)
        except:
            print('连接服务器出错')

        # 向服务器发送第一条消息，使用格式userid:friendid
        userid_friendid = session.USER_ID + ':' + session.FRIEND_ID
        try:
            self.tcpCliSock.send(userid_friendid.encode('utf-8'))
        except Exception as e:
            print(e)
            print('发送好友名称出错')

        # 创建接受消息线程
        self.thread_receive = threading.Thread(target=self.receive, args=(), name=session.FRIEND_NAME)
        self.thread_receive.start()

        self.root = Tk()
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

        # 添加表情、文件、发送按钮
        self.button_emoji = Button(self.lable_function, text='表情', bd=1, bg='red')
        # self.button_emoji.grid(row=0, column=1)
        self.button_emoji.pack(side=LEFT, fill=Y)

        self.button_file = Button(self.lable_function, text='文件', bd=1, bg='white', command=file)
        # self.button_file.grid(row=0, column=2)
        self.button_file.pack(side=LEFT, fill=Y)

        self.button_send = Button(self.lable_function, text='发送', bd=1, bg='blue', command=self.send)
        # self.button_send.grid(row=0, column=3, sticky='E')
        self.button_send.pack(side=RIGHT, fill=Y)

        # #发送标签,有时间再调整吧，妈个鸡
        # self.lable_send = Label(self.frame_buttom, bg='black', bd=1)
        # self.lable_send.pack(side=BOTTOM, fill=BOTH, ipady=5)



        self.root.mainloop()
