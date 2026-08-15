# User personal information
first_name = input("Enter your first name: ")
surname = input("Enter your surname: ")
age = int(input("age: "))
favourite_number = float(input("favourite number: "))

# Displaying a formatted greeting using an f-string
full_name = f"{first_name} {surname}"
print(f"\nWelcome, {full_name}!")

# Display the name in UPPERCASE using .upper() and in Title Case using .title()
print(f"{full_name.upper()}")
print(f"{full_name.title()}")

# Calculate and display the age in months (age × 12)
age_in_months = age * 12
print(age_in_months)

# Round the favourite number to 2 decimal places using round()
rounded_number = round(favourite_number, 2)
print(f"Favourite number: {rounded_number}")

# Print the data type of each collected value using type()
print(f"\nData type()")
print(type(first_name))
print(type(surname))
print(type(age))
print(type(favourite_number))

