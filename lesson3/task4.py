def my_func(x, y):
    # first option - using **
    # return x**y

    # second option - using cycle
    negative = False
    if y < 0:
        y = -y
        negative = True

    res = 1
    for i in range(y):
        res = res * x

    if negative:
        res = 1 / res

    return res

x = int(input('X: '))
y = int(input('Y: '))

print('X^Y: ', my_func(x, y))
