a = 'asd fsdf sfdf sdfwed'
c = 0
count = len([i for i in range(len(a.split(' ')))])
print(count)

b = input().split(' ')
c = 0
for i in range(len(b)):
    try:
        if int(b[i]):
            c = int(b[i])
    except ValueError:
        try:
            if b[i] == '+':
                c += int(b[i+1])
                break
            else:
                c -= int(b[i+1])
                break
        except ValueError:
            с = 0
            print('неверный ввод')
            
print(c)