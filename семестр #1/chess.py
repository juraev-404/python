import copy
a = ' '
b = '■'
fr = ['♙', '♘', '♗', '♖', '♕', '♔', '♚', '♛', '♜', '♝', '♞', '♟']
dc = {'A':  0, 'B':  1, 'C':  2, 'D':  3, 'E':  4, 'F':  5, 'G':  6, 'H':  7}

pole = []
for el in range(8):
    l2 = []
    for i in range(1, 9):
        a, b = b, a
        l2.append(a)
    a, b = b, a
    pole.append(l2)
pole_2 = copy.deepcopy(pole)
print(pole_2)

pole[1]= [fr[0] for i in range(8)]
pole[6]= [fr[-1] for i in range(8)]
pole[0][0] = fr[3]
pole[0][7] = fr[3]
pole[0][1] = fr[2]
pole[0][2] = fr[1]
pole[0][6] = fr[2]
pole[0][5] = fr[1]
pole[0][3] = fr[4]
pole[0][4] = fr[5]

pole[7][0] = fr[-4]
pole[7][7] = fr[-4]
pole[7][1] = fr[-3]
pole[7][2] = fr[-3]
pole[7][6] = fr[-2]
pole[7][5] = fr[-3]
pole[7][3] = fr[-5]
pole[7][4] = fr[-6]



f = 9
print('  A B C D E F G H')
for i in pole:
    # i[0] = f
    i = [str(el) for el in i]
    f -= 1
    print(f, ' '.join(i), f)
print('  A B C D E F G H')



while True:
    o = input().split(' ')
    x, y = o[1], o[2]
    x = [i for i in x]
    y = [i for i in y]
    x[1] = int(x[1])
    y[1] = int(y[1])
    print(x[1], y[1])
    coordinate_1 = pole[0-x[1]][dc[x[0]]]
    coordinate_2 = pole[0-y[1]][dc[y[0]]]
    


    def King():
        fw = fr[6]
        fb = fr[5]
        if abs(x[1]-y[1]) == 1 or abs(dc[x[0]] - dc[y[0]]) == 1:
            pole[0-y[1]][dc[y[0]]], pole[0-x[1]][dc[x[0]]] = pole[0-x[1]][dc[x[0]]], pole_2[0-x[1]][dc[x[0]]]
        else:
            raise ValueError('ход невозможен')


    def Bishop():
        fw = fr[7]
        fb = fr[4]
        for i in range(9):
            i += 1
            if i-x[1] == 0-y[1] and dc[x[0]]+i== dc[y[0]]:
                break
            elif -i-x[1] == 0-y[1] and dc[x[0]]-i== dc[y[0]]:
                break
            elif -i-x[1] == 0-y[1] and dc[x[0]]+i== dc[y[0]]:
                break
            elif i-x[1] == 0-y[1] and dc[x[0]]-i== dc[y[0]]:
                break
        if i != 9:
            pole[0-y[1]][dc[y[0]]], pole[0-x[1]][dc[x[0]]] = pole[0-x[1]][dc[x[0]]], pole_2[0-x[1]][dc[x[0]]]
        else:
            raise ValueError('ход невозможен')
        

    def Queen():
        fw = fr[2]
        fb = fr[9]

        for i in range(9):
            i += 1
            if i-x[1] == 0-y[1] and dc[x[0]]+i== dc[y[0]]:
                break
            elif -i-x[1] == 0-y[1] and dc[x[0]]-i== dc[y[0]]:
                break
            elif -i-x[1] == 0-y[1] and dc[x[0]]+i== dc[y[0]]:
                break
            elif i-x[1] == 0-y[1] and dc[x[0]]-i== dc[y[0]]:
                break
        if i != 9:
            pole[0-y[1]][dc[y[0]]], pole[0-x[1]][dc[x[0]]] = pole[0-x[1]][dc[x[0]]], pole_2[0-x[1]][dc[x[0]]]
        else:        
            if x[1] != y[1] and x[0] != y[0]:
                raise ValueError('ход невозможен')
            else:
                pass
            pole[0-y[1]][dc[y[0]]], pole[0-x[1]][dc[x[0]]] = pole[0-x[1]][dc[x[0]]], pole_2[0-x[1]][dc[x[0]]]


    def Knight():
        fw = fr[-2]
        fb = fr[1]
        if abs(x[1]-y[1]) == 2 and abs(dc[x[0]] - dc[y[0]]) == 1:
            pole[0-y[1]][dc[y[0]]], pole[0-x[1]][dc[x[0]]] = pole[0-x[1]][dc[x[0]]], pole_2[0-x[1]][dc[x[0]]]
        elif abs(x[1]-y[1]) == 1 and abs(dc[x[0]] - dc[y[0]]) == 2:
            pole[0-y[1]][dc[y[0]]], pole[0-x[1]][dc[x[0]]] = pole[0-x[1]][dc[x[0]]], pole_2[0-x[1]][dc[x[0]]]
        else:
            raise ValueError('ход невозможен')


    def Rook():
        if x[1] != y[1] and x[0] != y[0]:
            raise ValueError('ход невозможен')
        else:
            pass
        pole[0-y[1]][dc[y[0]]], pole[0-x[1]][dc[x[0]]] = pole[0-x[1]][dc[x[0]]], pole_2[0-x[1]][dc[x[0]]]





    def Pawn():
        coordinate_1 = pole[0-x[1]][dc[x[0]]]
        coordinate_2 = pole[0-y[1]][dc[y[0]]]
        fw = fr[-1]
        fb = fr[0]
        if coordinate_1 == fw:
            if x[1] == 2:
                if x[1]+2 != y[1] and x[1]+1 != y[1]:
                    raise ValueError('ход невозможен') 
                elif coordinate_2 == a and x[1]+1 == y[1] and x[0] != y[0]:
                    raise ValueError('ход невозможен')  
                elif coordinate_2 == b and x[1]+1 == y[1] and x[0] != y[0]:
                    raise ValueError('ход невозможен') 
                else:
                    pass
            else:
                if x[1]+1 != y[1] :
                    raise ValueError('ход невозможен') 
                elif coordinate_2 == a and x[1]+1 == y[1] and x[0] != y[0]:
                    raise ValueError('ход невозможен') 
                elif coordinate_2 == b and x[1]+1 == y[1] and x[0] != y[0]:
                    raise ValueError('ход невозможен') 
                else:
                    pass
        else:
            if x[1] == 7:
                if x[1]-2 != y[1] and x[1]-1 != y[1]:
                    raise ValueError('ход невозможен') 
                elif coordinate_2 == a and x[1]-1 == y[1] and x[0] != y[0]:
                    raise ValueError('ход невозможен')  
                elif coordinate_2 == b and x[1]-1 == y[1] and x[0] != y[0]:
                    raise ValueError('ход невозможен') 
                else:
                    pass
            else:
                if x[1]-1 != y[1] :
                    raise ValueError('ход невозможен') 
                elif coordinate_2 == a and x[1]-1 == y[1] and x[0] != y[0]:
                    raise ValueError('ход невозможен') 
                elif coordinate_2 == b and x[1]-1 == y[1] and x[0] != y[0]:
                    raise ValueError('ход невозможен') 
                else:
                    pass
        pole[0-y[1]][dc[y[0]]], pole[0-x[1]][dc[x[0]]] = pole[0-x[1]][dc[x[0]]], pole_2[0-x[1]][dc[x[0]]]
        
    if o[0]=='K':
        King()

    if o[0]=='Q':
        Queen()

    if o[0]=='B':
        Bishop()

    if o[0]=='R':
        Rook()

    if o[0]=='Kn':
        Knight()

    if o[0]=='p':
        Pawn()


    f = 9
    print('  A B C D E F G H')
    for i in pole:
        # i[0] = f
        i = [str(el) for el in i]
        f -= 1
        print(f, ' '.join(i), f)
    print('  A B C D E F G H')