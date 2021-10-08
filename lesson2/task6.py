import json

products = [
  (1, {"title": "Laptop", "price": "25000", "color": "black"}),
  (2, {"title": "Mobile", "price": "15000", "color": "gray"}),
  (3, {"title": "TV", "price": "225000", "color": "black"}),
  (4, {"title": "Accoustics", "price": "125000", "color": "white"}),
  (5, {"title": "Earphones", "price": "5000", "color": "white"})
]

analytics = {"title": [], "price": [], "color": []}

print('Initial products list:')
for product in products:
    print(product[0], product[1]["title"])
    for attr in product[1]:
        analytics[attr].append(product[1][attr])

print('')
print('Product analytics:')
print(json.dumps(analytics, indent=2))
