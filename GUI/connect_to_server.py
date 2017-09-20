from socket import *
import session


HOST = '127.0.0.1'
CHAT_PORT = 44444
BUFFERSIZE = 1024
CHAT_ADDR = (HOST, CHAT_PORT)

FILE_PORT = 44445
FILE_ADDR = (HOST, FILE_PORT)

CHAT_CONNECTED = False
FILE_CONNECTED = False

def connect():
    while True:
        try:
            session.chat_tcpCliSock = socket(AF_INET, SOCK_STREAM)
            session.chat_tcpCliSock.connect(CHAT_ADDR)
            print('成功连接到聊天服务器')
            break
        except Exception as e:
            print(e)
            print('连接聊天服务器时出错')

    while True:
        try:
            session.file_tcpCliSock = socket(AF_INET, SOCK_STREAM)
            session.file_tcpCliSock.connect(FILE_ADDR)
            print('成功连接到文件服务器')
            break
        except:
            print('连接文件服务器时出错')

