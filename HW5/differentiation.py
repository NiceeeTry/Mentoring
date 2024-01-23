class Expr:
    def __call__(self, **context):
        pass

    def d(self, wrt):
        pass


class Const(Expr):
    def __init__(self, val):
        self.val = val

    def __call__(self, **context):
        return self.val
    
    def d(self, wrt):
        return Const(0)

class Var(Expr):
    def __init__(self, var):
        self.var = var

    def __call__(self, **context):
        return context.get(self.var, 0)
    
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

class Sum(BinOp):
    def __call__(self, **context):
        return self.expr1(**context) + self.expr2(**context)
    
    def d(self, wrt):
        return Sum(self.expr1.d(wrt), self.expr2.d(wrt))

# print(Sum(x, y)(x = 1, y = 3))
# print(Sum(x, y).d(x)(x = 2, y=3))

class Product(BinOp):
    def __call__(self, **context):
        return self.expr1(**context) * self.expr2(**context)
    
    def d(self, wrt):
        return Sum(Product(self.expr1.d(wrt), self.expr2), Product(self.expr1, self.expr2.d(wrt)))

# print(Product(x, y)(x=2, y=3))
# print(Product(x, y).d(x)(x=2, y=3))


class Fraction(BinOp):
    def __call__(self, **context):
        return self.expr1(**context) / self.expr2(**context)
    
    def d(self, wrt):
        return Fraction(Sum(Product(self.expr2, self.expr1.d(wrt)), Product(Product(self.expr1, self.expr2.d(wrt)), Const(-1))), Product(self.expr2, self.expr2))

print(Fraction(x, y)(x = 4, y = 5))
print(Fraction(x, y).d(x)(x = 4, y = 5))

# print(Sum(x, Product(x, x)).d(x)(x=42)) 

# print(Product(x, Sum(x, C(2)))(x=42))

# print(Fraction(Product(x, y), Sum(C(42), x)).d(x)(x=42, y=24))  # 0.14285714285714285

# print(Fraction(Product(x, y), Sum(C(42), x)).d(y)(x=42, y=24))  # 0.5

