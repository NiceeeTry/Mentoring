import inspect
def peel(cls):
    if inspect.isclass(cls):
        res = {s for s in dir(cls) if not s.startswith("_")}
        return res

    

def implements(interface):
    def wraps(cls):
        list_of_cls = {m for m in dir(cls) if not m.startswith("_")}
        list_to_impl = {m for m in dir(interface) if not m.startswith("_")}
        if list_of_cls >= list_to_impl:
            return cls
        diff = " ".join(list_to_impl.difference(list_of_cls))
        assert False, f"method '{diff}' not implemented"
    return wraps
     


class Expr:
    def __call__(self, **context):
        pass

    def d(self, wrt):
        pass

    @property
    def is_constexpr(self):
        pass

    @property
    def simplified(self):
        pass

    def __neg__(self):
        return Product(Const(-1), self)
    
    def __pos__(self):
        return self

    def __add__(self, e2):
        return Sum(self, e2)
    
    def __sub__(self, e2):
        return Sum(self, -e2)
    
    def __mul__(self, e2):
        return Product(self, e2)
    
    def __truediv__(self, e2):
        return Fraction(self, e2)
    
    def __pow__(self, e2):
        return Power(self, e2)
    

class Const(Expr):
    def __init__(self, val):
        self.val = val

    @property
    def is_constexpr(self):
        return True

    @property
    def simplified(self):
        return self
    
    def __str__(self):
        return f"{self.val}"

    def __call__(self, **context):
        return self.val
    
    def d(self, wrt):
        return Const(0)

class Var(Expr):
    def __init__(self, var):
        self.var = var

    @property
    def is_constexpr(self):
        return False

    @property
    def simplified(self):
        return self

    def __str__(self):
        return f"{self.var}"

    def __call__(self, **context):
        return context[self.var]
    
    def d(self, wrt):
        return Const(1 if self.var == wrt.var else 0)


def V(name):
    return Var(name)

def C(val):
    return Const(val)


x = V("x")
y = V("y") 

class BinOp(Expr):
    def __init__(self, expr1, expr2):
        self.expr1, self.expr2 = expr1, expr2
    
    @property
    def is_constexpr(self):
        return self.expr1.is_constexpr and self.expr2.is_constexpr

    @property
    def simplified(self):
        expr1_simplified = self.expr1.simplified
        expr2_simplified = self.expr2.simplified

        if expr1_simplified.is_constexpr and expr2_simplified.is_constexpr:
            return Const(self.__class__(expr1_simplified, expr2_simplified)())
        return self.__class__(expr1_simplified, expr2_simplified)

    def operator(self):
        pass

    def __str__(self):
        return f"({self.operator()} {self.expr1} {self.expr2})"

class Sum(BinOp):
    def operator(self):
        return "+"

    def __call__(self, **context):
        return self.expr1(**context) + self.expr2(**context)
    
    def d(self, wrt):
        return Sum(self.expr1.d(wrt), self.expr2.d(wrt))


class Product(BinOp):
    def operator(self):
        return "*"
    
    def __call__(self, **context):
        return self.expr1(**context) * self.expr2(**context)
    
    def d(self, wrt):
        return Sum(Product(self.expr1.d(wrt), self.expr2), Product(self.expr1, self.expr2.d(wrt)))

class Fraction(BinOp):
    def operator(self):
        return "/"
    
    def __call__(self, **context):
        return self.expr1(**context) / self.expr2(**context)
    
    def d(self, wrt):
        return Fraction(Sum(Product(self.expr2, self.expr1.d(wrt)), Product(Product(self.expr1, self.expr2.d(wrt)), Const(-1))), Product(self.expr2, self.expr2))


class Power(BinOp):
    def operator(self):
        return "**"

    def __call__(self, **context):
        base, exp = self.expr1(**context), self.expr2(**context)
        return base ** exp

    def d(self, wrt):
        return Product(Product(Power(self.expr1, Sum(self.expr2, Const(-1))), self.expr2), self.expr1.d(wrt))

    
def newton_raphson(f, x0, threshold):
    print(threshold)
    x = x0
    while True:
        fx = f(x=x)
        dfx = f.d(Var("x"))(x=x)
        x_next = x - fx/dfx
        if abs(x_next - x) <= threshold:
            return x_next
        x = x_next


