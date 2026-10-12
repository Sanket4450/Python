colors = {"red", "green", "blue"}

print(colors)  # Output: {'red', 'green', 'blue'}
print(len(colors))  # Output: 3

set1 = {"A", "B", True, 1, 2.5}
print(
    set1
)  # True and 1 are considered the same in a set, so only one of them will be stored

set2 = {"B", "C", False, 0, 3.5}
print(
    set2
)  # False and 0 are considered the same in a set, so only one of them will be stored

print("green" in colors)  # Output: True
print("yellow" in colors)  # Output: False
print("yellow" not in colors)  # Output: True

for color in colors:
    print(color)  # Output: red, green, blue (order may vary)

colors.add("pink")  # Add a new color to the set
print(colors)  # Output: {'red', 'green', 'blue', 'pink'}

colors.update(["orange", "purple"])  # Add multiple colors to the set
print(colors)  # Output: {'red', 'green', 'blue', 'pink', 'orange', 'purple'}

colors.remove("blue")  # Remove a color from the set
print(colors)  # Output: {'red', 'green', 'pink', 'orange', 'purple'}

colors.discard(
    "yellow"
)  # Remove a color from the set, but do not raise an error if it doesn't exist
print(colors)  # Output: {'red', 'green', 'pink', 'orange', 'purple'}

extra_colors = colors.union(
    {"cyan", "magenta", "yellow"}
)  # Create a new set with all colors
print(
    extra_colors
)  # Output: {'red', 'green', 'pink', 'orange', 'purple', 'cyan', 'magenta', 'yellow'}
print(colors)  # Output: {'red', 'green', 'pink', 'orange', 'purple'}

print(colors.intersection({"green", "blue", "yellow"}))  # Output: {'green'}

colors.intersection_update(
    {"green", "blue", "yellow"}
)  # Update the set to keep only the intersection
print(colors)  # Output: {'green'}

different_colors = extra_colors.difference(
    {
        "green",
        "yellow",
        "cyan",
    }
)  # Create a new set with the difference
print(different_colors)  # Output: {'red', 'pink', 'orange', 'purple', 'magenta'}

different_colors.difference_update(
    {"red", "pink"}
)  # Update the set to remove the difference
print(different_colors)  # Output: {'orange', 'purple', 'magenta'}

print(
    different_colors.symmetric_difference({"purple", "black", "white"})
)  # Output: {'orange', 'magenta', 'black', 'white'}

different_colors.symmetric_difference_update(
    {"purple", "cyan", "aqua"}
)  # Update the set to keep only the symmetric difference
print(different_colors)  # Output: {'orange', 'magenta', 'cyan', 'aqua'}

colors.clear()  # Remove all colors from the set
print(colors)  # Output: set()

del colors  # Delete the set entirely
# print(colors)  # This will raise a NameError since the set no longer exists

fruits = frozenset(["apple", "banana", "cherry"])  # Create a frozenset
print(fruits)  # Output: frozenset({'apple', 'banana', 'cherry'})
print(type(fruits))  # Output: <class 'frozenset'>
print(len(fruits))  # Output: 3
