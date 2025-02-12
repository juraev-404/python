a = input()
b = input()
c = input()
a1 = [float(x) for x in a.split(', ')]
b1 = [float(x) for x in b.split(', ')]
c1 = [float(x) for x in c.split(', ')]
l1 = ((b1[0]-a1[0])**2+(b1[1]-a1[1])**2)**0.5
l2 = ((c1[0]-a1[0])**2+(c1[1]-a1[1])**2)**0.5
l3 = ((c1[0]-b1[0])**2+(c1[1]-b1[1])**2)**0.5
p = l1 + l2 + l3
s = abs(a1[0]*(b1[1]-c1[1])+b1[0]*(c1[1]-a1[1])+c1[0]*(a1[1]-b1[1]))/2
print(p, s)