from random import *

list_orig = [61, 228, 9, 9]
tuple_orig = tuple(list_orig) # делаю из массива кортеж
list2 = list(tuple_orig) # делаю дубляж оригинального массива, чтобы далее удялять элементы из него
list3 = [] # массив с разными вариациями соединений
list4 = [] # результирующий массив
sum =  ''
max_elem = 0

for k in range(20):
    list2 = list(tuple_orig)
    list3 = []
    
    for i in range(len(list2)): # рандомно выбираю значения из 
        num = choice(list2)
        indx = list2.index(num)
        del list2[indx] # !!!!!!
        list3.append(num)

    for j in list3: # переделываю все значения в строку и добавляю во временную переменную
        sum += str(j)

    list4.append(int(sum)) # переделываю в int и добавляю в массив list4
    sum=''
    
    

print(max(list4))
