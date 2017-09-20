from socket import *
from time import *
import threading
import sys

#HOST = '169.254.105.136'
HOST = '127.0.0.1'
PORT = 44444
BUFFERSIZE = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)



def to_server():
    while True:
        #input_str = input('输入聊天内容...')
        #input_data = bytes(input_str, 'utf-8')#必须将输入值转换为bytes才可以直接用流输出
        #sys.stdout.write("[" + username + "] ")
        #sys.stdout.flush()
        input_data = sys.stdin.readline()#broad为B:,p2p为P:username:message
        #print('input_data is ' +input_data)#str
        try:
            if not input_data:
                break
            else:
                #message_to_send = "[" + username + "]" #加上[username]
                #print(message_to_send)
            #tcpCliSock.send(b'%s [%s] %s' % (bytes(name, 'utf-8'), bytes(ctime(), 'utf-8'), input_data))
                #tcpCliSock.sendall(message_to_send.encode('utf-8') + input_data.encode('utf-8'))
                FLAG = False
                try:
                    if input_data[0:2] == 'B:':
                        print('[me]' + input_data.split('B:')[1],end='')
                        FLAG = True
                    elif input_data[0:2] == 'P:':
                        print('[me]' + input_data.split(':')[2], end='')
                        FLAG = True
                except:
                    print('输入消息格式错误！')

                if FLAG:
                    tcpCliSock.sendall(input_data.encode('utf-8'))
                else:
                    print('输入消息格式错误！')

                #break
  #username.encode('utf-8')
        except error:
            #print('to_server()' + error)
            print('消息发送失败')

def recv_server():
    while True:
        try:
            recv_data = tcpCliSock.recv(BUFFERSIZE).decode('utf-8')
            if not recv_data:
                break
            else:
                #print(recv_data.decode('utf-8'))
                sys.stdout.write(recv_data)
                sys.stdout.flush()
                #print('\n')
        except error:
            print('服务器连接已断开')
            sleep(3)
            break


if __name__ == '__main__':
    # 将第一条消息作为客户端的用户名称
    client_name = input('请输入用户名：')
    tcpCliSock.send(b'%s' % client_name.encode('utf-8'))

    # 启动接受消息线程
    thread_recvServer = threading.Thread(target=recv_server, args=())
    thread_recvServer.start()
    #thread_recvServer.join()


    #启动发送消息线程
    thread_toServer = threading.Thread(target=to_server, args=())
    thread_toServer.start()
    #thread_toServer.join()



    #tcpCliSock.close()