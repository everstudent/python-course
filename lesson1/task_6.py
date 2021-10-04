a = int(input('Please input a: '))
b = int(input('Please input b: '))

days = 0
day_value = a
while day_value < b:
    days += 1
    day_value *= 1.1

print('Day number is {0} (runner will make {1:.1f}km on this day)'.format(days, day_value))
