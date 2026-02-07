import numpy as np
from itertools import combinations

# a)

N = int(input())
arr = [np.random.randint(100) for i in range(N)]
min_pair = min(((a, b) for a, b in combinations(arr, 2)), key=lambda pair: abs(pair[0] - pair[1]))

print(min_pair)

# b)

M, N = input().split(' ')
M, N = int(M), int(N)
arr_2 = np.random.randint(100, size=(M, N))


count = sum([list(np.sort(arr_2[0])) == list(np.sort(i)) for i in arr_2[1:]])

print(arr_2, count)