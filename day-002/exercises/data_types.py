# string
print("Hello"[4]) # subscripting
print("Hello"[-1]) # prints the same 

# integer 
print(123 + 456)

# float
print(1.18)

# boolean
print(True)
print(False)

# len() can only accept strings
len("12345")

# Datatypes: string, integer, float, boolean
# type() function
print(type("Hello")) # string(str)
print(type(123456)) # integer
print(type("7.890")) # float
print(type(True)) # boolean

# Type Conversion
print("123" + "456") # Concatenation
print(int("123") + int("456")) # Calculation because of Type Conversion

# More Type Conversion functions(func)
float()
str()

# Using Type Conversion on functions
print("Number of letters in your name: " + str(len(input("Enter your name: "))))
