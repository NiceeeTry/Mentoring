from collections import deque
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE

class EventLoop:
    def __init__(self):
        self.tasks = deque()
        self.selector = DefaultSelector()

    def add_task(self, task):
        self.tasks.append(task)

    def run(self):
        while self.tasks or self.selector.get_map():

            while self.tasks:
                task = self.tasks.popleft()
                # print(task)
                try:
                    curr_task = next(task)
                    if curr_task:
                        tag, val  = curr_task
                    # print(tag, val)
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

def wait_read(sock):
    return ("read", sock)

def wait_write(sock):
    return ("write", sock)


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
def serve(host, port, backlog=0):
    with socket.socket() as sock:
        sock.bind((host, port))
        sock.listen(backlog)
        print("Listening on {}:{}".format(host, port))
        while True:
            yield wait_read(sock)
            conn, addr = sock.accept()
            print("Accepted client from", addr)
            yield schedule(echo(conn))


def echo(conn):
    while True:
        yield wait_read(conn)
        message = conn.recv(1024)
        if not message:
            break
        yield wait_write(conn)
        conn.sendall(message)
        # yield

        
if __name__ == "__main__":
    serve("localhost", 8080)
    
loop = EventLoop()
loop.add_task(countdown(3))
loop.add_task(serve("localhost", 8080))
loop.run()