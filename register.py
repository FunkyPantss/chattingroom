import session
import pymysql

# 插入数据
while True:
    # user = input("请输入用户账号：")
    # user_name = input("请输入用户名：")
    # password = int(input("请输入密码："))

    sql = "INSERT INTO Users (user_id, user_name, passwd) VALUES ( '%s', '%s', %d )"
    data = (user, user_name, password)
    try:
        session.CURSOR.execute(sql % data)
        session.connect.commit()
        print('注册成功，已插入', session.CURSOR.rowcount, '条数据')
        #每新建一个账号，同时新建一个好友表和一个群表
        sql_create_friend_relation_table = 'CREATE TABLE ' + user + '_friend(' \
                                                             'user_id CHAR(15) PRIMARY KEY,' \
                                                             'friend_id CHAR(15) NOT NULL);'
        sql_create_group_relation_table = 'CREATE TABLE ' + user + '_group(' \
                                                             'user_id CHAR(15) PRIMARY KEY,' \
                                                             'group_id CHAR(15) NOT NULL);'
        session.CURSOR.execute(sql_create_friend_relation_table)
        print(sql_create_friend_relation_table)
        break
    except pymysql.err.IntegrityError:#出现相同主键
        print("该账号已被注册，请选择其他账号")
        continue

