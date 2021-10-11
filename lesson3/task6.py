def int_func(str):
    list = str.split()
    res = []
    for word in list:
        res.append(word[0].upper() + word[1:])

    return ' '.join(res)

print(int_func('denys golotiuk homework is good'))
