#文件服务器只做转发，不做验证

from socket import *
import hashlib
import struct
import threading

HOST = '127.0.0.1'
PORT = 44445
BUFFERSIZE = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(100)

user_online = {}#存入客户端id,如果使用set，比起用list能加快200倍速度。但是因为要存储sock所以要用dict

HEAD_STRUCT = '128sIq32s'
info_size = struct.calcsize(HEAD_STRUCT)


def cal_md5(file_path):
    with open(file_path, 'rb') as fr:
        md5 = hashlib.md5()
        md5.update(fr.read())
        md5 = md5.hexdigest()
        return md5


def unpack_file_info(file_info):
    file_name, file_name_len, file_size, md5 = struct.unpack(HEAD_STRUCT, file_info)
    file_name = file_name[:file_name_len]
    return file_name, file_size, md5


def recv_file(id, tcpCliSock_i):
    try:
        #这里是文件头，需要先将文件头转发到目标端
        file_info_package = tcpCliSock.recv(info_size)
        tcpCliSock_i.send(file_info_package)
        #解包
        file_name, file_size, md5_recv = unpack_file_info(file_info_package)

        recved_size = 0
        with open('./server_file/' + file_name, 'wb') as fw:
            while recved_size < file_size:
                remained_size = file_size - recved_size
                recv_size = BUFFERSIZE if remained_size > BUFFERSIZE else remained_size
                recv_file = tcpCliSock_i.recv(recv_size)
                recved_size += recv_size
                fw.write(recv_file)
                #添加转发的部分
                p2p(id, recv_file)
        md5 = cal_md5(file_name)
        if md5 != md5_recv.decode('utf-8'):
            print(type(md5))
            print(type(md5_recv.decode('utf-8')))
            print('md5：' + md5)
            print('recv：' + md5_recv.decode('utf-8'))
            print('MD5 compared fail!')
        else:
            print('Received successfully')
    except Exception as e:
        print("Socket error: %s" % str(e))


def p2p(id, recv_stream):
    # 目标机在线的情况
    if is_online(id):
        try:
            user_online[id].send(recv_stream)
        except Exception as e:
            print(e)
            print('p2p出错')
    else:
        print('目标机不在线')
        return False

def is_online(id):#给出一个ID判断其是否在线，如果在线返回True
    if id in user_online.keys():
        return True
    else:
        return False


if __name__ == '__main__':
    print('文件服务器正在等待客户端连接...')
    while True:
        tcpCliSock, addr = tcpSerSock.accept()
        print('客户端', addr[0], ':', str(addr[1]), '已连接\t')


        try:
            userid_friendid = tcpCliSock.recv(BUFFERSIZE).decode('utf-8')  # 客户机的第一条消息是客户机名字
        except:
            # print('客户端已断开连接')
            # break
            print('接受消息错误')
        user_id, friend_id = userid_friendid.split(':')
        print('user_id:' + user_id)
        print('friend_id:' + friend_id)

        user_online[user_id] = tcpCliSock

        # print('user_name is [' + user_name +']')#连接前一条end=''的print语句

        threading.Thread(target=recv_file, args=(friend_id, tcpCliSock)).start()
        # _thread.start_new_thread(receive, (friend_id, tcpCliSock))