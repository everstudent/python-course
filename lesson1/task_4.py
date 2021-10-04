number=input('Input any number: ')

i = 0
max = 0
while i < len(number):
    n = int(number[i])
    if n > max:
        max = n
    i += 1

print('Max figure is: ', max)
