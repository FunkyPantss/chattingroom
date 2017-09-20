import session


def login(user_id, passwd):
    while True:
        # session.USER_ID = input("请输入用户账号：")
        # session.USER_NAME = input("请输入密码：")


        #全局设置user_id
        session.USER_ID = user_id


        # 查询数据
        sql = "SELECT user_id,passwd FROM Users WHERE user_id= " + session.USER_ID + ' AND passwd=' + passwd
        print(sql)
        session.CURSOR.execute(sql)
        # for row in cursor.fetchall():
        #     print("Name:%s\tSaving:%.2f" % row)
        # print('共查找出', cursor.rowcount, '条数据')
        if session.CURSOR.rowcount:
            print('登录成功')
            return True
            break
        else:
            print("登录失败，请重新登录")
            return False


