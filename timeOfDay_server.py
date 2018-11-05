import time
import socket

UDP_IP_ADDRESS = '127.0.0.1'
UDP_PORT_NO = 1237

serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))

while True:
    data, addr = serverSock.recvfrom(1024)
    data.decode()

    print("Client :", addr[0], addr[1])
    myT = time.localtime()
    Time = str(myT.tm_hour) + 'hrs' + str(myT.tm_min) + 'mins' + str(myT.tm_sec) + 'sec'
    Date = str(myT.tm_mday) + '/' + str(myT.tm_mon) + '/' + str(myT.tm_year)

    Reply = 'Date -> ' + Date + 'Time -> ' + Time
    Reply = Reply.encode()
    serverSock.sendto(Reply, (addr[0], addr[1]))

serverSock.close()