import datetime

now = datetime.datetime.now()

print(now)
print(now.year)
print(now.date())

birthday = datetime.datetime(2006, 4, 24)
accurate_birthday = datetime.datetime(2006, 4, 24, 18, 45, 20)

print(birthday)
print(accurate_birthday)

print(accurate_birthday.strftime("%A"))  # Monday
print(accurate_birthday.strftime("%B"))  # April
