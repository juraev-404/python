# 1

li = [1,2,3,4,5,6,7,8,9]
li1=[]
li2=[]
[(lambda i: li1.append(i) if int(i)%2==0 else li2.append(i))(x) for x in li]
print('#1: ', li1, li2, sep='\n')

# 2

li_2 =  ['orange', 'red', 'green', 'blue', 'white', 'black']
li_3 =  ['orange', 'black'] 
li_2 = list(filter(lambda i: i not in li_3, li_2))
print('#2: ', li_2)

# 3

li_4 =  [64, 76, 31, 45, 48, 98, 61, 55, 13, 25, 76,]
ras = lambda i: 'отсортирован' if sorted(i) == li_4 else 'неотсортирован'
print('#3 до сортировки: ', ras(li_4))

li_4.sort()
print('#3 после сортировки: ', ras(li_4))