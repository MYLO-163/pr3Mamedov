
import socket
from _thread import *
def listen(con):
    while True:
        try:
            data = con.recv(1024)
            print(data.decode())
        except:
            con.close()
def send(con):
    while True:
        try:
            message = input(": ")
            con.send(message.encode())
        except:
            con.close()

client = socket.socket()  # создаем сокет клиента
hostname = socket.gethostname()  # получаем хост локальной машины
port = 12345  # устанавливаем порт сервера
client.connect((hostname, port))  # подключаемся к серверу

start_new_thread(listen, (client,))  # запускаем поток клиента
start_new_thread(send, (client,))  # запускаем поток клиента

while True:
    a=1