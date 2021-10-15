from sys import argv, exit

if len(argv) != 4:
    print('Please pass 3 arguments: {hours} {salary} {bonus}')
    exit()

script, hours, salary, bonuses = argv

result = int(hours) * int(salary) + int(bonuses)
print('Resulting payment: ', result);
