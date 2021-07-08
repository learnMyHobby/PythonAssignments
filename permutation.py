#  Write a Python code to calculate Permutation (5,3)

import itertools

a = [5,3]

permut = itertools.permutations(a)

for i in list(permut):
    print(i)




