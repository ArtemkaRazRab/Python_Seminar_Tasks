# 3. Напишите программу, удаляющую из текста все слова, содержащие "абв".
my_str = 'Напишите прогабврамму, удабваляющую из текста все слова, содержащие'
my_str = my_str.split(' ')
res = ''
for word in my_str:
    if word.find('абв') == -1:
        #res += word + ' '
        res = res+ word + ' '
print(res)