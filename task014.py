# Задача 14. Задайте строку из набора чисел.
# Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя использовать пробел

path = 'task2.txt'
data=open(path, 'r')
list = data.read().split()
data.close
for i in range(0, len(list)):
    list[i] = int(list[i])
print(list)
print('Максимальное число:', max(list))
print('Минимальное число:', min(list))

# my_str='123 456 789 147 258 369'
# print(my_str.split(' '))