class Expr:
    def __call__(self, **context):
        pass

    def d(self, wrt):
        pass

    def __neg__(self):
        return Product(Const(-1), self)
    def __pos__(self):
        self
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

    def __str__(self):
        return f"{self.val}"

    def __call__(self, **context):
        return self.val
    
    def d(self, wrt):
        return Const(0)

class Var(Expr):
    def __init__(self, var):
        self.var = var

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

# print(C(42)())
# print(C(42).d(V("x"))())
# print(V("x")(x=42))
# print(V("x").d(V("x"))())
# print(V("x").d(V("y"))())

x = V("x")
y = V("y") 
class BinOp(Expr):
    def __init__(self, expr1, expr2):
        self.expr1, self.expr2 = expr1, expr2
    
    def operator(self):
        pass

    def __str__(self):
        return f"({self.operator()} {self.expr1} {self.expr2})"

class Sum(BinOp):
    # def __str__(self):
    #     return f"(+ {self.expr1} {self.expr2})"
    def operator(self):
        return "+"

    def __call__(self, **context):
        return self.expr1(**context) + self.expr2(**context)
    
    def d(self, wrt):
        return Sum(self.expr1.d(wrt), self.expr2.d(wrt))

# print(Sum(x, y)(x = 1, y = 3))
# print(Sum(x, y).d(x)(x = 2, y=3))
# print(Sum(x, y)(x=1,y=4))

class Product(BinOp):
    def operator(self):
        return "*"
    
    def __call__(self, **context):
        return self.expr1(**context) * self.expr2(**context)
    
    def d(self, wrt):
        return Sum(Product(self.expr1.d(wrt), self.expr2), Product(self.expr1, self.expr2.d(wrt)))

# print(Product(x, y)(x=2, y=3))
# print(Product(x, y).d(x)(x=2, y=3))


class Fraction(BinOp):
    def operator(self):
        return "/"
    
    def __call__(self, **context):
        return self.expr1(**context) / self.expr2(**context)
    
    def d(self, wrt):
        return Fraction(Sum(Product(self.expr2, self.expr1.d(wrt)), Product(Product(self.expr1, self.expr2.d(wrt)), Const(-1))), Product(self.expr2, self.expr2))

# print(Fraction(x, y)(x = 4, y = 5))
# print(Fraction(x, y).d(x)(x = 4, y = 5))

# print(Sum(x, Product(x, x)).d(x)(x=42)) 

# print(Product(x, Sum(x, C(2)))(x=42))

# print(Fraction(Product(x, y), Sum(C(42), x)).d(x)(x=42, y=24))  # 0.14285714285714285

# print(Fraction(Product(x, y), Sum(C(42), x)).d(y)(x=42, y=24))  # 0.5



class Power(BinOp):
    def operator(self):
        return "**"

    def __call__(self, **context):
        base, exp = self.expr1(**context), self.expr2(**context)
        return base ** exp

    def d(self, wrt):
        return Product(Product(Power(self.expr1, Sum(self.expr2, Const(-1))), self.expr2), self.expr1.d(wrt))


# print(Power(Fraction(V("x"), C(4)), C(2))(x=42))
# print(Power(Fraction(V("x"), C(4)), C(2)).d(V("x"))(x=42))
# print(Power(Fraction(V("x"), C(4)), C(-9))(x=42))
    

# print(Sum(x, Product(x, x)).d(x))
# print(Product(x, Sum(x, C(2))))
# print(Power(Fraction(x, C(4)), C(2)))

# print((C(1) - V("x")) ** C(3) + V("x"))
    
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


expr = (V("x") + C(-1)) ** C(3) + V("x")
zero = newton_raphson(expr, 0.5, threshold=1e-4)
print(expr)
print(zero, expr(x=zero))