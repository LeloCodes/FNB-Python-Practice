# The Challenge: “The South African Fuel Cost Calculator”

# The kilometres the user wants to drive
kilometres = int(input("Enter the kilometres: "))

# The current petrol price per liter
price_per_litre = float(input(" Enter the petrol price per litre: "))

# Their car uses exactly 1 liter of fuel for every 10 kilometers driven
liters_needed = kilometres / 10
print("Liters needed:", liters_needed)

# The total cost
total_cost = liters_needed * price_per_litre
print("Total_cost:", total_cost)

# Formating the final cost to 2 decimal places.
rounded_total_cost = round(total_cost, 2)
print(rounded_total_cost)

