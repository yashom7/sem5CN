import socket

UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 6789

serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))

while True:
    data, addr = serverSock.recvfrom(1024)
    data = data.decode()
    print("Client: ", data)
    Reply = input('server -> ')
    Reply = Reply.encode()
    serverSock.sendto(Reply, (addr[0], addr[1]))