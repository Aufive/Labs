# -*- coding: utf-8 -*-
import socket
import cezar

client = socket.socket(

    socket.AF_INET,
    socket.SOCK_STREAM,

)

client.connect(
    ('192.168.0.102', 1423)
)

while True:
    data = client.recv(2048)  #receive, пишем какое количество данных хотим получить за один пакет

    print(data.decode('utf-8'))
    while True:
        message = input("Word for encryption: ").upper()
        result = ''
        for i in message:
            place = cezar.alfa.find(i)
            new_place = place + cezar.kliucz
            if i in cezar.alfa:
             result += cezar.alfa[new_place]
            else:
             result += i
        print('Слово с кодировкой:', result)
        print(result)
        client.send(result.encode('utf-8'))