# Задача 8. Показать числа от -N до N

N = int(input('Введите число N: '))
for i in range(-N, N+1, 1):
    print(i, end=' ')

# Еще один способ решения этой задачи (while)

n = int(input('Введите число N: '))
i = -n
while i <= n:
    print(i, end=' ')
    i = i+1