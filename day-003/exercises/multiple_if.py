
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

# elif:
# if conditionA:
#   ...code if conditionA is true
# elif conditionB:
#   ...code if conditionA is false and conditionB is true
# 1 or multiple elif statements
# Condition 2 is only checked if condition 1 is false
# else:
#   ...code if conditions are false

# Nested if statements:
# if conditionA:
#   ...code if conditionA is true
#   if conditionB:
#       ...code if conditionA and conditionB are true
#       if conditionC:
#           ...code if conditionA, conditionB and conditionC are true



if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child ticket $5.")
    elif age <= 18:
        bill = 7
        print("Youth ticket $7.")
    else:
        bill = 12
        print("adult pay $12.")
    wants_photo = input("Do you want to have a photo take? y = yes or n = no: ")
    if wants_photo == "y":
        bill += 3
    print(f"Your bill is {bill}")


else:
    print("Sorry you have to grow taller before you can ride.")
