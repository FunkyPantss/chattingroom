from socket import *
from time import sleep
import _thread


#HOST = '169.254.105.136'
HOST = '127.0.0.1'
PORT = 44444
BUFFERSIZE = 1024
ADDR = (HOST, PORT)

user_list = {}

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(10)


#负责接收客户机消息，执行判断条件在调用broadcast
def receiver(user_name, tcpCliSock_i):

    #print('开始接收客户机消息')  # for test
    while True:
        try:
            recv_data = tcpCliSock_i.recv(BUFFERSIZE).decode('utf-8')#在这里先编码成str
            if not recv_data:
                print('消息为空')
                sleep(3)
                break

            elif recv_data[0:2] == 'B:':#广播
                B_recv_data = recv_data.split('B:')[1]
                print('[%s]:' % user_name, B_recv_data)
                message_to_send = '[' + user_name + ']' + B_recv_data
                #message_to_send = B_recv_data
                broadcast(user_name, message_to_send.encode('utf-8'))
                #tcpCliSock_i.close()
                #return
                #break
            elif recv_data[0:2] == 'P:':#p2p
                to_send_usr = recv_data.split(':')[1]
                P_recv_data = recv_data.split(':')[2]
                print('[%s]:' % user_name, P_recv_data)
                message_to_send = '[' + user_name + ']' + P_recv_data
                # message_to_send = B_recv_data
                p2p(to_send_usr, message_to_send.encode('utf-8'))

        except error:
            #print(error)
            print(user_name + '已经断开连接')
            message_to_send = user_name + '已断开连接'
            broadcast(user_name, message_to_send.encode('utf-8'))
            sleep(3)
            tcpCliSock_i.close()
            break

        #tcpCliSock_i.close()


def broadcast(user_name, message):
    for usr, sock in user_list.items():
        if usr != user_name:
        #sock.sendall(bytes(message,'utf-8'))#message已经是bytes
            sock.sendall(message)

def p2p(user_name, message):#单播，新   #user_name为对方用户名
    for usr, sock in user_list.items():
        if usr == user_name:
            sock.sendall(message)


if __name__ == '__main__':
    print('正在等待客户端连接...')

    while True:
        tcpCliSock, addr = tcpSerSock.accept()  # 接收客户机socket
        print('客户端', addr[0], ':', str(addr[1]), '已连接\t')
        try:
            tcpCliSock.send('你已经连接到了服务器'.encode('utf-8') + HOST.encode('utf-8') + '\n'.encode('utf-8'))
        #tcpCliSock.send(b'please input your username:')#在客户端处理
        except:
            print('error1')

        try:
            user_name = tcpCliSock.recv(BUFFERSIZE).decode('utf-8')  # 客户机的第一条消息是客户机名字
            #print('user_name is [' + user_name +']')#连接前一条end=''的print语句
        except:
            print('error2')

        if user_name in user_list:
            tcpCliSock.sendall('用户名已被使用'.encode('utf-8'))
        else:
            try:
                user_list[user_name] = tcpCliSock  # 加入字典
                print('当前聊天室的用户为:')
                for usr in user_list.keys():
                    print('[' + usr + ']')
                print('\n\n')
                #tcpCliSock.sendall(b'%s 已连接 \n' % user_name.encode('utf-8'))#发给正在建立连接的客户端
                tcpCliSock.sendall(user_name.encode('utf-8') + '已连接\n'.encode('utf-8'))
                broadcast(user_name, user_name.encode('utf-8') + '加入了这个聊天室.\n'.encode('utf-8'))
            except:
                print('因为服务器端未输入用户名就断开连接导致出错')
            # try:
            #     t = threading.Thread(target=receiver, args=(user_name, tcpCliSock))
            #     print(t.start())
            #     print(t.join())
            # except error:
            #     print(error)
            _thread.start_new_thread(receiver,(user_name,tcpCliSock))
            #receiver(user_name,tcpCliSock)


    tcpSerSock.close()




        #pass
        # receiver(tcpCliSock)
        # t_receiver = threading.Thread(target=receiver, args=(tcpCliSock,))
        # t_receiver.start()

        #pass
