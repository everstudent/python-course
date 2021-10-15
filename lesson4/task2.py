import random

original_list = [random.randint(1, 100) for el in range(20)]
print('Original list:')
print(original_list)

result_list = [el for i, el in enumerate(original_list) if el > original_list[i-1]]
print('Resulting list:')
print(result_list)
