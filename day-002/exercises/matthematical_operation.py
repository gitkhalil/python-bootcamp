print("My age: " + str(12))
print(123 + 456) # plus
print(456 - 123) # minus
print(123 * 456) # multiply
print(123 / 456) # devide return value is float
print(123 // 456) # devide return value is int
print(2 ** 3) # to the power

# PEMDAS
# Parentheses, Exponents, Multiplication/Division, Addition/Subtraction
# ()
# **
# * OR /
# + OR -

print(3 * 3 + 3 / 3 - 3) #result 7.0

# Change the code so it outputs 3.0
print(3 * (3 + 3) / 3 - 3) #result 3.0
print(3 * ((3 + (3 / 3))- 3)) #result 3.0

bmi = 84 / 1.65 ** 2
print(bmi) #30.85399449035813

# Flooring a Number
print(int(bmi)) #30

# Rounding a Number
print(round(bmi)) #31
print(round(bmi, 2)) #30.85

# Assignment Operators
score = 0
print(score)
score += 50
print(score)
score -= 20
print(score)
score *= 10
print(score)
score /= 5
print(score)

# f-String
print(f"Your score is: {score}") #output: Your score is: 60.0
