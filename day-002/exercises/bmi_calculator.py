height = 1.65 
weight = 84

# Write your code here.
# Calculate the bmi using weight and height.
bmi = (weight / (height ** 2))

print(bmi) # prints 30.85399449035813
print(round(bmi)) # rounding prints 31
print(round(bmi, 2)) # prints 30.85

print(f"your BMI ist: {bmi}") # f-String