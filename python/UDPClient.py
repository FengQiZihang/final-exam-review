import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_addr = ('127.0.0.1', 12345)

while True:
    msg = input("请输入: ")
    s.sendto(msg.encode('utf-8'), server_addr)
    data, addr = s.recvfrom(1024)
    print(data.decode('utf-8'))
