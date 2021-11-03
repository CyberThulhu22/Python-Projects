def Chained(functions):
    def chain(input):
        for f in functions:
            input = f(input)
        return input
    return chain

def f1(x):
    return x*2
def f2(x):
    return x+2
def f3(x):
    return x**2

print(Chained([f1,f2,f3])(0))
