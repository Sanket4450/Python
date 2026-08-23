x = 15
y = 4

# Arithmetic Operators

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y) # 15 to the power of 4
print(x // y) # 15 divided by 4 (integer division)

# Ternary Operator

a = 'Pass' if x > y else 'Fail'
print(a) # prints 'Pass' because x is greater than y

num = 6

b = 'Fri' if num == 5 else 'Sat' if num == 6 else 'Sun'
print(b) # prints 'Sat' because num is equal to 6

# Comparison Operators

print(x == y) # prints False because x is not equal to y
print(x != y) # prints True because x is not equal to y
print(x > y) # prints True because x is greater than y
print(x < y) # prints False because x is not less than y
print(x >= y) # prints True because x is greater than or equal to y
print(x <= y) # prints False because x is not less than or equal to y

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(list1 is list2) # prints False because list1 and list2 are different objects in memory
print(list1 == list2) # prints True because list1 and list2 have the same elements
print(list1 is list3) # prints True because list3 is a reference to list1

# Logical Operators

print(x > 10 and y < 5) # prints True because both conditions are True
print(x > 10 or y < 5) # prints True because at least one condition is True
print(not(x > 10 and y < 5)) # prints False because the condition is True and not operator negates it

list1 = ['apple', 'banana', 'cherry']

print('banana' in list1) # prints True because 'banana' is in list1
print('grape' not in list1) # prints True because 'grape' is not in list1

print('b' in 'banana') # prints True because 'b' is in 'banana'