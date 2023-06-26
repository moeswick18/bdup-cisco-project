def f(x):
    z = 2
    def g(y):
        return z*x + y
    return g
a = 5
b = 1
h = f(a)
print(h.__code__.co_freevars[0], "=", h.__closure__[0].cell_contents)
print(h.__code__.co_freevars[1], "=", h.__closure__[1].cell_contents)