from collections import deque

class EventLoop:
    def __init__(self):
        self.tasks = deque()

    def add_task(self, task):
        self.tasks.append(task)

    def run(self):
        while self.tasks:
            task = self.tasks.popleft()
            try:
                tag, val = next(task)
                # print(tag, val)
                if tag == "pause":
                    self.add_task(task)
                elif tag == "schedule":
                    self.add_task(val)
                    self.add_task(task)
                        
                else:
                    raise ValueError("invalid tag")
                
            except StopIteration:
                pass

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

loop = EventLoop()
loop.add_task(countdown(3))
loop.run()


    
