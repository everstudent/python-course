import json

products = []

analytics = {"title": [], "price": [], "color": []}

for i in range(3):
    product = {}
    for el in analytics:
        print('Input', el, 'for', i + 1, ' product:')
        product[el] = input();
    products.append((i + 1, product))

print('Initial products list:')
for product in products:
    print(product[0], product[1]["title"])
    for attr in product[1]:
        analytics[attr].append(product[1][attr])

print('')
print('Product analytics:')
print(json.dumps(analytics, indent=2))
