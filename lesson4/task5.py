from functools import reduce

list = [el for el in range(100, 1000 + 1) if el % 2 == 0]
multiply = reduce(lambda a, b: a*b, list);
print(multiply)
