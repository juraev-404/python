import copy
pole = [['•' for i in range(8)] for el in range(8)]
fl = 8
flag_1 = 0
dc = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
pole[5][5] = 'Q'
pole[2][3] = 'Q'

print('  A B C D E F G H')
for i in pole:
    print(fl-flag_1, ' '.join(i), fl-flag_1)
    flag_1 += 1
print('  A B C D E F G H')
pole_2 = copy.deepcopy(pole)

while True:
    def Q(x, y):
        x = [i for i in x]
        y = [i for i in y]
        x[1], y[1] = int(x[1]), int(y[1])
        if pole[0-x[1]][dc[x[0]]] == '•':
            print('нет фигури')
            k = input().split()
            Q(k[0], k[1])
        flag = 0
        for i in range(9):
            if i-x[1] == 0-y[1] and dc[x[0]]+i == dc[y[0]]:
                break
            elif -i-x[1] == 0-y[1] and dc[x[0]]-i == dc[y[0]]:
                break
            elif -i-x[1] == 0-y[1] and dc[x[0]]+i == dc[y[0]]:
                break
            elif i-x[1] == 0-y[1] and dc[x[0]]-i == dc[y[0]]:
                break
            flag += 1
        if flag != 9:
            pole[0-x[1]][dc[x[0]]], pole[0-y[1]][dc[y[0]]] = '•', pole[0-x[1]][dc[x[0]]]
        else:
            if x[1] != y[1] and x[0] != y[0]:
                raise ValueError('ход невозможен')
            else:
                pass
            pole[0-x[1]][dc[x[0]]], pole[0-y[1]][dc[y[0]]] = '•', pole[0-x[1]][dc[x[0]]]
        

            

    k = input().split()
    x = [i for i in k[0]]
    y = [i for i in k[1]]
    x[1], y[1] = int(x[1]), int(y[1])
    if y[1]>8:
        print('вне поля')
        k = input().split()
        Q(k[0], k[1])
    else:
        Q(k[0], k[1])


    flag_1 = 0
    print('  A B C D E F G H')
    for i in pole:
        print(fl-flag_1, ' '.join(i), fl-flag_1)
        flag_1 += 1
    print('  A B C D E F G H')
    pole_2 = copy.deepcopy(pole)