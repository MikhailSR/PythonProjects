from random import choice, shuffle
import string as st


def gen(lenght, method):
	passwords = []

	simple = 0
	while simple <= lenght:
		for j in range(len(method)):
			if method[j] == 'chars':
				passwords.append(choice(st.punctuation))
				simple += 1
				continue
			if method[j] == 'liters_small':
				passwords.append(choice(st.ascii_lowercase))
				simple += 1
				continue
			if method[j] == 'liters_big':
				passwords.append(choice(st.ascii_uppercase))
				simple += 1
				continue
			if method[j] == 'numbers':
				passwords.append(choice(st.digits))
				simple += 1
				continue

	shuffle(passwords)
	return ''.join(passwords)


def main():
	method = []
	number = int(input('Кол-во паролей: '))
	lenght = int(input('Длина строки: '))

	chars_quest = input("Спецсимволы (+/-): ")
	liters_small_quest = input("Маленькие буквы (+/-): ")
	liters_big_quest = input("Большие буквы (+/-): ")
	numbers_quest = input("Цифры (+/-): ")

	if chars_quest == '+': method.append('chars')
	if liters_small_quest == '+': method.append('liters_small')
	if liters_big_quest == '+': method.append('liters_big')
	if numbers_quest == '+': method.append('numbers')

	print('Result:\n')
	for i in range(number):
		print(gen(lenght, method))

main()