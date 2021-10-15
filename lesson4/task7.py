from functools import reduce

def fact(n):
    for el in range(1, n):
        if el == 1:
            yield 1
        else:
            yield reduce(lambda a, b: a*b, range(1, el + 1))

for el in fact(10):
    print(el);
