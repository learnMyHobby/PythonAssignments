# Write a program to calculate direction and magnitude of the vector described by the following points.
# A = (20,30)
# B = (30,40)

import math
import numpy

# importing required libraries
import numpy
import math


# function definition to compute magnitude o f the vector
def magnitude(vector):
    return math.sqrt(sum(pow(element, 2) for element in vector))


# computing and displaying the magnitude of the vector
print('Magnitude of the Vector:', magnitude(numpy.array([30,40])))



# finding the direction of the vector

# have to subract from terminal point with initial point

x1 = 20
x2 = 30

y1 = 30
y2 = 40

res1 = math.sqrt(pow(y1-x1),2 )
print(res1)


