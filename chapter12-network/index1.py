import socket
import time

HOST = 'data.pr4e.org'
PORT = 80
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((HOST, PORT))
mysock.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')
count = 0
pic = b''

while True:
    data = mysock.recv(1024 * 100)
    if len(data) < 1:
        break
    time.sleep(3)
    count += len(data)
    print(len(data), count)
    pic += data

mysock.close()

pos = pic.find(b'\r\n\r\n')
print('header len ', pos)
print(pic[:pos].decode())

pic = pic[pos + 4:]
out = open('img.jpg', 'wb')
out.write(pic)
out.flush()
out.close()
