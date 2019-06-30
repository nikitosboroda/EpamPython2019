from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

"""https://medium.com/swlh/lets-write-a-chat-app-in-python-f6783a9ac170"""


def accept_incoming_connections():
    """Принимаем подкдючение юзера,
        приветствуем его."""
    while True:
        client, client_address = SERVER.accept()  # возвращет сокет и адрес клиента.
        # сокет используется для посылки клиенту данных
        print(f"{client_address} has connected.")
        client.send(bytes("Greetings from the cave!"
                          "Now type your name and press enter!", "utf8"))
        addresses[client] = client_address  # добавляем адрес киента в словарь
        # для дальнейшей работы с ним
        Thread(target=handle_client, args=(client,)).start()  # запускаем функцию
        # handle_client в отдельном потоке


def handle_client(client):  # сокет клиента - аргумент
    """Обрабатывает одно клиентское соединение."""

    name = client.recv(BUFSIZ).decode("utf8")  # принимаем введенное
    # имя пользователя
    welcome = 'Welcome %s! If you ever want to quit, type {quit} to exit.' % name
    # приветствуем его
    client.send(bytes(welcome, "utf8"))
    msg = "%s has joined the chat!" % name
    broadcast(bytes(msg, "utf8"))

    clients[client] = name
    # ловим сообщения клиента, если оно не {quit}, то транслируем его
    # остальным пользователям
    while True:
        msg = client.recv(BUFSIZ)
        if msg != bytes("{quit}", "utf8"):
            broadcast(msg, name + ": ")
        else:
            client.send(bytes("{quit}", "utf8"))
            client.close()
            del clients[client]
            broadcast(bytes("%s has left the chat." % name, "utf8"))
            break


def broadcast(msg, prefix=""):
    """Транслирует сообщение всем пользователям"""

    for sock in clients:
        sock.send(bytes(prefix, "utf8") + msg)


clients = {}
addresses = {}
# задаем данные для сервера и запускаем его
HOST = ''
PORT = 33000
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == "__main__":
    SERVER.listen(5)  # включаем режим прослушивания, в очереди может быть максимум 5
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)  # запускаем функцию в отдельном потоке
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()  # с помощью join() ждем пока поток закончит
    SERVER.close()  # закрываем соединение
