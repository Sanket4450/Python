a = 'Hello from the other side!'

print(len(a)) # prints the length of the variable a

print('other' in a) # checks if the substring 'other' is present in the variable a and prints True or False

print(a[0]) # prints the first character of the variable a

print(a[0:5]) # prints the substring from index 0 to 4 of the variable a
print(a[6:]) # prints the substring from index 6 to the end of the variable a
print(a[:5]) # prints the substring from the start to index 4 of the variable a
print(a[-5:]) # prints the last 5 characters of the variable a
print(a[::-1]) # prints the variable a in reverse order

print(a.upper()) # prints the variable a in uppercase
print(a.lower()) # prints the variable a in lowercase

print("abcd".capitalize()) # capitalizes the first character of the variable a and prints the result

print(a.strip())

print(a.replace('other', 'this')) # replaces the substring 'other' with 'this' in the variable a and prints the result

print(a.split(' ')) # splits the variable a into a list of substrings using space as the delimiter and prints the result

print(a + ' How are you?') # concatenates the variable a with another string and prints the result

b = 18

print(f"My age is {b} years old.") # uses an f-string to print the value of variable b within a string
print("My age is {} years old.".format(b)) # uses the format method to print the value of variable b within a string

print("My name is \"Sanket\"")
print('I am learning Python\'s string manipulation techniques.')

print(a.count('o')) # counts the number of occurrences of the substring 'o' in the variable a and prints the result

print(a.find('other')) # finds the index of the first occurrence of the substring 'other' in the variable a and prints the result
print(a.index('other')) # finds the index of the first occurrence of the substring 'other' in the variable a and prints the result

print(a.startswith('Hello')) # checks if the variable a starts with the substring 'Hello' and prints True or False
print(a.endswith('side!')) # checks if the variable a ends with the substring 'side
