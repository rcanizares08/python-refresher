user_age = input("Enter your age: ")
age_number = int(user_age)

months = age_number * 12
print(f"{age_number} is equal to {months} months.")


# The other form, @roxana canizares
user_age = int(input("Enter your age: "))
months = user_age * 12
days = months * 30
hours = days * 24
minute = hours * 60
print(f"{user_age} is equal to {months} months and {days} days and {hours} hours and {minute} minutes")
