# # a = {(2,4):'a', (2,3):'c'}
# # b = {}
# # for item, value in a:
# #     count = 0
# #     fl = 0
# #     for i in item:
# #         count += i
# #         fl += 1
# #     sr = count/fl
# #     b.update({sr: value})
# # print(b)

# def psort(**args):

#     li = dict(sorted(args.items())).values()

#     print(li)

# psort(c=21, a=22, ac=17, b=16)

# li = [['E', 'e', 'n', 'y'], ['m', 'e', 'e', 'n', 'y'], ['m', 'i', 'n', 'e', 'y'], ['m', 'o', 'e']]

# a = ','.join([''.join(i) for i in li])

# print(a)

# import string

# import paket_2.p
# import paket_2.v

# def nam_par(*args, name=string.ascii_lowercase):

#     print(dict([(i, b) for i, b in zip(name, args)]))

# nam_par(7, 3, 1, 8, 10, 13, name='xyzafg')

# import paket_2
# print(paket_2.v.v(10, 20, 30))

# import datetime
# li = [int(i) for i in input('гггг мм дд').split(' ')]
# date = datetime.datetime(li[0], li[1], li[2])
# print(date.weekday())



with open('file.txt', 'w') as fi:
	fi.write('2 2')
num = []
with open('file.txt', 'r') as f:
	a = f.readlines()
	for i in a[0].split(' '):
		num.append(int(i))
with open('res.txt', 'w') as fl:
	fl.write(str(sum(num)))
with open('res.txt', 'r') as fl2:
	b = fl2.readlines()
	print(b)
	co






S = input()
J = input()
res = 0
s = ''
for i in S:
	if i in s:
		print(i)
		continue
	else:
		for el in J:
			if el == i:
				res+=1
			else:
				pass
	s = s + i
	    
print(res, s)