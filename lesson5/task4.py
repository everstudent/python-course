map = {
    'One': 'Раз',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}

with open('data4.txt') as f:
    with open('data4_ru.txt', 'w') as ru_f:
        for l in f:
            eng = l[0:l.find('—') - 1]
            ru_l = map[eng] + l[l.find('—') - 1:]
            ru_f.write(ru_l)

print('Done')
