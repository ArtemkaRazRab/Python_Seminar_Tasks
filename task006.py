# Задача 6. По двум заданным числам проверять является ли первое квадратом второго

numberA = int(input('Введите число А: '))
numberB = int(input('Введите число B: '))
if numberA == numberB**2:
    print(f'Число {numberA} является квадратом числа {numberB}')
else:
    print(f'Число {numberA} не является квадратом числа {numberB}')