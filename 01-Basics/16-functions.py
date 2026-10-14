def print_hello():
    print("Hello, World!")


print_hello()
print_hello()
print_hello()

result = print_hello()  # returns None
print(f"The result of print_hello() is: {result}")


def sum_numbers(a, b):
    return a + b


sum_result = sum_numbers(5, 10)
print(f"The sum of 5 and 10 is: {sum_result}")


def print_name(name="John Doe"):
    print(f"Hello, {name}!")


print_name("Alice")
print_name()  # Uses the default value


def print_car_info(brand, model, year):
    print(f"Car Brand: {brand}, Model: {model}, Year: {year}")


print_car_info(
    year=2020, brand="Toyota", model="Corolla"
)  # Using keyword arguments, order doesn't matter


def print_full_name(first_name, last_name, /):
    print(f"Full Name: {first_name} {last_name}")


print_full_name("John", "Doe")  # Positional-only arguments


def print_person_info(*, name, age):
    print(f"Name: {name}, Age: {age}")


print_person_info(name="Alice", age=30)  # Keyword-only arguments


def print_subjects(*subjects):  # receives in a tuple
    print("Subjects:", ", ".join(subjects))


print_subjects("Math", "Science", "History")  # Unlimited positional arguments


def print_student_info(**info):  # receives in a dictionary
    for key, value in info.items():
        print(f"{key}: {value}")


print_student_info(name="Alice", age=20, grade="A")  # Unlimited keyword arguments


def my_function(title, *args, **kwargs):
    print("Title:", title)
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)


my_function("User Info", "Emil", "Tobias", age=25, city="Oslo")


def sum(
    a,
    b,
    c,
):
    return a + b + c


inputs = (1, 2, 3)
inputs2 = (4, 5, 6)
inputs3 = {7, 8, 9}

print(sum(*inputs))  # Unpacking a list
print(sum(*inputs2))  # Unpacking a tuple
print(sum(*inputs3))  # Unpacking a set


def print_car_info(brand, model, year):
    print(f"Car Brand: {brand}, Model: {model}, Year: {year}")


car_info = {"brand": "Toyota", "model": "Corolla", "year": 2020}
print_car_info(**car_info)  # Unpacking a dictionary

x = 10


def my_func():
    global x  # Declare x as global to modify the global variable
    x += 2  # This will modify the global x
    print(x)


my_func()  # increments x to 12
my_func()  # increments x to 14
my_func()  # increments x to 16
print(
    x
)  # This will print 12, as the x inside my_func is global and affects the global x


def function1():
    x = 5  # Local variable
    print(f"Inside function1, x = {x}")

    def function2():
        nonlocal x  # Declare x as nonlocal to modify the variable from the enclosing scope
        x += 3  # This will modify the x in function1
        print(f"Inside function2, x = {x}")

    function2()  # increments x to 8
    function2()  # increments x to 11
    function2()  # increments x to 14
    print(f"After function2, inside function1, x = {x}")


function1()
