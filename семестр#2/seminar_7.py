li = ['Red', 'Blue', 'Black', 'White', 'Pink']
li_2 = map(lambda x: list(x), li)
print(list(li_2))

from functools import reduce

li_n = [1,2,5,4,6,8,9]
val = 5
li_n2 = list(filter(lambda x: x > val, li_n))[::-1]
li_n3 = reduce(lambda x, y: x*y, li_n2)

print(li_n2, li_n3, sep='\n')