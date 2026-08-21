print(10 > 5) # prints True because 10 is greater than 5
print(10 < 5) # prints False because 10 is not less than 5
print(10 == 10) # prints True because 10 is equal to 10
print(10 != 5) # prints True because 10 is not equal to 5
print(10 >= 5) # prints True because 10 is greater than or equal to 5
print(10 <= 5) # prints False because 10 is not less than or equal to 5

print(bool(True)) # prints True because True is considered as True
print(bool(False)) # prints False because False is considered as False
print(bool(1)) # prints True because 1 is considered as True
print(bool(0)) # prints False because 0 is considered as False
print(bool("")) # prints False because an empty string is considered as False
print(bool("Hello")) # prints True because a non-empty string is considered as True
print(bool(None)) # prints False because None is considered as False
print(bool([])) # prints False because an empty list is considered as False
print(bool([1, 2, 3])) # prints True because a non-empty list is considered as True
print(bool(())) # prints False because an empty tuple is considered as False
print(bool((1, 2, 3))) # prints True because a non-empty tuple is considered as True
print(bool({})) # prints False because an empty dictionary is considered as False
print(bool({"key": "value"})) # prints True because a non-empty dictionary is considered as True
print(bool(set())) # prints False because an empty set is considered as False
print(bool({1, 2, 3})) # prints True because a non-empty set is considered as True

print(isinstance(10, int)) # prints True because 10 is an instance of int
print(isinstance(10.5, float)) # prints True because 10.5 is an instance of float
print(isinstance("Hello", str)) # prints True because "Hello" is an instance of str
print(isinstance([1, 2, 3], list)) # prints True because [1, 2, 3] is an instance of list
print(isinstance((1, 2, 3), tuple)) # prints True because (1, 2, 3) is an instance of tuple
print(isinstance({"key": "value"}, dict)) # prints True because {"key": "value"} is an instance of dict
print(isinstance({1, 2, 3}, set)) # prints True because {1, 2, 3} is an instance of set