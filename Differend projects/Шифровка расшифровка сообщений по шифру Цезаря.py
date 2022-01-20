# variant 1
# message = input('Введите сообщение: ').upper()
# result = ''
#
# for char in message:
#     if char.isupper():
#         value = ord(char)+13
#         char = chr(value)
#     if not char.isupper():
#         value -= 26
#         char = chr(value)
#     result += char
# print(result)


# my version 2
message = input('Введите сообщение: ').upper()
result = ''

for char in message:
    value = ord(char)+13
    if value > 90:
        value -= 26
        char = chr(value)
    else:
        char = chr(value)
    result += char
print(result)
