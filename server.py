import socket

server = socket. socket (socket.AF_INET, socket .SOCK_STREAM)
server.bind(("127.0.0.1", 8080)) #10.128.0.8
server.listen()
while True:
    user, address = server.accept()
    user.send(input().encode("utf-8"))
    data = user.recv(1024)
    print(data.decode("utf-8"))