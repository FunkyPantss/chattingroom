import pymysql

USER_ID = '7'
USER_NAME = ''

FRIEND_NAME = '11111'
FRIEND_ID = '1'

chat_tcpCliSock = None
file_tcpCliSock = None

# 连接数据库
connect = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='qinchuan',
    db='ChattingRoom',
    charset='utf8'
)

# 获取游标
CURSOR = connect.cursor()

emoji = ''
