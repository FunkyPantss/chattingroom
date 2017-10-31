#-*- coding=utf-8 -*-
import os
import hashlib
import struct
import GUI.chat_window

BUFFER_SIZE = 1024
HEAD_STRUCT = '128sIq32s'


def cal_md5(file_path):
    with open(file_path, 'rb') as fr:
        md5 = hashlib.md5()
        md5.update(fr.read())
        md5 = md5.hexdigest()
        return md5


def get_file_info(file_path):
    file_name = os.path.basename(file_path)
    file_name_len = len(file_name)
    file_size = os.path.getsize(file_path)
    md5 = cal_md5(file_path)
    return file_name, file_name_len, file_size, md5


def send_file_to_server(file_path, tcpCliSock):
    file_name, file_name_len, file_size, md5 = get_file_info(file_path)
    file_head = struct.pack(HEAD_STRUCT, file_name.encode('utf-8'), file_name_len, file_size, md5.encode('utf-8'))

    try:
        print("Start connect")
        tcpCliSock.send(file_head)
        sent_size = 0

        with open(file_path, 'rb') as fr:
            while sent_size < file_size:
                remained_size = file_size - sent_size
                send_size = BUFFER_SIZE if remained_size > BUFFER_SIZE else remained_size
                send_file = fr.read(send_size)
                sent_size += send_size
                tcpCliSock.send(send_file)
        #文件传输结束

    except Exception as e:
        print("Socket error: %s" % str(e))
    finally:
        print("Closing connect")

def send_file(file_path, tcpCliSock):#首先调用这个函数
    if not file_path:
        print('未选择文件')
    send_file_to_server(file_path, tcpCliSock)
