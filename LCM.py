#  Write a Python code to calculate LCM of (25,55)

# giving the input to the two numbers

num1 = 25
num2 = 55

if(num1 > num2):
    maximum = num1
else:
    maximum = num2
while(True):
    if(maximum % num1 == 0) and (maximum % num2 == 0):
        print(maximum)
        break
    maximum+= 1

