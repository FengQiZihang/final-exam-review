# UDP 套接字编程关键语法

## 导入模块
```python
import socket
```

---

## 服务端 (Server)

### 1. 创建套接字
```python
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
```
- `AF_INET`: IPv4 地址族
- `SOCK_DGRAM`: UDP 数据报套接字

### 2. 绑定地址和端口
```python
s.bind(('127.0.0.1', 12345))
```

### 3. 接收数据
```python
data, addr = s.recvfrom(1024)
```
- `data`: 接收到的数据
- `addr`: 发送方地址元组 (IP, 端口)

### 4. 发送数据
```python
s.sendto(msg.encode('utf-8'), addr)
```
- 使用 `recvfrom` 获取的 `addr` 回复

---

## 客户端 (Client)

### 1. 创建套接字
```python
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
```

### 2. 指定服务器地址
```python
server_addr = ('127.0.0.1', 12345)
```

### 3. 发送数据
```python
s.sendto(msg.encode('utf-8'), server_addr)
```

### 4. 接收数据
```python
data, addr = s.recvfrom(1024)
```

---

## 完整示例

### 服务端
```python
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 12345))

while True:
    data, addr = s.recvfrom(1024)
    print(data.decode('utf-8'))
    msg = input()
    s.sendto(msg.encode('utf-8'), addr)
```

### 客户端
```python
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_addr = ('127.0.0.1', 12345)

while True:
    msg = input("请输入: ")
    s.sendto(msg.encode('utf-8'), server_addr)
    data, addr = s.recvfrom(1024)
    print(data.decode('utf-8'))
```

---

## TCP 与 UDP 对比

| 对比项 | TCP | UDP |
|--------|-----|-----|
| 套接字类型 | `SOCK_STREAM` | `SOCK_DGRAM` |
| 连接 | 需要 `connect()` | 无需连接 |
| 服务端监听 | `listen()` + `accept()` | 直接 `recvfrom()` |
| 发送 | `send()` | `sendto(data, addr)` |
| 接收 | `recv()` | `recvfrom()` 返回 (data, addr) |
| 可靠性 | 可靠传输 | 不可靠传输 |
