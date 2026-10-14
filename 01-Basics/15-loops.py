i = 0

while i < 5:
    print(i)
    i += 1

while True:
    print(i)

    if i >= 10:
        break
    i += 1

print()

j = 0

while j < 5:
    j += 1
    if j == 3:
        continue
    print(j)

fruit = "Pineapple"
fruits = ["Apple", "Banana", "Cherry"]
birds = ("Parrot", "Sparrow", "Eagle")
colors = {"red", "green", "blue"}
car = {"brand": "Toyota", "model": "Corolla", "year": 2020}

for letter in fruit:
    print(letter)

for fruit in fruits:
    print(fruit)

for bird in birds:
    print(bird)

for color in colors:
    print(color)

for key, value in car.items():
    print(f"{key}: {value}")
