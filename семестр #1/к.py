dc = {'один': 1, 'два': 2, 'три': 3, 'четыре': 4, 'пять': 5, 'шесть': 6,'семь': 7, 'восемь': 8, 'девять': 9, 'десять': 10, 'одиннадцать': 11, 
      'двенадцать': 12, 'тринадцать': 13, 'четырнадцать': 14, 'пятнадцать': 15, 'шестнадцать': 16, 'семнадцать': 17, 'восемнадцать': 18,
      'девятнадцать': 19, 'двадцать': 20, 'тридцать': 30, 'сорок': 40, 'пятьдесят': 50, 'шестьдесят': 60, 'семьдесят': 70, 'восемьдесят': 80,
      'девяносто': 90, 'сто': 100, 'двести': 200, 'триста': 300, 'четыреста': 400, 'пятсоть': 500, 'шестьсот': 600, 'семьсот': 700, 'восемьсот': 800, 
      'девятьсот': 900, 'тысяча': 1000, 'две тысячи': 2000, 'три тысячи': 3000, 'четыре тысячи': 4000, 'пять тысяч': 5000, 'шесть тысяч': 6000, 
      'семь тысяч': 7000, 'восемь тысяч': 8000, 'девять тысяч': 9000}
li = input().split(' ')
for el in li:
    if el == 'на':
        li.remove('на')
li1 = [] 
def calc():
    ras = 0
    if li[0] == 'минус':       
        d = 'минус'
    else:
        d = 'плюс'
    um = 0
    count = 0
    z = 0
    for i in li:
        if i != 'минус' and i != 'плюс' and i != 'умножить':
            if z == 2:
                z = 0
                if d == 'минус':
                    ras -= -dc[i]
                if d == 'плюс':
                    ras += -dc[i]
                if d == 'умножить' and count != 2:
                    um += dc[i]
                    if count == 0:
                        um1 = um
                    count += 1
                    ras = ras*um
                    if count == 2:
                        ras/=um1
                        count = 0
            elif z == 3:
                z = 0
                um += -dc[i]
                if count == 0:
                    um1 = um
                count += 1
                ras = ras*um
                if count == 2:
                    ras/=um1
                    count = 0
                # print('asdf')
            else:
                z = 0
                if d == 'минус':
                    ras -= dc[i]
                if d == 'плюс':
                    ras += dc[i]
                if d == 'умножить' and count != 2:
                    um += dc[i]
                    if count == 0:
                        um1 = um
                    count += 1
                    ras = ras*um
                    if count == 2:
                        ras/=um1
                        count = 0
        else:
            d = i
            z += 1
            if d == 'умножить':
                z += 1
    st = str(int(ras))
    sti = abs(int(st))
    li2 = []
    ras = ''
    for i in st:
        if i == '-':
            ras += 'минус '
        else:
            li2.append(i)
    a = len(li2)-1
    # print(li2)
    for i in li2:
        for k, v in dc.items():
            if sti < 20 and sti > 11:
                if v == abs(sti):
                    ras += k + ' '
            else:
                if int(i) == 0:
                    a -= 1
                    break
                if v == int(i)*(10**a):
                    ras += k + ' '
                    a -= 1
        if sti < 20:
            break
    return ras
print(calc())