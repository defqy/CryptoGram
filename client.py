import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 8080)) #158.160.106.231
receiver = socket.socket()
while True:
    data = client.recv(1024)
    print(data.decode("utf-8"))
    client.send(input().encode("utf-8"))