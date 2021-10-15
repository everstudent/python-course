from itertools import count, cycle


# First iterator
def gen_1(start, stop):
    for el in count(start):
        if ( el > stop ):
            break;
        yield el

print('First iterator test:')
for i in gen_1(3, 10):
    print(i)



# Second iterator
def gen_2(list, times):
    total = len(list) * times
    for el in cycle(list):
        total -= 1;
        if total < 0:
            break
        yield el

print('Second iterator test:')
for i in gen_2(['a', 'c', 'e'], 3):
    print(i)
