# range() func with for loop

for numbers in range(0, 11): # a <= range(a, b) < b
    print(numbers) # -> 0,1,2,3,4,5,6,7,8,9,10

for numbers in range(0, 11, 2):
    print(numbers) # -> 0,2,4,6,8,10

gaussian_sum = 0
for gaus in range(1, 101):
    gaussian_sum += gaus
print(gaussian_sum)

