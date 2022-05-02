# Задача 11. Выяснить, кратно ли число заданному или нет, если нет, вывести остаток

numberA = int(input('Введите число А: '))
numberB = int(input('Введите число B: '))
if numberA % numberB == 0:
    print(f'число {numberA} кратно числу {numberB}')
else:
    print(f'число {numberA} не кратно числу {numberB}, остаток {numberA % numberB}')


# Еще один способ решения этой задачи (TRUE/FALSE)

# numberA = int(input('Введите число А: '))
# numberB = int(input('Введите число B: '))
# if numberA % numberB:
#     print(f'число {numberA} не кратно числу {numberB}, остаток {numberA % numberB}')
# else:
#     print(f'число {numberA} кратно числу {numberB}')


# ФИШКИ PYTHON
# a=[1,2,3]
# b=a
# a.append(4)
# print(b)

# Копирование списка

# a=[1,2,3]
# b=a[:] # Срез
# a.append(4)
# print(b)