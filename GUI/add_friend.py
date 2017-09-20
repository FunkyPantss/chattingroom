import pymysql
import session
from tkinter import *
from GUI import friend_list


class add_function():
    def click_button_group(self):  # 控制颜色
        self.button_group.config(bg='blue')
        self.button_friend.config(bg='white')

        self.button_findfriend.grid_forget()
        self.button_findgroup.grid(row=1, column=1)

    def click_button_friend(self):  # 控制颜色
        self.button_friend.config(bg='blue')
        self.button_group.config(bg='white')

        self.button_findgroup.grid_forget()
        self.button_findfriend.grid(row=1, column=1)

    def find_friend(self):
        def makefriend():
            sql = 'INSERT INTO ' + str(int(session.USER_ID)) + "_friend VALUES(%d, '%s', 1);"
            try:
                print(type(self.info[0]))
                print(type(self.info[1]))
                print(str(self.info[1]))
                print(sql % (self.info[0], str(self.info[1])))
                session.CURSOR.execute(sql % (self.info[0], str(self.info[1])))
                session.connect.commit()
                # 在好友列表中添加最新的好友

                friend_list.top.name_id[self.info[1]] = self.info[0]
                friend_list.top.listbox_friend.insert(END, self.info[1])

                self.label_3.config(text='成功添加好友!')
            except pymysql.err.IntegrityError:
                self.label_3.config(text='该用户已经是你的好友了!')
            except EXCEPTION as e:
                self.label_3.config(text='添加好友时出错，请联系管理员')
                print(e)

        number = self.entry.get()
        sql = 'SELECT user_id,user_name FROM users WHERE user_id =' + number + ';'
        session.CURSOR.execute(sql)
        if session.CURSOR.rowcount:
            self.info = session.CURSOR.fetchone()
            self.label_info.config(text='成功!')

            self.label.config(text='用户名：' + self.info[1])
            self.label.grid(row=1)

            self.label_2.config(text='用户账号：' + str(self.info[0]))
            self.label_2.grid(row=2)

            self.button = Button(self.label_info_bottom, command=makefriend)
            self.button.config(text='添加好友')
            self.button.grid(row=3)
        else:
            self.label_info.config(text='失败!')

    def find_group(self):
        number = self.entry.get()
        # sql = 'SELECT user_id FROM users WHERE groups =' + number + ';'
        sql = 'SELECT * FROM users'
        session.CURSOR.execute(sql)

        if session.CURSOR.rowcount:
            self.label_info.config(text='成功!')
        else:
            print('失败')
            self.label_info.config(text='失败!')

    def __init__(self):
        self.root = Tk()
        self.root.title('查找')
        self.root.geometry('400x200+500+300')

        # 上方——找群、找人
        self.label = Label(self.root)
        self.label.pack(side=TOP, fill=BOTH, ipady=10)

        # 添加两个按钮
        self.button_friend = Button(self.label, text='找人', command=self.click_button_friend)
        self.button_friend.pack(side=LEFT, fill=BOTH, expand=1)

        self.button_group = Button(self.label, text='找群', command=self.click_button_group)
        self.button_group.pack(side=RIGHT, fill=BOTH, expand=1)

        # 下方——输入框
        self.label_bottom = Label(self.root)
        self.label_bottom.pack(side=TOP, fill=BOTH, expand=1)

        # 输入框
        self.entry = Entry(self.label_bottom)
        self.entry.grid(row=1, column=0)

        # 两个按钮，一个查找群一个查找好友
        self.button_findfriend = Button(self.label_bottom, text='查找', command=self.find_friend)
        self.button_findfriend.grid(row=1, column=1)

        self.button_findgroup = Button(self.label_bottom, text='查找', command=self.find_group)
        # 第二个按钮先不显示
        # self.button_findfirend.grid(row=1, column=1)

        # 输出查找成功或失败
        self.label_info = Label(self.label_bottom)
        self.label_info.grid(row=1, column=2, sticky='w')

        # 输入好友信息或群信息label
        self.label_info_bottom = Label(self.label_bottom)
        self.label_info_bottom.grid(row=2)

        # 最下方——查找成功后输入好友或群信息
        self.label = Label(self.label_info_bottom)
        self.label_2 = Label(self.label_info_bottom)
        self.label_3 = Label(self.label_info_bottom)  # 这行默认不显示,应该config添加成功或打印错误信息

        self.root.mainloop()
