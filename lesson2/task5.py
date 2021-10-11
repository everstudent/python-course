list = [7, 5, 3, 3, 2]
rate = int(input('Input rate number: '))
inserted = False

for i, el in enumerate(list):
    if el <= rate:
        inserted = True
        list.insert(i, rate)
        break

if not inserted:
    list.append(rate)

print('Resulting rating:', list)
