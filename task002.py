# Задача 2. Даны два числа. Показать большее и меньшее число

numberA = int(input('Введите число A: '))
numberB = int(input('Введите число B: '))
if numberA > numberB:
    print(f'большее число {numberA}, меньшее число {numberB}')
elif numberA == numberB:
    print(f'число {numberA} равно числу {numberB}')
else:
    print(f'большее число {numberB}, меньшее число {numberA}')