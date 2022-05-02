# Задача 15. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# Пользователь вводит A, B, C
#     1) с помощью математических формул
#     2) с помощью дополнительных библиотек python

a=int(input('Введите число a:'))
b=int(input('Введите число b:'))
c=int(input('Введите число c:'))

def diskr(a ,b ,c):
    d=b**2-4*a*c
    return d

def sqrt(a, b, c):
    d=diskr(a, b, c)
    if d>0:
        x1=(-b+d**0.5)/(2*a)
        x2=(-b-d**0.5)/(2*a)
        return x1, x2
    elif d==0:
        x=-b/2*a
        return x
    else:
        return False
print(sqrt(a, b, c))


# Можно записать вот так
# def abc(a, b, c):
#     d=b**2-4*a*c
#     if d<0 or a==0:
#         return ('нет корней')
#     x1=(-b+d**(1/2))/(2*a)
#     x2=(-b-d**(1/2))/(2*a)
#     return(x1, x2)
# a=int(input('Введите число a:'))
# b=int(input('Введите число b:'))
# c=int(input('Введите число c:'))
# print(abc(a, b, c))