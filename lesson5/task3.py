with open('data3.txt') as f:
    salaries = []
    for line in f:
        surname, salary = line.split()
        salary = int(salary)
        salaries.append(salary)
        if salary < 20000:
            print(surname, ':', salary)

print('---')
avg = sum(salaries)/len(salaries)
print('Average salary:', avg)
