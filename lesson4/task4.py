original = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

resulting = [el for el in original if original.count(el) == 1 ]

print(resulting)
