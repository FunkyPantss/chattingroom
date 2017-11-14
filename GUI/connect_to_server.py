from socket import *
import session
from time import sleep
import rsa


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
            #session.chat_tcpCliSock.send('11111'.encode('utf-8'))
            print('成功连接到聊天服务器')
            #协商密钥,从服务器接受的第一条消息是公钥
            #while True:
            pub = session.chat_tcpCliSock.recv(1024)
            session.pubkey = rsa.PublicKey.load_pkcs1(pub)


            print(session.pubkey)
                #print(session.pubkey.decode('utf-8'))
                # if not session.pubkey:
                #     break#
            print(1)
            break
        except Exception as e:
            print(e)
            print('连接聊天服务器时出错')
            sleep(3)


    while True:
        try:
            session.file_tcpCliSock = socket(AF_INET, SOCK_STREAM)
            session.file_tcpCliSock.connect(FILE_ADDR)
            print('成功连接到文件服务器')
            break
        except:
            print('连接文件服务器时出错')
            sleep(3)


