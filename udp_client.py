import socket

UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 6789

clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    Message = input('Client -> ')
    if Message == 'quit':
        break
    Message = Message.encode()
    clientSock.sendto(Message, (UDP_IP_ADDRESS, UDP_PORT_NO))

    reply, addr = clientSock.recvfrom(1024)

    print('Server: ', reply.decode())