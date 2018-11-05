import socket

host = '127.0.0.1'
port = 5005

serverSock = socket.socket()
serverSock.bind((host, port))

serverSock.listen(1)
connection, addr = serverSock.accept()
print("Connnection from: ", addr)
while True:
    data = connection.recv(1024).decode()
    if not data:
        break
    
    print("Client: ", data)
    msg = input('Server -> ')
    connection.send(msg.encode())
    
connection.close()


