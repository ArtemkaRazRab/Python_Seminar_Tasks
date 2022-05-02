# Задача 9. Показать последнюю цифру трехзначного числа

number = int(input('Введите трехзначное число: '))
if number < 100 or number > 999:
    print('Ошибка')
else:
    print(number % 10)

# Еще один способ решения этой задачи (while)

# while True:
#     num = int(input('Введите трехзначное число: '))
#     if len(str(num)) != 3:
#         print('Я просил трехзначное число')
#     elif len(str(num)) == 3:
#         break
# print(f'Последняя цифра этого числа - {num % 10}')

# Еще один способ решения этой задачи

# digit=input('')
# print(digit[-1])

# Еще один способ решения этой задачи (random)

# import random
# number = random.randint(100, 999)
# print(number)
# findLastNumber = number % 10
# print(findLastNumber)