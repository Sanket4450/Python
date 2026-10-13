car1 = {"brand": "Toyota", "model": "Fortuner", "year": 2020}

print(type(car1))  # Output: <class 'dict'>
print(len(car1))  # Output: 3

print(car1["brand"])  # Output: Toyota

keys = car1.keys()
print(keys)  # Output: dict_keys(['brand', 'model', 'year'])

values = car1.values()
print(values)  # Output: dict_values(['Toyota', 'Fortuner', 2020])

car1["color"] = "Black"
car1["model"] = "Innova"

print(keys)  # Output: dict_keys(['brand', 'model', 'year', 'color'])
print(values)  # Output: dict_values(['Toyota', 'Innova', 2020, 'Black'])

items = car1.items()

print(
    items
)  # Output: dict_items([('brand', 'Toyota'), ('model', 'Innova'), ('year', 2020), ('color', 'Black')])

print(type(keys))  # Output: <class 'dict_keys'>
print(type(values))  # Output: <class 'dict_values'>
print(type(items))  # Output: <class 'dict_items'>

print("brand" in car1)  # Output: True
print("price" in car1)  # Output: False

car1.update({"price": 30000, "year": 2021})

print(
    car1
)  # Output: {'brand': 'Toyota', 'model': 'Innova', 'year': 2021, 'color': 'Black', 'price': 30000}

car1.pop(
    "price",
)

print(car1)


for key in car1:
    print(key)

for key in car1:
    print(car1[key])

for key in car1.keys():
    print(key)

for value in car1.values():
    print(value)

for key, value in car1.items():
    print(key, value)

referenced_car = car1
copied_car = car1.copy()

car1.clear()

print(car1)  # Output: {}
print(referenced_car)  # Output: {}
print(
    copied_car
)  # Output: {'brand': 'Toyota', 'model': 'Innova', 'year': 2021, 'color': 'Black'}

del car1

# print(car1)  # Output: NameError: name 'car1' is not defined
