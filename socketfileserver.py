import socket

HOST = 'localhost'
PORT = 1307
BUFFER_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (HOST, PORT)
sock.bind(server_address)
sock.listen(1)
client_socket, client_address = sock.accept()
print("Connected %s successfully" % str(client_address))

with open('test.jpg', 'wb') as f:
    while True:
        data = sock.recv(BUFFER_SIZE)
        f.write(data)
    sock.close()