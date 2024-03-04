import socket
from collections import deque
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE

READ = "read"
WRITE = "write"
PAUSE = "pause"
SCHEDULE = "schedule"

class EventLoop:
    def __init__(self):
        self.tasks = deque()
        self.selector = DefaultSelector()

    def run_until_complete(self, task):
        self.tasks.append(task)
        self.run()

    def sock_accept(self, sock):
        yield (READ, sock)
        client, addr = sock.accept()
        return client, addr
    
    def sock_recv(self, sock, size):
        yield READ, sock
        return sock.recv(size)

    def sock_sendall(self, sock, data):
        yield WRITE, sock
        return sock.send(data)
    
    def pause(self):
        return (PAUSE, None)
    
    def schedule(self, target):
        return (SCHEDULE, target)
    
    def start_server(self, host, port):
        return serve(self, host, port)
        
    def run(self):
        while self.tasks or self.selector.get_map():

            while self.tasks:
                task = self.tasks.popleft()

                try:
                    curr_task = next(task)
                    if curr_task:
                        tag, val  = curr_task
                    if tag == PAUSE:
                        self.tasks.append(task)
                    elif tag == SCHEDULE:
                        self.tasks.append(val)
                        if task:
                            self.tasks.append(task)
                    elif tag in (READ, WRITE):
                        sock = val
                        event = EVENT_WRITE if tag == WRITE else EVENT_READ
                        self.selector.register(sock, event, data=task)
                    else:
                        raise ValueError("invalid tag")
                    
                except StopIteration:
                    pass

            for key, _event in self.selector.select():
                self.tasks.append(key.data)
                self.selector.unregister(key.fileobj)


def serve(loop, host, port, backlog=0):
    with socket.socket() as sock:
        sock.bind((host, port))
        sock.listen(backlog)
        print("Listening on {}:{}".format(host, port))
        while True:
            conn, addr = yield from loop.sock_accept(sock)
            print("Accepted client from", addr)
            yield loop.schedule(echo(loop, conn))


def echo(loop, conn):
    while True:
        message = yield from loop.sock_recv(conn, 1024)
        if not message:
            break
        yield from loop.sock_sendall(conn, message)
    print("Closed")

        
if __name__ == "__main__":
    loop = EventLoop()
    loop.run_until_complete(loop.start_server("localhost", 8080))




# def task_foo():
#     print("1 task_foo")
#     yield pause()
#     print("2 task_foo")
#     yield pause()

# def task_bar():
#     for i in range(3):
#         print(i + 1, "task_bar")
#         yield pause()

# loop = EventLoop()
# loop.add_task(task_foo())
# loop.add_task(task_bar())
# loop.run()
        
# def countdown(n):
#     if n:
#         print("count", n)
#         yield schedule(countdown(n - 1))
#         print("done ", n)

# loop = EventLoop()
# loop.add_task(countdown(3))
# loop.run()