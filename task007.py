# Задача 7. По заданному номеру дня недели вывести его название

N = int(input('Введите номер дня недели: '))
if N == 1:
    print('Понедельник')
elif N == 2:
    print('Вторник')
elif N == 3:
    print('Среда')
elif N == 4:
    print('Четверг')
elif N == 5:
    print('Пятница')
elif N == 6:
    print('Суббота')
elif N == 7:
    print('Воскресенье')
elif N < 1 or N > 7:
    print('Ошибка')