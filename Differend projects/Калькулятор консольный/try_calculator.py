from sys import exit as ex


def inputNumber():
    while True:
        try: 
            number = float(input('\n---Введите число: '))
            return number
        except ValueError: 
            # if not(number): ex()
            print('Возможно в строке есть буквы или пробелы. Попробуйте еще раз!')


def inputOperation():
    while True:
        operation = input('---Введите действие: ')
        operation = operation.strip()

        if not(operation): ex()
        if operation not in ['+', '-', '*', '/', '**', 'sqrt']: print('Такой операции не существует!')
        else: return operation



# def checkOperations(object):
#     if not(object): return ex()
#     if object not in ['+', '-', '*', '/', '**', 'sqrt']: return 'Такой операции не существует!'


# def check(object):
#     if not(object): ex()
#     try: float(object)
#     except ValueError: return 'Возможно в строке есть буквы или пробелы. Попробуйте еще раз!'


def squareRoot(number):
    from math import sqrt

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
    firstNumber = inputNumber()
    operation = inputOperation()

    if operation == 'sqrt':
        squareRoot(firstNumber)
    else:
        secondNumber = inputNumber()

        while True:
            # firstNumber = float(firstNumber)
            # secondNumber = float(secondNumber)

            if operation == '+': print('\tРезультат:', add(firstNumber, secondNumber))
            elif operation == '-': print('\tРезультат:', sub(firstNumber, secondNumber))
            elif operation == '*': print('\tРезультат:', mul(firstNumber, secondNumber))
            elif operation == '/': print('\tРезультат:', div(firstNumber, secondNumber))
            elif operation == '**': print('\tРезультат:', pow(firstNumber, secondNumber))

            firstNumber = inputNumber()
            operation = inputOperation()

            if operation == 'sqrt': squareRoot(firstNumber)
            secondNumber = inputNumber()


if __name__ == '__main__':
    while True:
        main()