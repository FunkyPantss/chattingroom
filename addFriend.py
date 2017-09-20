import session

while True:
    friend_id = input("请输入好友账号：")

    # 查询数据
    sql = "SELECT user_id FROM Users WHERE user_id= " + friend_id
    print(sql)
    session.CURSOR.execute(sql)
    if friend_id == session.USER_ID:
        print("请不要输入自己的ID")
    elif session.CURSOR.rowcount:#查询到好友ID，进行添加好友操作session.USER_ID
        sql_add_relation = 'INSERT INTO ' + session.USER_ID + '_relation VALUES(%s,%s);'
        print(sql_add_relation % (session.USER_ID, friend_id))
        session.CURSOR.execute(sql_add_relation, (session.USER_ID, friend_id))
        print('sss')
        break
    else:#未查询到好友ID
        print("未查询到好友ID，请重新输入")
