# Задача 13 - Запись в файл словаря

# my_dict={
#     1: 'One',
#     2: 'Two'
# }
# data=open('test.txt', 'w')
# for i in my_dict:
#     data.write(my_dict[i])
#     data.write(' ')
# data.close()

# path='test.txt'
# with open(path, 'r') as data:
#     for line in data:
#         print(line, end='')

# можно записать вот так

# file_name='test.txt'
# my_dict={
#     1: 'One',
#     2: 'Two'
# }
# file=open('test.txt', 'w')
# for i in my_dict:
#     file.write(my_dict[i])
# file.close()

# file=open('test.txt', 'r')
# for i in file:
#     print(i)
# file.close()

# можно записать вот так

# file_name='test.txt'
# my_dict={
#     1: 'One',
#     2: 'Two'
# }

# file=open('test.txt', 'r')
# all_info=file.read(5)
# print(all_info)
# file.close()