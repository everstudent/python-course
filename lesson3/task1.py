def delete(a, b):
    if b == 0:
        return False

    return a / b


a = int(input('A: '))
b = int(input('B: '))

print('Delete operation result:', delete(a, b))
