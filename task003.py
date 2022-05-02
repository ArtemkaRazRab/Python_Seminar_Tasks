# Задача 3. Найти максимальное из трех чисел

numberA = int(input('Введите число A: '))
numberB = int(input('Введите число B: '))
numberC = int(input('Введите число C: '))

if numberA < numberB and numberC < numberB:
    print(f'большее число {numberB}')
elif numberA < numberC:
    print(f'большее число {numberC}')
else:
    print(f'большее число {numberA}')