# 1. Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.

# *Пример:*

# 2+2 => 4;

# 1+2*3 => 7;

# 1-2*3 => -5;

# num = input('введите выражение через пробел ')
# logic = num.split(' ')
# print(logic)
# # result_1 = [i for i in range(len(logic)) if logic[i] == '*' or logic[i] == '/']
# # result_2 = [i for i in range(len(logic)) if logic[i] == '+' or logic[i] == '-']

# mult = num
# for i in range(len(logic)):
#     if logic[i] == '*':
#         mult = int(logic[i - 1]) * int(logic[i + 1])
#     elif logic[i] == '/':
#         mult = int(logic[i - 1]) / int(logic[i + 1])
# print(mult)

# еще один вариант решения

Str = input("Введите пример: ")
List = []
for i in Str:
    List.append(i)
print(List)
for j in range (2):
    for i in range (len(List)):
        if i < len(List):
            if List[i] == '*':
                List[i] = int(List[i-1]) * int(List[i+1])
                List.pop(i-1)
                List.pop(i)
            elif List[i] == '/':
                List[i] = int(List[i-1]) / int(List[i+1])
                List.pop(i-1)
                List.pop(i)
        else:
            break
print(List)
for j in range (2):
    for i in range (len(List)):
        if i < len(List):
            if List[i] == '+':
                List[i] = int(List[i-1]) + int(List[i+1])
                List.pop(i-1)
                List.pop(i)
            elif List[i] == '-':
                List[i] = int(List[i-1]) - int(List[i+1])
                List.pop(i-1)
                List.pop(i)
        else:
            break
print(List)

# еще один вариант решения

# expression = '23+2*12/6-9'
# print(eval(expression))