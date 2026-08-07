# Use float(input()) to collect two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Calculate and display: addition, subtraction, multiplication 
# Addition
addition = num1+num2
print(f"Addition: {round(addition,2)}")

# Subtraction
subtraction = num1-num2
print(f"Substraction: {round(subtraction,2)}")

# Multiplication
multiplication = num1*num2
print(f"Multiplication: {round(multiplication,2)}")

# Handle the division by zero: division, floor division (//) and modulus (%)
if num2 == 0:
   print("Division: Error! Cannot divide by zero")
   print("Floor division: Error! Cannot divide by zero")
   print("Modulus: Error! Cannot divide by zero")
else:
     division = num1/num2
     floor_division = num1//num2
     modulus = num1%num2
     print(f"Division: {round(division,2)} ")
     print(f"Floor division: {round(floor_division,2)}")
     print(f"Modulus: {round(modulus,2)}")

