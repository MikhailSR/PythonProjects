from random import choice
from string import digits


correctPassword = "11111"  # правильный пароль
len_correctPassword = len(correctPassword)
wrongPasswords = set()  # множество для неправильных паролей
run = True
count = 0

while run:
    password = ""
    for i in range(len_correctPassword):
        password = ""
        for j in range(len_correctPassword):
            password += choice(digits)
        if password not in wrongPasswords:
            if password == correctPassword:
                run = False
                break
            else:
                print(password)
                wrongPasswords.add(password)
                count += 1


print("Correct password: ", password)
print("Вариантов перебрано: ", count)