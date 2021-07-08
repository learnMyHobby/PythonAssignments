# write the program to convert 108 to binary

import math

# declaring the variable and passin the decimal to the corresponding variable

dec_number = 108

#converting to the binary number using bin()
bin_number = bin(dec_number)
print(bin_number)

# converting back to the decimal number
print(int(bin_number,2))