linesFile = [] 

with open("D:/Back-end/Разные задания и проекты/Сумма цифр из файла/numb.txt", "r") as file:
    for elem in file:
        if elem != ' ':
            linesFile.append(int(elem))
    
print(sum(linesFile))


# f = open('data.txt', 'r')
# ans = 0
# for line in f:
#     try:
#         ans += int(line.strip())
#     except ValueError:
#         pass


# with open('file.txt', 'r') as fin:
#     ans = sum(int(line) for line in fin)



