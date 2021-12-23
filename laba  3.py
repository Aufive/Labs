import socket
import decezar

server = socket.socket(

    socket.AF_INET,
    socket.SOCK_STREAM,

)

server.bind(
    ('0.0.0.0', 1423)
)

server.listen()  #дает зеленый свет о том, что мы можем принимать сообщения

while True:
    user_socket, adress = server.accept()#тут ми  приймаємо підключення
    user_socket.send('You are connected'.encode('utf-8'))   #(Серверы и клиенты обмениваются между собой байтами(в виде пакетов))

    while True:
        data = user_socket.recv(2048)
        slovo = data.decode('utf-8')
        print(slovo)
        result = ''
        for i in slovo:
            place = decezar.alfa.find(i)
            new_place = place + decezar.kliucz
            if i in decezar.alfa:
                result += decezar.alfa[new_place] # перевірка букви якщо вона є в алфівіті ми закидуємо в результат
            else:
                result += i
        print('Слово без кодировки:', result)