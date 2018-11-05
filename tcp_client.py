import socket

host = '127.0.0.1'
port = 5005

clientSock = socket.socket()
clientSock.connect((host, port))

message = input('Client -> ')

while message != 'q':
    clientSock.send(message.encode())
    data = clientSock.recv(1024).decode()

    print('Server: ', data)
    message = input('Client -> ')

clientSock.close()