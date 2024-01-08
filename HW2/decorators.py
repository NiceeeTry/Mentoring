from functools import reduce, wraps

ITERABLE_ERROR = "input has to be an iterable object"
ARGUMENTS_NUMBER_ERROR = "minimum 2 arguments required"

# ----------------------------- 1 -----------------
def union(*args):
    if all(isinstance(obj, (list, tuple, dict, set)) for obj in args):
        return reduce(lambda x, y: x.union(y), args, set())

    return TypeError(ITERABLE_ERROR)


def digits(num):
    if num == 0:
        return [0]
    res = []
    while num > 0:
       res.insert(0, num % 10)
       num //= 10
    return res 


def lcm(*args):
    if len(args) < 2:
        return ValueError(ARGUMENTS_NUMBER_ERROR)

    def gcd(a, b):
        while b:
            a, b = b, a%b
        return a 

    def lcm_for_two_arg(a, b):
        return (a * b) // gcd(a, b)    

    return reduce(lcm_for_two_arg, args)   


# def compose(*args):

#     def inner(num): 
#         res = num
#         for f in reversed(args):
#             res = f(res)
#         return res
#     return inner

def compose(*args):
    return lambda x: reduce(lambda acc, f: f(acc), reversed(args), x)

# print(union({1, 2, 3}, {10}, {2, 6}))
# print(digits(1914))
# print(lcm(100500, 42))

# f = compose(lambda x: 2 * x, lambda x: x + 1, lambda x: x % 9)
# print(f(42))

# ----------------------------- 2 -----------------

def once(func):
    @wraps(func)
    def inner(*args, **kwargs):
        if not hasattr(inner, "result"):
            inner.result = func(*args, **kwargs)
        return inner.result
    return inner

@once
def initialize_settings():
    print("Settings initialized")
    return {"token": 42}


def trace_if(predicate):
    def trace(func):
        @wraps(func)
        def inner(*args, **kwargs):
            if predicate(*args, **kwargs):
                print(func.__name__, args, kwargs)
            return func(*args, **kwargs)
        return inner

    return trace

@trace_if(lambda x, y, **kwargs: kwargs.get("integral"))
def div(x, y, integral=False):
    return x // y if integral else x / y


def n_times(num):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            for _ in range(num):
                func(*args, **kwargs)
        return inner
    return wrapper


@n_times(3)
def do_something():
    print("Something is going on")

# print(initialize_settings())
# print(initialize_settings())
# print(initialize_settings())
# initialize_settings()
# initialize_settings()
# initialize_settings()

# print(div(4,2, integral = True))

# do_something()

# ----------------------------- 3 and 4 -----------------

def project():
    tasks = {}
    dependencies = {}

    def register(func=None, *, depends_on=None):
        if func is None:
            return lambda f: register(f, depends_on=depends_on)

        wraps(func)

        task_name = func.__name__
        tasks[task_name] = func

        if depends_on is not None:
            dependencies[task_name] = depends_on

        def wrapper(*args, **kwargs):
            stack = []

            def dfs(task):
                if task not in stack:
                    stack.append(task)
                    for dependency in dependencies.get(task, []):
                        dfs(dependency)

            dfs(task_name)

            for to_do in reversed(stack):
                tasks[to_do]()

        
        wrapper.get_dependencies = lambda: dependencies.get(task_name, [])

        return wrapper

    def get_all():
        return list(tasks.keys())

    register.get_all = get_all
    return register



register = project()

@register
def do_something():
    print("doing something")

@register(depends_on=["do_something"])
def do_other_thing():
    print("doing other thing")



# print(register.get_all())
# print(do_something.get_dependencies())
# print(do_other_thing.get_dependencies())

# do_something()
# do_other_thing()

