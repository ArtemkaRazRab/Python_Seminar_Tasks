# Задача 10. Дано число из отрезка [10, 99]. Показать наибольшую цифру числа

number = int(input('Введите число из отрезка [10, 99]: '))
if number < 10 or number > 99:
    print('Ошибка')
elif number // 10 > number % 10:
    print(number // 10)
elif number // 10 < number % 10:
    print(number % 10)
else:
    print('Цифры данного числа одинаковы')

# Еще один способ решения этой задачи (random)

# import random
# randomNumber = random.randint(10, 99)
# findOneDigit = randomNumber % 10
# findTwoDigit = int(randomNumber/10)
# print('Случайное число:',randomNumber)
# if findOneDigit > findTwoDigit:
#     print('Большая цифра числа:',findOneDigit)
# else:
#     print('Большая цифра числа:',findTwoDigit)

# Еще один способ решения этой задачи (random)

# number = 45678
# numberList = []
# while number > 0:
#     numberList.append(number % 10)
#     number //= 10
# print(numberList)
# numberListLenght = len(numberList)
# maxNumber = numberList[0]
# minNumber = numberList[0]

# for i in range(numberListLenght):
#     if numberList[i] > maxNumber:
#         maxNumber = numberList[i]
#     if numberList[i] < minNumber:
#         minNumber = numberList[i]
# print(f'maxNumber: {maxNumber}, minNumber: {minNumber}')

# Пример использования встроенных функций min, max
# my_list = [1.01, -412.4, 312, 12, -41, 12.42]
# print(min(my_list))
# print(max(my_list))