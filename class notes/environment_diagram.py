from operator import add


def kit(a):
    def foo(b):
        return a * tac(a, b)

    return foo


tac = add
result1 = kit(2)(3)
print(result1)

tac = max
result1 = kit(2)(3)
print(result1)
