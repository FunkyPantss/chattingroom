from socket import *
from time import *
import threading
import sys
import session

HOST = '127.0.0.1'
PORT = 44444
BUFFERSIZE = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)



# def start_thread_send(user_id, message, mode):
#     thread_recvServer = threading.Thread(target=send, args=(user_id, message, mode))
#     thread_recvServer.start()


def send(message, mode):
    if mode == 'friend':
        try:
            tcpCliSock.send(message.encode('utf-8'))
        except:
            print('发送消息时出错')


if __name__ == '__main__':
    try:
        tcpCliSock.send(session.FRIEND_NAME.encode('utf-8'))
    except:
        print('发送用户名时出错')
