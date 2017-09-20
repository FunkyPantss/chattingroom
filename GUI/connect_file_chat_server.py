from socket import *


HOST = '127.0.0.1'
CHAT_PORT = 44444
BUFFERSIZE = 1024
CHAT_ADDR = (HOST, CHAT_PORT)

FILE_ADDR = 44445

CONNECTED = False

while True:
    try:
        