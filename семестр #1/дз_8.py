# a = input('строка №1: ')
# b = input('строка №2: ')
# c = input('строка №3: ')
# print(set(a + b))
# for i in set(c):
#     s = 'из символов первых двух строк нельзя получить третью строку'
#     if i in set(a + b):
#         pass
#     else:
#         break
#     s = 'из символов первых двух строк можно получить третью строку'
# print(s)

#8

st = 'ten,one,five,two,three,four'
li = st.split(',')
dc = {}
for i in range(len(li)):
    dc.update({li[i]: i+1})
print(dc)

#9.1

phones_list = [
    {'name':'Ivan', 'city':'Moscow', 'phones':['232-19-55', '+7 (916) 230-00-75']}, 
    {'name':'Anna', 'city':'Samara', 'phones':['200-11-15']}, 
    {'name':'Anna', 'city':'Vologda', 'phones':['+7 (931) 711-00-75']},  
    {'name':'Nikolay', 'city':'Moscow', 'phones':['+7 (916) 778-71-05', '331-66-11', '783-3385']}, 
    {'name':'Ivan', 'city':'Moscow', 'phones':['+7 (916) 205-41-05', '232-19-55']}, 
    {'name':'Anna', 'city':'Samara', 'phones':['+7 (916) 105-13-56']} 
]

for el in phones_list:
    for i in phones_list:
        if el['name'] == i['name'] and el['city'] == i['city'] and el['phones'] != i['phones']:
            el['phones'] += (i['phones'])
            phones_list.pop(phones_list.index(i))
for l in phones_list:
    print(l)  

#9.2

phones = {}
for el3 in phones_list:
    phones.update({el3['city']: {el3['phones'][0]: el3['name']}})
for el4 in phones_list:
    for i2 in el4['phones']:
        phones[el4['city']].update({i2: el4['name']})
print(phones)