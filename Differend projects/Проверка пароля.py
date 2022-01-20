def check_pass(pswd):

    errors = {1:'недостаточная длина',
              2:'нет заглавных букв',
              3:'нет строчных букв',
              4:"нет чисел",
              5:"недостаточно чисел",
              6:"нет спецсимволов"}

    # основные проверки пароля (наличие спецсимволов, заглавных и маленьких букв, длина)
    if len(pswd) >= 8:
        del errors[1]
    if ('*' in pswd) or ('#' in pswd) or ('-' in pswd):
         del errors[6]
    if pswd.lower() != pswd:
        del errors[2]
    if pswd.upper() != pswd:
        del errors[3]

    # проверка на налицие цифр и их количество
    countNumbers = 0
    for i in pswd:
        if i.isdigit():
            countNumbers += 1
        if countNumbers == 3:
            del errors[5]
            del errors[4]
            break
    else:
        if countNumbers == 0: del errors[5]
        else: del errors[4]


    # вывод ошибок, если есть и вывод результата если нет
    if len(errors) == 0:
        print('Пароль надёжный')
    else:
        for value in errors.values():
            print(value)


print(check_pass('889Yy#*T'))
# print(check_pass('@#@@u'))
# print(check_pass('Tr56#2@@'))
# print(check_pass('qwerty11'))
# print(check_pass('11qweQ-s'))