#  Ask enter to enter two numbers (say, a and b). Generate two random numbers
#   between those two numbers and find a combination of these two newly generated
#   random numbers.

import random
from itertools import combinations
a = int(input("enter the first number: "))
b = int(input("enter the second number: "))
randomNumbers = [random.randint(1,10),random.randint(1,10)]
twoVariables = [a,randomNumbers,b]   # generating two random numbers
                                                                # between those numbers
print(randomNumbers)
print(twoVariables)

# no finding the combinations of the two newly generated number

int1 = combinations(randomNumbers,2)

for i in list(int1):
    print(i)



