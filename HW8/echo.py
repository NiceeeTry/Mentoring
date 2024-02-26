import socket
def serve(host, port, backlog=0):
    with socket.socket() as sock:
        # Свяжем сокет с указанным хостом и портом.
        sock.bind((host, port))
        # И будем ждать подключений от клиентов. Значение ``backlog``
        # определяет, сколько клиентов могут одновременно ожидать
        # подключения.
        sock.listen(backlog)
        print("Listening on {}:{}".format(host, port))
        while True:
            # Вызов метода ``socket.accept`` блокируется до тех пор,
            # пока не появится следующий клиент.
            conn, addr = sock.accept()
            print("Accepted client from", addr)
            echo(conn)
        # conn.close()

def echo(conn):
    while True:
        # Аргумент метода ``socket.recv`` --- максимальный размер сообщения,
        # которое готов принять сервер (в байтах).
        message = conn.recv(1024)
        if not message:
            # Пустое сообщение --- признак того, что клиент разорвал
            # соединение.
            break
        conn.sendall(message)
        # conn.sendall(b"h1")
        # conn.close()
        
if __name__ == "__main__":
    serve("localhost", 8080)



# import socket
# import threading

# HEADER = 64
# PORT = 5050
# FORMAT = 'utf-8'
# DISCONNECT_MESSAGE = "!DISCONNECT"
# # SERVER = "192.168.140.73"
# SERVER = socket.gethostbyname(socket.gethostname())
# # print(SERVER)
# ADDR = (SERVER, PORT)
# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind(ADDR)

# def handle_client(conn, addr):
#     print(f"New connection {addr}")
#     connected = True
#     while connected:
#         msg_length = conn.recv(HEADER).decode(FORMAT)
#         if msg_length:
#             msg_length = int(msg_length)
#             msg = conn.recv(msg_length).decode(FORMAT)
#             if msg == DISCONNECT_MESSAGE:
#                 connected = False
#             print(f"{addr}: {msg}")
#     conn.close()

# def start():
#     server.listen()
#     while True:
#         conn, addr = server.accept()
#         thread = threading.Thread(target=handle_client, args=(conn, addr))
#         thread.start()
#         print(f"active connections {threading.active_count()-1}")

# print("starting...")
# start()