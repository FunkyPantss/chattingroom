from socket import *
from time import sleep
import threading
import _thread
import rsa

HOST = '127.0.0.1'
PORT = 44444
BUFFERSIZE = 1024
ADDR = (HOST, PORT)

user_online = {}  # 存入客户端id,如果使用set，比起用list能加快200倍速度。但是因为要存储sock所以要用dict

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(100)


def receive(id, tcpCliSock_i):
    while True:
        try:
            recv_data = tcpCliSock_i.recv(BUFFERSIZE)  # 不再encode，只在print时encode
            print(recv_data.decode('utf-8'))
            if not recv_data:
                print('消息为空')
                sleep(3)
                break
            elif int(id) < 10000:  # 私聊#这里的id是str
                p2p(id, recv_data)
            elif int(id) >= 10000:
                broadcast(id, recv_data)
        except Exception as e:
            print(e)
            print('客户端断开连接')


def broadcast(id, message):
    # 通过群id获得群成员，遍历发送消息
    pass


def p2p(id, message):
    # 目标机在线的情况
    if is_online(id):
        try:
            user_online[id].send(message)
        except Exception as e:
            print(e)
            print('p2p出错')


def is_online(id):  # 给出一个ID判断其是否在线，如果在线返回True
    if id in user_online.keys():
        return True
    else:
        return False


if __name__ == '__main__':
    print('聊天服务器正在等待客户端连接...')
    while True:
        tcpCliSock, addr = tcpSerSock.accept()
        print('客户端', addr[0], ':', str(addr[1]), '已连接\t')

        # 产生密钥对
        (pubkey, privkey) = rsa.newkeys(1024)
        pub = pubkey.save_pkcs1()
        print(type(pub))
        with open('./pem/public' + str(addr[1]) + '.pem', 'w+') as pubfile:
            pubfile.write(pub.decode('utf-8'))
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


        while True:
            try:
                userid_friendid = tcpCliSock.recv(BUFFERSIZE).decode('utf-8')  # 客户机的第一条消息是客户机名字
                print(userid_friendid)
                if not userid_friendid:
                    break
            except:
                # print('客户端已断开连接')
                # break
                print('接受消息错误')
                break
        print(userid_friendid)
        user_id, friend_id = userid_friendid.split(':')
        print('user_id:' + user_id)
        print('friend_id:' + friend_id)

        user_online[user_id] = tcpCliSock

        # print('user_name is [' + user_name +']')#连接前一条end=''的print语句

        threading.Thread(target=receive, args=(friend_id, tcpCliSock)).start()
        # _thread.start_new_thread(receive, (friend_id, tcpCliSock))
