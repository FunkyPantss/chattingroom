from tkinter import *
import session

from GUI import chat_window
from GUI import add_friend
from GUI import group_chat_window


import pymysql


class top():
    # @staticmethod
    def chatwindow(self, event):
        # self.chat = Tk()
        # self.chat.geometry('600x300+450+250')
        # self.chat.title('这里显示好友名称')
        # self.chat.mainloop()

        # chat = Toplevel()
        pass

    def selected_friend(self, event):  # event即使不需要也要写上
        # print('选择了' + str(self.listbox_friend.get(self.listbox_friend.curselection())))
        session.FRIEND_NAME = str(self.listbox_friend.get(self.listbox_friend.curselection()))
        session.FRIEND_ID = str(self.name_id[session.FRIEND_NAME])
        # print('现在friendname是' + session.FRIEND_NAME)
        # print('现在friendID是' + session.FRIEND_NAME)
        # self.chat = Tk()
        # self.chat.geometry('700x500+450+250')
        # self.chat.title(self.listbox_friend.get(self.listbox_friend.curselection()))
        # self.chat.mainloop()

        # 在这里启动发送消息和接受消息的线程

        try:
            session.file_tcpCliSock.send((session.USER_ID + ':' + session.FRIEND_ID).encode('utf-8'))
        except EXCEPTION as e:
            print(e)
            print('seng_file error')

        chat_window.chat()  # 打开聊天窗口

    def selected_group(self, event):
        session.GROUP_NAME = str(self.listbox_group.get(self.listbox_group.curselection()))
        session.GROUP_ID = str(self.group_id[session.GROUP_NAME])
        # session.chat_tcpCliSock.send(str(session.GROUP_ID) + ':' + )

        group_chat_window.chat()

    def showfriend(self):
        # 取消群列表显示
        self.listbox_group.pack_forget()
        self.scroll_group.pack_forget()

        # 显示好友列表
        self.refresh_friend()

        self.scroll.pack(side=RIGHT, fill=BOTH)
        self.listbox_friend.pack(fill=BOTH, expand=1)

    def showgroup(self):
        # 取消好友列表的显示，未改变里面的内容
        self.listbox_friend.pack_forget()
        self.scroll.pack_forget()

        # 显示群列表
        self.scroll_group.pack(side=RIGHT, fill=BOTH)
        self.listbox_group.pack(fill=BOTH, expand=1)

    def refresh_friend(self):
        sql = 'SELECT friend_id,friend_name FROM ' + session.USER_ID + '_friend WHERE state=1'
        try:
            session.CURSOR.execute(sql)
            self.infos = session.CURSOR.fetchall()
            print(self.infos)

            self.listbox_friend.delete(0, END)
            self.name_id = {}

            for info in self.infos:
                self.name_id[info[1]] = info[0]
                self.listbox_friend.insert(END, info[1])
            print(self.name_id)
        # except EXCEPTION as e:
        #     print(e)
        #     print('从数据库中取好友列表时出错')
        except:
            pass

    def refresh_group(self):
        sql = 'SELECT group_id,group_name FROM ' + session.USER_ID + '_group'
        try:
            session.CURSOR.execute(sql)
            self.infos_group = session.CURSOR.fetchall()
            for info in self.infos_group:
                self.group_id[info[1]] = info[0]
                self.listbox_group.insert(END, info[1])
        except Exception as e:
            print(e)
            print('从数据库中取群列表时出错')

    def add(self):
        add_friend.add_function()
        print('已退出add_function')
        self.refresh_friend()
        print('添加成功')

    def right_mouse(self, event):
        def dislike(friend_id):
            sql = 'UPDATE ' + str(session.USER_ID) + '_friend SET state=0 WHERE friend_id=' + str(friend_id)
            print(sql)
            session.CURSOR.execute(sql)
            self.refresh_friend()

        def delete(friend_id):
            sql = 'DELETE FROM ' + str(session.USER_ID) + '_friend WHERE friend_id=' + str(friend_id)
            print(sql)
            session.CURSOR.execute(sql)
            self.refresh_friend()

        session.FRIEND_NAME = str(self.listbox_friend.get(self.listbox_friend.curselection()))
        session.FRIEND_ID = str(self.name_id[session.FRIEND_NAME])

        print(session.FRIEND_NAME)
        self.menubar.delete(0, END)
        self.menubar.add_command(label='加入黑名单', command=lambda: dislike(session.FRIEND_ID))
        self.menubar.add_command(label='删除好友', command=lambda: delete(session.FRIEND_ID))
        self.menubar.post(event.x_root, event.y_root)

    def __init__(self):
        try:

            self.root = Tk()
            self.root.geometry('291x701+900+50')
            self.root.title('好友列表')

            # 最上方——个人信息
            self.label_info = Label(self.root, text='个人信息', relief=SUNKEN, anchor=W, bd=1)  # W是West对齐，即左对齐;bd是border
            self.label_info.pack(side=TOP, fill=X, ipady=30)

            # 第二部分——好友、群选择
            self.frame_choice = Frame(self.root, bg='red')
            self.frame_choice.pack(side=TOP, fill=X, ipady=15)
            # 在这个frame中添加两个按钮
            self.button_friend = Button(self.frame_choice, text='好友', command=self.showfriend)
            self.button_friend.pack(side=LEFT, fill=BOTH, expand=1)

            self.button_group = Button(self.frame_choice, text='群', command=self.showgroup)
            self.button_group.pack(side=RIGHT, fill=BOTH, expand=1)

            # 中部——Frame
            self.frame = Frame(self.root)
            self.frame.pack(side=TOP, fill=BOTH, expand=1)

            # 中部——好友列表
            self.scroll = Scrollbar(self.frame, orient=VERTICAL)
            self.listbox_friend = Listbox(self.frame)  # W是West对齐，即左对齐;bd是border
            # self.variable_a.trace('w', self.updateoptions)
            self.listbox_friend.config(selectmode=BROWSE, yscrollcommand=self.scroll.set, bd=1, font=20, height=20,
                                       width=20)
            self.scroll.config(command=self.listbox_friend.yview)
            self.scroll.pack(side=RIGHT, fill=BOTH)
            self.listbox_friend.pack(fill=BOTH, expand=1)

            # 示例
            # for item in range(1, 50):
            #     self.listbox_friend.insert(END, item)

            # 从数据库中取出好友列表，以字典[名称]:ID的方式存储，并将名称显示出来
            self.name_id = {}
            self.refresh_friend()

            self.listbox_friend.bind('<Double-Button-1>', self.selected_friend)  # 给listbox_friend绑定事件
            try:
                self.menubar = Menu(self.listbox_friend, tearoff=FALSE)
                self.listbox_friend.bind('<Button-3>', self.right_mouse)  # 右击
            except:
                pass

            # 中部——群列表


            self.scroll_group = Scrollbar(self.frame, orient=VERTICAL)
            self.listbox_group = Listbox(self.frame)  # W是West对齐，即左对齐;bd是border
            self.listbox_group.config(selectmode=BROWSE, yscrollcommand=self.scroll.set, bd=1, font=20, height=20,
                                      width=20)
            self.scroll_group.config(command=self.listbox_group.yview)

            self.group_id = {}
            self.refresh_group()

            self.listbox_group.bind('<Double-Button-1>', self.selected_group)  # 给listbox_group绑定事件

            # 默认先显示好友列表，这两行到showgroup中调用
            # self.scroll_group.pack(side=RIGHT, fill=BOTH)
            # self.listbox_group.pack(fill=BOTH, expand=1)
            # for item in range(50, 100):
            #     self.listbox_group.insert(END, item)

            #
            # 最下方——添加好友
            self.label_add = Button(self.root, relief=SUNKEN, anchor=W, bd=1)  # W是West对齐，即左对齐;bd是border
            self.label_add.pack(side=BOTTOM, fill=X, ipady=10)

            self.button_add = Button(self.label_add, text='查找', command=self.add)
            self.button_add.grid(sticky='w')

            self.root.mainloop()
        except:
            pass
