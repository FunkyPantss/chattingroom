from socket import *
import hashlib
import struct
import session

HOST = '127.0.0.1'
PORT = 44445
BUFFERSIZE = 1024
ADDR = (HOST, PORT)

# tcpSerSock = socket(AF_INET, SOCK_STREAM)
# tcpSerSock.bind(ADDR)
# tcpSerSock.listen(100)

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


#使用全局变量session.file_tcpCliSock接受文件
def recv():
    print('文件服务器正在等待客户端连接...')
    try:
        # 解包
        file_info_package = session.file_tcpCliSock.recv(info_size)
        file_name, file_size, md5_recv = unpack_file_info(file_info_package)

        recved_size = 0
        with open(file_name, 'wb') as fw:
            while recved_size < file_size:
                remained_size = file_size - recved_size
                recv_size = BUFFERSIZE if remained_size > BUFFERSIZE else remained_size
                recv_file = session.file_tcpCliSock.recv(recv_size)
                recved_size += recv_size
                fw.write(recv_file)
        md5 = cal_md5(file_name)
        if md5 != md5_recv.decode:
            print('md5' + md5)
            print('reve' + md5_recv.decode('utf-8'))
            print('MD5 compared fail!')
        else:
            print('Received successfully')
            return file_name

    except Exception as e:
        print("Socket error: %s" % str(e))
        return False

