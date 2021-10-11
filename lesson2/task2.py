list = []

for i in range(5):
    val = input("Input #{} element: ".format(i+1));
    list.append(val)

for i,el in enumerate(list):
    if i % 2 != 0:
        continue

    if i+1 >= len(list):
        break

    var1, var2 = list[i], list[i + 1]
    list[i], list[i+1] = var2, var1

print('List with neibour elements swapped:', list)
