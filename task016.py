# Задача 16. Задайте два числа.
# Напишите программу, которая найдет НОК (наименьшее общее кратное) этих двух чисел

a = int(input('Введите число a:'))
b = int(input('Введите число b:'))
c = max(a, b)

while ((c % b != 0) and (c % a != 0)) or ((c % b == 0) and (c % a != 0)) or ((c % b != 0) and (c % a == 0)):
    c += 1

print(c)


# Можно записать вот так

# a = int(input('Введите число a:'))
# b = int(input('Введите число b:'))
# c = max(a, b)
# k = 1
# while True:
#     if ((c*k) % a == 0 and (c*k) % b == 0):
#         print(c*k)
#         break
#     k+=1

# Можно записать вот так

a = int(input('Введите число a:'))
b = int(input('Введите число b:'))

def nok(a, b):
    k = 1
    c = max(a, b)
    while True:
        if ((c*k) % a == 0 and (c*k) % b == 0):
            return(c*k)
        k+=1
print(nok(a, b))