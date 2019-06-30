from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter


def receive():
    """Обработка входящих сообщений"""
    while True:  # бесконечный цикл т.к. мы получаем сообщения независимо от наших
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")  # чтение данных из сокета
            msg_list.insert(tkinter.END, msg)
        except OSError:  # возможно пользователь покинул чат
            break


def send(event=None):  # event нужен для ГУИ
    """Обработка отправляемых сообщений"""
    # my_msg - ГУИ поле ввода
    msg = my_msg.get()  # извлекаем сообщение для отправки
    my_msg.set("")  # Очищаем поле ввода
    client_socket.send(bytes(msg, "utf8"))  # передаем сообщение серверу
    if msg == "{quit}":
        client_socket.close()  # закрываем сессию
        top.quit()  # и приложение


def on_closing(event=None):
    """Вызывается, когда закрывается ГУИ окно руками"""
    my_msg.set("{quit}")
    send()


# Создаем графический интерфейс приожения с названием Chatter

top = tkinter.Tk()
top.title("Chatter")

messages_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar()  # Строка для ввода сообщений
my_msg.set("Type your messages here.")
scrollbar = tkinter.Scrollbar(messages_frame)  # Для перемещения по чату

# создаем хранилище сообщений и запоняем его
msg_list = tkinter.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()

# создаем поле  ввода для сообщений пользователей и отправляем их на сервер
entry_field = tkinter.Entry(top, textvariable=my_msg)
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = tkinter.Button(top, text="Send", command=send)
send_button.pack()

# обрабатываем закрытие окна
top.protocol("WM_DELETE_WINDOW", on_closing)

# подключение к серверу
HOST = input('Enter host: ') # localhost
PORT = input('Enter port: ')
if not PORT:
    PORT = 33000
else:
    PORT = int(PORT)

BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

# заупскаем в отдельном потоке получение сообщений
receive_thread = Thread(target=receive)
receive_thread.start()
tkinter.mainloop()  # запуск ГУИ
