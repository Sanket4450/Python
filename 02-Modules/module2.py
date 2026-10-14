import platform  # Built-in module

import module1
import module3 as m3  # Import module3 with an alias
from module3 import divide, subtract  # Import specific functions from module3

print(module1.car1)  # Use this syntax to access the car1 dictionary from module1.py

print(module1.sum(10, 20))  # Use this syntax to call the function from module1.py

print(m3.multiply(5, 6))  # Use this syntax to call the function from module3.py

print(
    platform.system()
)  # Use this syntax to call the function from the built-in module

print(
    dir(module1)
)  # Use this syntax to get the list of attributes and methods of module1
print(
    dir(platform)
)  # Use this syntax to get the list of attributes and methods of the built-in module

print(divide(10, 2))  # Use this syntax to call the divide function from module3.py
print(subtract(10, 5))  # Use this syntax to call the subtract function
