string = '100101110000110'
max = 0
count = 0

for i in range(len(string)):
    if string[i] == '0':
        count += 1
    else:
        count = 0
    if count > max:
        max = count
print(max)