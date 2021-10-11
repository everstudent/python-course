def my_func(a, b, c):
    all = [a, b, c];
    minimum = min(all);

    mult = 1

    for num in all:
        if num != minimum:
            mult = mult * num

    return mult

print( 'Test1:', my_func(3, 1, 7) )
print( 'Test2:', my_func(3, 5, 4) )
