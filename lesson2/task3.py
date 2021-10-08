month=int(input('Input any month number, 1...12: '))

months = {0: 'Winter', 1: 'Spring', 2: 'Summer', 3: 'Fall'}
if month >= 12:
    month = 1

if month < 1:
    month = 1

print(months[month // 3]);
