def my_function(arg):
    return len(arg)


try:
    my_function(5)
except NameError:
    print("NameError occurred")
except TypeError as e:
    print("TypeError occurred:", e)

try:
    my_function("ABCD")
except Exception as e:
    print("An exception occurred:", e)
else:
    print("No exception occurred")  # else runs if no exception occurs in the try block
finally:
    print(
        "Finally block executed"
    )  # finally runs regardless of whether an exception occurred or not

try:
    raise NameError("This is a custom exception")
except NameError as e:
    print("Caught an exception:", e)
