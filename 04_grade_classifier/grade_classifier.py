# Collect learner name and marks for three subjects (as floats) using input()
learner_name = input("Enter learner name: ")
subject1 = float(input("Enter your subject1 marks: "))
subject2 = float(input("Enter your subject2 marks: "))
subject3 = float(input("Enter your subject3 marks: "))

# Calculate the average mark across the three subjects
average = (subject1 + subject2 + subject3)/3
print(f"Average: {average}")

# Assign a letter grade: A (80+), B (70-79), C (60-69), D (50-59), F (below 50) using if/elif/else
if average >=80:
    Grade = "A"
elif average >=70:
    Grade = "B"
elif average >=60:
    Grade = "C"
elif average >=50:
    Grade = "D"
else:
    Grade = "F"

# Assign Pass status if the average is 50 or above, Fail otherwise
if average >=50:
    status = "Pass"
else:
    status = "Fail"

# Formatted report card
print(f"\n----- REPORT CARD -----")
print(f"Learner Name: {learner_name}")
print(f"Subject 1: {subject1}")
print(f"Subject 2: {subject2}")
print(f"Subject 3: {subject3}")
print(f"Average Mark: {average:.2f}")
print(f"Grade: {Grade}")
print(f"Status: {status}")

# Flag any individual subject mark below 40 as ‘needs intervention’
if subject1 <40:
    print(f"Subject1: needs intervention")

if subject2 <40:
    print(f"Subject2: needs intervention")

if subject3 <40:
    print(f"Subject3: needs intervention")