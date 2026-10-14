x = None  # If you want to set absense of data then you can use None. You can't keep empty variable

print(x)  # None
print(type(x))  # <class 'NoneType'>

print(x is None)  # True
print(x == None)  # True
print(x is not None)  # False

print(bool(None))  # False


def my_function():
    print("Hello from a function")


result = my_function()  # Function doesn't return anything so it returns None
print(result)  # None
