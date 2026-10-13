age = 20

if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are not an adult.")

print("You are an adult.") if age >= 18 else print(
    "You are a teenager."
) if age >= 13 else print("You are not an adult.")

username = "Emil"
password = "python123"
is_active = True

if username:
    if password:
        if is_active:
            print("Login successful")
        else:
            print("Account is not active")
    else:
        print("Password required")
else:
    print("Username required")
