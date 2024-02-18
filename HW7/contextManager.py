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