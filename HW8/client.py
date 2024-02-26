
import socket
import time

HOST = "localhost"  # The server's hostname or IP address
PORT = 8080  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    for _ in range(100):
        time.sleep(0.5)
        s.sendall(b"Hello, world")
        data = s.recv(1024)
        print(f"Received {data!r}")     