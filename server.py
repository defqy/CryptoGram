import socket
server = socket. socket (socket.AF_INET, socket .SOCK_STREAM)
print('Server is starting...')
server.bind(("127.0.0.1", 8080)) #10.128.0.8 локальный ip
print('Server is looking for a clients...')
server.listen(5)
while True:
    user, address = server.accept()
    user.send(input().encode("utf-8"))
    data = user.recv(1024)
    print(data.decode("utf-8"))