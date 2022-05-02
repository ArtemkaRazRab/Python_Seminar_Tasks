# списки: list[]
# кортежи: tuple()
# словари: dict{} (keys(), values(), items())
# множества: set{}
# работа с файлами
# функции


# my_list = [1, 2, 3, 4, 5]  # список
# my_tuple = (1, 2, 3, 4, 5)  # кортеж


# словари

# my_dict={
#     ('красный', 'спелый'): 'помидор'
# }
# print(my_dict[('красный', 'спелый')])

# my_tuple = ('красный', 'спелый')
# my_dict={
#     my_tuple: 'помидор'
# }
# print(my_dict[(my_tuple)])

# my_dict = {
#     62234: {
#         'name': 'стул',
#         'count': '100'
#     },
#     54324: {
#         'name': 'диван',
#         'count': '50'
#     }
# }
# print(my_dict[54324]['name'])

# my_dict = {
#     62234: {
#         'name': 'стул',
#         'count': '100'
#     },
#     54324: {
#         'name': 'диван',
#         'count': '50'
#     }
# }
# # for key in my_dict.keys(): # выводим ключи из верхнего уровня
# #     print(key)
# #     print(my_dict[key])

# # for value in my_dict.values(): # выводим значения из верхнего уровня
# #     print(value)

# for key, value in my_dict.items(): # выводим значения из верхнего уровня
#     print(key, value)


# множества

# my_set = {1, 2, 3, 4}
# my_set.add(5)
# print(my_set)

# Задача 12 Структурировать словарь (id, имя, дата и т.д)
# Что делать с данными: найти, добавить, заменить, удалить

while True:
    menu_programm = {
    1: 'найти товар',
    2: 'добавить товар',
    3: 'заменить товар',
    4: 'удалить товар',
}

    for key, value in menu_programm.items():
        print(f'{key}: {value}')

    number_menu = int(input('выберите нужный пункт меню: '))

    menu_product = {
        '001': {
            'наименование': 'молоко',
            'количество': '50 шт',
            'дата изготовления': '23.04.2022',
            'срок годности': '1 месяц'
        },

        '002': {
            'наименование': 'хлеб',
            'количество': '100 шт',
            'дата изготовления': '24.04.2022',
            'срок годности': '7 дней'
        },

        '003': {
            'наименование': 'масло',
            'количество': '30 шт',
            'дата изготовления': '25.04.2022',
            'срок годности': '12 месяцев'
        }
    }
    if number_menu == 1:
        id_search = str(input('введите id товара, который хотите найти: '))
        for key, value in menu_product[id_search].items():
            print(f'{key}: {value}')

    elif number_menu == 2:
        name_add = str(input('введите id товара, который хотите добавить: '))
        name = str(input('наименование: '))
        count = str(input('количество: '))
        production_date = str(input('дата изготовления: '))
        expiry_date = str(input('срок годности: '))
        menu_product[name_add] = {'наименование': name,
                                'количество': count,
                                'дата изготовления': production_date,
                                'срок годности': expiry_date}
        for key, value in menu_product.items():
            print(f'{key} {value}')

    elif number_menu == 3:
        name_old = str(input('введите id товара, который хотите заменить: '))
        name_new = str(input('введите новое id товара, который хотите добавить: '))
        name = str(input('наименование: '))
        count = str(input('количество: '))
        production_date = str(input('дата изготовления: '))
        expiry_date = str(input('срок годности: '))
        menu_product[name_new] = menu_product.pop(name_old)
        menu_product[name_new] = {'наименование': name,
                                'количество': count,
                                'дата изготовления': production_date,
                                'срок годности': expiry_date}
        for key, value in menu_product.items():
            print(f'{key} {value}')

    elif number_menu == 4:
        name_del = str(input('введите id товара, который хотите удалить: '))
        del menu_product[name_del]
        for key, value in menu_product.items():
            print(f'{key} {value}')
        break
