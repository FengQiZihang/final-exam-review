import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 12345))
s.listen(5)

conn, addr = s.accept()
while True:
    print(conn.recv(1024).decode('utf-8'))
    msg = input()
    conn.send(msg.encode('utf-8'))
conn.close()
s.close()
