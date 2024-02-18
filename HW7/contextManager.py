class assert_raises:
    def __init__(self, err):
        self.error = err
    
    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        if type is None:
            raise AssertionError(f"did not raise '{self.error.__name__}'")
        elif not issubclass(self.error, type):
            return False
        else:
            return True
    
with assert_raises(ValueError):
    "foobar".split("")
# with assert_raises(ValueError):
#     pass
# with assert_raises(ValueError):
#     raise TypeError
    

class closing:
    def __init__(self, obj):
        self.obj = obj
    
    def __enter__(self):
        return self.obj
    
    def __exit__(self, *err):
        self.obj.close()

with closing(open("example.txt")) as handle:
    copy = handle

# print(copy.closed)
    

from traceback import print_exception

class log_exceptions:

    def __enter__(self):
        return self
    
    def __exit__(self, type, value, traceback):
        if type is not None:
            print_exception(type, value, traceback)
            return True
        return False

def f():
    with log_exceptions():
        {}["foobar"]
    return 42

# print(f())
from functools import wraps

def with_context(context):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            with context:
                return func(*args, **kwargs)
        return inner
    return wrapper

# from contextlib import redirect_stdout
# import io
# handle = io.StringIO()

# @with_context(redirect_stdout(handle))
# def f():
#     print("Hello world!")

# f()
# print(handle.getvalue())