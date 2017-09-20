from socket import *


HOST = '127.0.0.1'
CHAT_PORT = 44444
BUFFERSIZE = 1024
CHAT_ADDR = (HOST, CHAT_PORT)

FILE_PORT = 44445
FILE_ADDR = (HOST, FILE_PORT)

CHAT_CONNECTED = False
FILE_CONNECTED = False

while CHAT_CONNECTED is False:
    try:
        chat_tcpCliSock = socket(AF_INET, SOCK_STREAM)
        chat_tcpCliSock.connect(CHAT_ADDR)
        CONNECTED = True
        print('成功连接到聊天服务器')
    except:
        print('连接聊天服务器时出错')

while FILE_CONNECTED is False:
    try:
        file_tcpCliSock = socket(AF_INET, SOCK_STREAM)
        file_tcpCliSock.connect(FILE_ADDR)
        CONNECTED = True
        print('成功连接到文件服务器')
    except:
        print('连接文件服务器时出错')

