# TCP 套接字编程关键语法

## 导入模块
```python
import socket
```

---

## 服务端 (Server)

### 1. 创建套接字
```python
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```
- `AF_INET`: IPv4 地址族
- `SOCK_STREAM`: TCP 流式套接字

### 2. 绑定地址和端口
```python
s.bind(('IP地址', 端口号))
```
- `'127.0.0.1'`: 本机回环地址
- `'0.0.0.0'`: 所有可用网卡

### 3. 监听连接
```python
s.listen(5)
```
- 参数: 等待连接队列的最大长度

### 4. 接受客户端连接
```python
conn, addr = s.accept()
```
- `conn`: 与客户端通信的新套接字
- `addr`: 客户端地址元组 (IP, 端口)

### 5. 接收数据
```python
data = conn.recv(1024).decode('utf-8')
```
- 参数: 最大接收字节数

### 6. 发送数据
```python
conn.send(msg.encode('utf-8'))
```

### 7. 关闭连接
```python
conn.close()
s.close()
```

---

## 客户端 (Client)

### 1. 创建套接字
```python
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

### 2. 连接服务器
```python
c.connect(('服务器IP', 端口号))
```

### 3. 发送数据
```python
c.send(msg.encode('utf-8'))
```

### 4. 接收数据
```python
data = c.recv(1024).decode('utf-8')
```

### 5. 关闭连接
```python
c.close()
```

---

## 完整示例

### 服务端
```python
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
```

### 客户端
```python
import socket

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(('127.0.0.1', 12345))

while True:
    msg = input("请输入: ")
    c.send(msg.encode("utf-8"))
    print(c.recv(1024).decode("utf-8"))
c.close()
```
