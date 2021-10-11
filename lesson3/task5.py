global_sum = 0

def string_to_sum(str):
    global global_sum

    if not str:
        return True

    nums = str.split()

    stop = False
    for num in nums:
        if num == 'STOP':
            stop = True
        else:
            global_sum += int(num)

    print('Sum so far:', global_sum)

    return stop

while True:
    numbers = input('Input numbers: ')
    stop = string_to_sum(numbers)
    if stop:
        break;
