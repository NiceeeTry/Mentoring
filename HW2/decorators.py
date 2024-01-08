from functools import reduce, wraps

# ----------------------------- 1 -----------------
def union(*args):
    if all(isinstance(obj, (list, tuple, dict, set)) for obj in args):
        return reduce(lambda x, y: x.union(y), args, set())
    return TypeError("input has to be an iterable object")


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
        return ValueError("minimum 2 arguments required")

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

# ----------------------------- 3 -----------------