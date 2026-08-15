# The Secure Password Hint Tool

# The users secret password
password = input("Enter your password: ")

# Use .strip() to clean up any accidental spaces
password = password.strip()

# Grab the very first letter and the very last letter
first_letter = password[0]
last_letter = password[-1]

# Print a hint using an f-string
print(f"Your password hint: It starts with {first_letter.upper()} and ends with {last_letter.upper()}") 