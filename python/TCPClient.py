import socket

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(('127.0.0.1', 12345))

while True:
    msg = input("请输入: ")
    c.send(msg.encode("utf-8"))
    print(c.recv(1024).decode("utf-8"))
c.close()
