from sys import exit as ex
from math import sqrt
import test_calc


def checkOperations(object):
    if not(object): return ex()
    if object not in ['+', '-', '*', '/', '**', 'sqrt']: return 'Такой операции не существует!'


def check(object):
    if not(object): ex()
    try: float(object)
    except ValueError: return 'Возможно в строке есть буквы или пробелы. Попробуйте еще раз!'


def squareRoot(number):
    try:
        print('\tРезультат:', round(sqrt(float(number)), 3))
        main()
    except ValueError:
        print('Корень из отрицательных чисел не добывается')
        main()


def add(a, b):
    return round(a + b, 3)


def sub(a, b):
    return round(a - b, 3)
    

def mul(a, b):
    return round(a * b, 3)


def div(a, b):
    try: return round(a / b, 3)
    except ZeroDivisionError: return 'На ноль делить нельзя!'


def pow(a, b):
    return round(a ** b, 3)   


def main():
    firstNumber = input('\n---Введите первое число: ')
    if check(firstNumber) == 'Возможно в строке есть буквы или пробелы. Попробуйте еще раз!': 
        print('Возможно в строке есть буквы или пробелы. Попробуйте еще раз!')
        return 0

    operation = input('---Введите действие: ')
    operation = operation.strip()
    if checkOperations(operation) == 'Такой операции не существует!':
         print('Такой операции не существует!') 
         return 0
    
    if operation == 'sqrt':
        squareRoot(firstNumber)
    else:
        secondNumber = input('---Введите второе число: ')
        if check(secondNumber) == 'Возможно в строке есть буквы или пробелы. Попробуйте еще раз!': 
            print('Возможно в строке есть буквы или пробелы. Попробуйте еще раз!')
            return 0

        while True:
            firstNumber = float(firstNumber)
            secondNumber = float(secondNumber)

            if operation == '+': print('\tРезультат:', add(firstNumber, secondNumber))
            elif operation == '-': print('\tРезультат:', sub(firstNumber, secondNumber))
            elif operation == '*': print('\tРезультат:', mul(firstNumber, secondNumber))
            elif operation == '/': print('\tРезультат:', div(firstNumber, secondNumber))
            elif operation == '**': print('\tРезультат:', pow(firstNumber, secondNumber))

            firstNumber = input('\n---Введите первое число: ')
            if check(firstNumber) == 'Возможно в строке есть буквы или пробелы. Попробуйте еще раз!': 
                print('Возможно в строке есть буквы или пробелы. Попробуйте еще раз!')
                return 0

            operation = input('---Введите действие: ')
            if checkOperations(operation) == 'Такой операции не существует!':
                print('Такой операции не существует!') 
                return 0

            if operation == 'sqrt': squareRoot(firstNumber)

            secondNumber = input('---Введите второе число: ')
            if check(secondNumber) == 'Возможно в строке есть буквы или пробелы. Попробуйте еще раз!': 
                print('Возможно в строке есть буквы или пробелы. Попробуйте еще раз!')
                return 0


if __name__ == '__main__':
    while True:
        main()