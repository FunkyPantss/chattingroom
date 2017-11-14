from socket import *
from time import sleep
import threading
import rsa
import pymysql

HOST = '127.0.0.1'
PORT = 44444
BUFFERSIZE = 1024
ADDR = (HOST, PORT)

user_online = {}  # 存入客户端id,如果使用set，比起用list能加快200倍速度。但是因为要存储sock所以要用dict

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(100)

# 连接数据库
connect = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='123456',
    db='ChattingRoom',
    charset='utf8'
)
# 获取游标
CURSOR = connect.cursor()

def receive(my_id, tcpCliSock_i, privkey):
    print('receive接收消息')
    while True:
        try:
            crypto = tcpCliSock_i.recv(BUFFERSIZE)  # 接收到的是密文
            recv_data = rsa.decrypt(crypto, privkey)# byte类型,这一步可以不要，直接转发密文
            print(recv_data.decode('utf-8'))
            print(recv_data.decode('utf-8').split(':'))
            if not recv_data:
                print('消息为空')
                sleep(3)
                break

            friend_id = recv_data.decode('utf-8').strip().split(':')[0]
            recv_data = recv_data.decode('utf-8').strip().split(':')[1]
            print('id' + friend_id)
            print('recv_data' + recv_data)

            if int(friend_id) < 10000:  # 私聊
                print('条件为私聊')
                p2p(friend_id, recv_data)
            elif int(friend_id) >= 10000:
                broadcast(my_id, friend_id, recv_data)





            # if not crypto:  # recv_data
            #     print('消息为空')
            #     sleep(3)
            #     break
            # elif int(id) < 10000:  # 私聊#这里的id是str
            #     p2p(id, crypto)
            # elif int(id) >= 10000:
            #     broadcast(id, crypto)
        except Exception as e:
            print(e)
            print('客户端断开连接')


def broadcast(my_id, id, message):
    print('broadcast接受消息')
    # 通过群id在数据库中获得群成员，遍历发送消息,不在线也发
    sql = 'SELECT user_id FROM group_' + str(id)
    CURSOR.execute(sql)
    friend_tuple = CURSOR.fetchall()#((1,), (2,), (7,), (8,), (111,))  <class 'tuple'>
    print('tuple')
    print(friend_tuple)
    for i in friend_tuple:
        if str(i) != str(my_id):
            friend_id = str(i[0])#每个元组的0索引
            print('friend_id' + friend_id)
            #print('broadcast')
            #if is_online(friend_id):
            try:
                user_online[friend_id].send(message.encode('utf-8'))
            except Exception as e:
                print(e)
                print('服务器群发消息出错')


def p2p(id, message):
    # 目标机在线的情况
    print('p2p接收消息')
    if is_online(id):
        try:
            user_online[id].send(message.encode('utf-8'))
        except Exception as e:
            print(e)
            print('p2p出错')


def is_online(id):  # 给出一个ID判断其是否在线，如果在线返回True
    if id in user_online.keys():
        return True
    else:
        return False


if __name__ == '__main__':
    while True:
        print('聊天服务器正在等待客户端连接...')
        try:

            while True:
                tcpCliSock, addr = tcpSerSock.accept()
                print('客户端', addr[0], ':', str(addr[1]), '已连接\t')

                # 产生密钥对
                (pubkey, privkey) = rsa.newkeys(1024)
                pub = pubkey.save_pkcs1()#字节类型
                pri = privkey.save_pkcs1()
                #存储公钥
                with open('./pem/public' + str(addr[1]) + '.pem', 'w+') as pubfile:
                    pubfile.write(pub.decode('utf-8'))
                #存储私钥
                with open('./pem/private' + str(addr[1]) + '.pem', 'w+') as prifile:
                    prifile.write(pri.decode('utf-8'))

                # 将公钥发给客户端
                try:
                    tcpCliSock.sendall(pub)
                    print('公钥发送成功')
                except Exception as e:
                    print(e)

                # try:
                #     userid_passwd = tcpCliSock.recv(BUFFERSIZE).decode('utf-8')
                # except:
                #     print('接受账号密码错误')
                #
                # user_id, passwd = userid_passwd.split(':')


                #while True:
                try:
                    user_id = tcpCliSock.recv(BUFFERSIZE).decode('utf-8')  # 客户机的第一条消息是客户机名字
                    #print(userid_friendid)
                    #print(1)
                    # if not userid_friendid:
                    #     break
                except:
                    # print('客户端已断开连接')
                    # break
                    print('接受消息错误')
                    #break

                print('user_id:' + user_id)

                user_online[user_id] = tcpCliSock

                # print('user_name is [' + user_name +']')#连接前一条end=''的print语句

                threading.Thread(target=receive, args=(user_id, tcpCliSock, privkey)).start()
                # _thread.start_new_thread(receive, (friend_id, tcpCliSock))
        except Exception as e:
            print(e)
            pass
