result = {}

with open('data6.txt') as f:
    for l in f:
        types = l.split()
        for i, el in enumerate(types):
            if i == 0:
                title = el[:-1]
            else:
                if el.find('(') > 0:
                    items = int(el[0:el.find('(')])
                    result[title] = result[title] + items if title in result else items

print(result)
