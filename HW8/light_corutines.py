from collections import deque
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE

class EventLoop:
    def __init__(self):
        self.tasks = deque()
        self.selector = DefaultSelector()

    def add_task(self, task):
        self.tasks.append(task)

    def sock_accept(self, sock):
        yield ("read", sock)
        client, addr = sock.accept()
        return client, addr
    
    def sock_recv(self, sock, size):
        yield "read", sock
        return sock.recv(size)

    def sock_sendall(self, sock, data):
        yield "write", sock
        return sock.send(data)

    def run(self):
        while self.tasks or self.selector.get_map():

            while self.tasks:
                task = self.tasks.popleft()
                try:
                    curr_task = next(task)
                    if curr_task:
                        tag, val  = curr_task
                    if tag == "pause":
                        self.add_task(task)
                    elif tag == "schedule":
                        self.add_task(val)
                        if task:
                            self.add_task(task)
                    elif tag in ("read", "write"):
                        sock = val
                        event = EVENT_WRITE if tag == "write" else EVENT_READ
                        self.selector.register(sock, event, data=task)
                    else:
                        raise ValueError("invalid tag")
                    
                except StopIteration:
                    pass

            for key, _event in self.selector.select():
                self.add_task(key.data)
                self.selector.unregister(key.fileobj)


def pause():
    return ("pause", None)

def schedule(target):
    return ("schedule", target)


def task_foo():
    print("1 task_foo")
    yield pause()
    print("2 task_foo")
    yield pause()

def task_bar():
    for i in range(3):
        print(i + 1, "task_bar")
        yield pause()

# loop = EventLoop()
# loop.add_task(task_foo())
# loop.add_task(task_bar())
# loop.run()
        
def countdown(n):
    if n:
        print("count", n)
        yield schedule(countdown(n - 1))
        print("done ", n)

# loop = EventLoop()
# loop.add_task(countdown(3))
# loop.run()

import socket
def serve(loop, host, port, backlog=0):
    with socket.socket() as sock:
        sock.bind((host, port))
        sock.listen(backlog)
        print("Listening on {}:{}".format(host, port))
        while True:
            conn, addr = yield from loop.sock_accept(sock)
            # conn, addr = sock.accept()
            print("Accepted client from", addr)
            yield schedule(echo(loop, conn))


def echo(loop, conn):
    while True:
        message = yield from loop.sock_recv(conn, 1024)
        # message = conn.recv(1024)
        if not message:
            break
        yield from loop.sock_sendall(conn, message)
        # yield wait_write(conn)
        # conn.sendall(message)
    print("Closed")

        
if __name__ == "__main__":
    
    loop = EventLoop()
    # loop.add_task(countdown(3)) 
    loop.add_task(serve(loop, "localhost", 8080))
    loop.run()