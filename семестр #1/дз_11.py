# 9

def digits(s, count=0, ind=-1):
    ind+=1
    try:
        if len(s)==ind:
            return count
        elif int(s[ind]):
            count+=1
            return digits(s, count, ind)
    except ValueError:
        return digits(s, count, ind)
s = 'as2d54w8d4a1df6ef   s5fdx8d2s1ca5s4d2'
print(digits(s))

#10

def simm(s, ind=-1):
    ind += 1
    if ind >= len(s)/2:
        return 'да, строка симметрична'
    else:
        if s[ind] == s[ind*-1-1]:
            return simm(s, ind)
        else:
            return 'нет, строка несимметрична'
s = 'asdkj5l5l5jkdsa'
print(simm(s))

