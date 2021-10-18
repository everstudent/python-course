with open('data2.txt', 'r') as f:
    line_number = 0
    for line in f:
        line_number += 1
        words = line.count(' ') + 1
        print(f"{line_number} line wods {words}")

print('---')
print('Total lines:', line_number)
