# User personal information
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
bio = input("Enter your message bio: ")

# Create a username by combining first initial + last name in lowercase
username = f"{first_name[0].lower()}{last_name.lower()}" 

# Display the full name in Title Case using .title()
full_name = f"{first_name.title()} {last_name.title()}" 
print(full_name)

# Strip leading/trailing whitespace from the bio before displaying it using .strip()
bio = bio.strip()

# Count and display the number of characters in the bio using len()
print(f"Number of characters: {len(bio)}")

# Replace any occurrence of ‘I am’ in the bio with ‘I’m’ using .replace(bio = message_bio.replace("I am", "I'm")
bio = bio.replace("I am", "I'm")

# Display all output using f-strings
print(f"First name: {first_name}")  
print(f"Last name: {last_name}")
print(f"Message bio: {bio}")     
print(f"Username: {username}")