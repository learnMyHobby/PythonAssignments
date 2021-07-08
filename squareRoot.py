# Write a Python code that inputs input from the user and calculate its square root.


import math
# taking the input from the user in integer

number = int(input('Enter the number you want square root of: '))

squareRoot = math.sqrt(number) # importing the math module to find out the sqrt of the number


print(f'The square root of {number} is ', squareRoot)