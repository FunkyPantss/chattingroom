import login_code
from tkinter import *
from GUI import friend_list
import tkinter.messagebox
import session
import pymysql
import time
from GUI import connect_to_server

class login():
    def denglu(self):
        user_id = self.entry_id.get()
        passwd = self.entry_passwd.get()
        while user_id != '' and passwd != '':
            user_id = self.entry_id.get()
            passwd = self.entry_passwd.get()
            if login_code.login(user_id, passwd):#登录成功,进入下一个界面
                self.root.destroy()
                #在登录成功后就先连接聊天服务器和文件服务器
                connect_to_server.connect()
                friend_list.top()

            else:#登录失败
                tkinter.messagebox.showerror('登录失败', '账号或密码错误，请重新输入')
                pass


    def register(self):
        #首先取消下方登录按钮的显示，把注册按钮显示到第1列
        self.button_login.grid_forget()
        self.button_register.grid(row=4, column=1)
        #再插入一行用于输入用户名
        self.label_username.grid(row=2, column=0)
        self.entry_username.grid(row=2, column=1)

        user_id = self.entry_id.get()
        user_name = self.entry_username.get()
        passwd = self.entry_passwd.get()

        while user_id != '' and user_name != '' and passwd != '':
            user_id = self.entry_id.get()
            user_name = self.entry_username.get()
            passwd = self.entry_passwd.get()



            sql = "INSERT INTO Users (user_id, user_name, passwd) VALUES ( '%d', '%s', %s )"
            data = (int(user_id), user_name, passwd)
            print(data)
            try:
                session.CURSOR.execute(sql % data)
                session.connect.commit()
                print('注册成功，已插入', session.CURSOR.rowcount, '条数据')


            except pymysql.err.IntegrityError:  # 出现相同主键,重新输入
                self.entry_id.delete(0, END)
                self.entry_username.delete(0, END)
                self.entry_passwd.delete(0, END)
                print("该账号已被注册，请选择其他账号")
                break


            except:
                print('register()出现其他错误')
                break

            try:
                # 每新建一个账号，同时新建一个好友表和一个群表
                sql_create_friend_relation_table = 'CREATE TABLE ' + user_id + '_friend(' \
                                                                               'friend_id INT(10) NOT NULL PRIMARY KEY,' \
                                                                               'friend_name VARCHAR(45) NOT NULL,' \
                                                                               'state INT(1) NOT NULL DEFAULT 1);'

                sql_create_group_relation_table = 'CREATE TABLE ' + user_id + '_group(' \
                                                                              'user_id INT(10) PRIMARY KEY,' \
                                                                              'group_id INT(10) NOT NULL,' \
                                                                              'group_name VARCHAR(45) NOT NULL);'
                print(sql_create_friend_relation_table)
                print(sql_create_group_relation_table)

                session.CURSOR.execute(sql_create_friend_relation_table)
                session.CURSOR.execute(sql_create_group_relation_table)
                print(sql_create_friend_relation_table)
                tkinter.messagebox.showinfo('', '注册成功！')
                self.denglu()
                break
            except Exception as e:
                print(e)
                print('创建表时出错')
                break




    def __init__(self):
        self.root = Tk()
        self.root.geometry('422x278+450+250')
        self.root.title('QQ')


        #上方——图片
        self.frame = Frame(self.root, bg='blue')
        self.frame.pack(side=TOP, fill=BOTH, expand=1)


        #下方——功能
        self.frame_function = Frame(self.root, bg='red', height=30)
        self.frame_function.pack(side=BOTTOM, fill=BOTH, expand=1)

        #账号
        self.label_id = Label(self.frame_function, text='账号:')
        self.label_id.grid(row=1,column=0)
        self.entry_id = Entry(self.frame_function)
        self.entry_id.focus_set()
        self.entry_id.grid(row=1,column=1)


        #用户名(先定义，在这里不显示,应显示在第二行）
        self.label_username = Label(self.frame_function, text='用户名：')
        self.entry_username = Entry(self.frame_function)

        #密码
        self.label_passwd = Label(self.frame_function, text='密码:')
        self.label_passwd.grid(row=3, column=0)
        self.entry_passwd = Entry(self.frame_function)
        self.entry_passwd.grid(row=3, column=1)
        #注册
        self.button_register = Button(self.frame_function, text='注册', command=self.register)
        self.button_register.grid(row=4, column=0)
        #空行
        #登录
        self.button_login = Button(self.frame_function, text='登录', command=self.denglu)
        self.button_login.grid(row=4, column=1, sticky='e')



        self.root.mainloop()
