# from math import permuttions
from more_itertools import distinct_permutations
from itertools import permutations, combinations_with_replacement, combinations
import scipy



# omega = 'aabb'

# z = sorted(distinct_permutations(omega))
# print(z)

# a = 6/23 +5/22+4/21+3/20+2/19+1/18
# print(a)

A = 0
B = 0
import random

for i in range(100000):
    c = random.randint(1,2)
    if c == 1:
        A+=1
    else:
        B+=1
print(A/100000)
print(B/100000)
