animals = ("dog", "cat", "hamster", "lion", "tiger", "bear")

print(animals)
print(len(animals))  # Output: 6

single_tuple = ("apple",)  # A single-element tuple requires a trailing comma
print(single_tuple)
print(type(single_tuple))  # Output: <class 'tuple'>

false_tuple = "banana"  # This is not a tuple, it's a string
print(false_tuple)
print(type(false_tuple))  # Output: <class 'str'>

empty_tuple = ()  # An empty tuple
print(empty_tuple)

print(animals[0])  # Output: dog
print(animals[-1])  # Output: bear
print(animals[1:4])  # Output: ('cat', 'hamster', 'lion')

print(animals.index("tiger"))  # Output: 4

print(animals.count("cat"))  # Output: 1

print("lion" in animals)  # Output: True

print(animals + ("elephant", "giraffe"))  # Concatenate tuples

animals_list = list(animals)  # Convert tuple to list
animals_list.append("zebra")  # Add an element to the list
print(
    animals_list
)  # Output: ['dog', 'cat', 'hamster', 'lion', 'tiger', 'bear', 'zebra']

(animal1, animal2, animal3, animal4, animal5, animal6) = (
    animals  # Unpack the tuple into variables, compulsary all variables must be assigned
)

print(animal1)  # Output: dog
print(animal2)  # Output: cat

print((1, 2, 3) + (4, 5, 6))  # Output: (1, 2, 3, 4, 5, 6)

print(
    animals * 3
)  # Output: ('dog', 'cat', 'hamster', 'lion', 'tiger', 'bear', 'dog', 'cat', 'hamster', 'lion', 'tiger', 'bear', 'dog', 'cat', 'hamster', 'lion', 'tiger', 'bear')

for animal in animals:
    print(animal)  # Output: dog, cat, hamster, lion, tiger, bear

del animals  # Delete the tuple entirely
# print(animals)  # This will raise a NameError since the tuple no longer exists
