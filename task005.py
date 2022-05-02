# Задача 5. Показать четные числа от 1 до N

# N = int(input('Введите число N: '))
# for i in range(1, N+1, 1):
#     if not (i % 2):
#         print(i)

# Ещё один вариант решения этой задачи

# N = int(input('Введите число N: '))
# for i in range(2, N+1, 2):
#     print(i)

# Ещё один вариант решения этой задачи (списки)
evenlist = []
N = int(input('Введите число N: '))
for i in range(2, N+1, 2):
    if i % 2 == 0:
        evenlist.append(i)
print(evenlist)