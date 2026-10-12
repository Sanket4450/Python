fruits = ["apple", "banana", "cherry"]

mixed_list = [1, "hello", 3.14, True]

print(fruits)
print(mixed_list)

print(len(fruits))  # Output: 3

print(fruits[0])  # Output: apple
print(fruits[-1])  # Output: cherry
print(fruits[-2])  # Output: banana
print(fruits[1:3])  # Output: ['banana', 'cherry']

birds = ["sparrow", "eagle", "parrot", "dove", "crow"]

birds[1] = "peacock"  # Change the second element
print(birds)  # Output: ['sparrow', 'peacock', 'parrot', 'dove', 'crow']

birds[2:4] = ["owl", "falcon"]  # Change the third and fourth elements
print(birds)  # Output: ['sparrow', 'peacock', 'owl', 'falcon', 'crow']

birds[1:3] = ["hummingbird"]  # Replace the second and third elements with one element
print(birds)  # Output: ['sparrow', 'hummingbird', 'falcon', 'crow']

birds.insert(2, "kingfisher")  # Insert "kingfisher" at index 2
print(birds)  # Output: ['sparrow', 'hummingbird', 'kingfisher', 'falcon', 'crow']

birds.append("woodpecker")  # Add "woodpecker" at the end
print(
    birds
)  # Output: ['sparrow', 'hummingbird', 'kingfisher', 'falcon', 'crow', 'woodpecker']

pet_animals = ["dog", "cat", "hamster"]
wild_animals = ["lion", "tiger", "bear"]

all_animals = pet_animals + wild_animals  # Concatenate the two lists
print(all_animals)  # Output: ['dog', 'cat', 'hamster', 'lion', 'tiger', 'bear']

pet_animals.extend(wild_animals)  # Extend the pet_animals list with wild_animals
print(pet_animals)  # Output: ['dog', 'cat', 'hamster

vegetables = ["carrot", "broccoli", "spinach", "potato", "tomato", "potato"]

vegetables.remove("potato")  # Remove the first occurrence of "potato"
print(vegetables)  # Output: ['carrot', 'broccoli', 'spinach', 'tomato', 'potato']

vegetables.pop(2)  # Remove the element at index 2 (spinach)
print(vegetables)  # Output: ['carrot', 'broccoli', 'tomato', 'potato']

vegetables.pop()  # Remove the last element (potato)
print(vegetables)  # Output: ['carrot', 'broccoli', 'tomato']

for vegetable in vegetables:
    print(vegetable)  # Output: carrot, broccoli, tomato

vegetables.sort()  # Sort the list in ascending order
print(vegetables)  # Output: ['broccoli', 'carrot', 'tomato']

vegetables.sort(reverse=True)  # Sort the list in descending order
print(vegetables)  # Output: ['tomato', 'carrot', 'broccoli']

vegetables.reverse()  # Reverse the order of the list
print(vegetables)  # Output: ['broccoli', 'carrot', 'tomato']

vegetable_ref = vegetables  # Create a reference to the list
vegetable_ref.append("cucumber")  # Add "cucumber" to the list using the reference
print(vegetables)  # Output: ['broccoli', 'carrot', 'tomato', 'cucumber']

vagetables_copy = vegetables.copy()  # Create a copy of the list
print(vagetables_copy)  # Output: ['broccoli', 'carrot', 'tomato', 'cucumber']

print(vegetables.count("carrot"))  # Count the occurrences of "carrot" in the list

print(vegetables.index("tomato"))  # Find the index of "tomato" in the list

vegetables.clear()  # Remove all elements from the list
print(vegetables)  # Output: []

del vegetables  # Delete the list entirely
# print(vegetables)  # This will raise a NameError since the list no longer
