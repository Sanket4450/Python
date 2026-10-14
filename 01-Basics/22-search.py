import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

print(x)  # <re.Match object; span=(0, 17), match='The rain in Spain'>
print(x.string)  # The rain in Spain
print(x.span())  # (0, 17)

y = re.search("rain", txt)
print(y)  # <re.Match object; span=(4, 8), match='rain'>
print(y.string)  # The rain in Spain
print(y.span())  # (4, 8)

z = re.search("sun", txt)
print(z)  # None
