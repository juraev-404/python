import numpy as np
np.random.seed(42)
arr = np.random.rand(4, 7)*20
print(arr)

x = (arr - np.min(arr))/ (np.max(arr)-np.min(arr))
print(x)

D = np.random.randint(0, 11, (8, 9))
print(np.sum(D, axis = 0))

print(np.sum(D, axis = 1))

print(np.max(np.sum(D, axis = 1)))

print(np.argmax(np.sum(D, axis = 1)))
