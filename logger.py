from data_create import name_data, surname_data, phone_data, address_data

# logger.py
from data_create import name_data, surname_data, phone_data, address_data

first_dict = {}
second_dict = {}


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате записать данные\n\n"
                    f"1 Вариант: \n"
                    f"{name}\n{surname}\n{phone}\n{address}\n\n"
                    f"2 Вариант: \n "
                    f"{name};{surname};{phone};{address}\n"
                    f"Выберите вариант: "))
    while var != 1 and var != 2:
        print("Неправильный ввод ")
        var = int(input("Введите число "))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")
            print("Данные успешно записаны в файл в первом формате.")
    elif var == 2:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name};{surname};{phone};{address}\n\n")
            print("Данные успешно записаны в файл во втором формате.")

def dict_contacts_first(): # прочитаем файлы и соберем в словари 1 и 2
    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
        contacts_1 = f.readlines()
        for i in range(0, len(contacts_1) - 4, 5):
            name = contacts_1[i].strip()         # strip - удаляет пробельные символы с начала и сконца строки
            surname = contacts_1[i+1].strip()
            key = (name, surname)     # ключ - кортеж имя+фамилия
            first_dict[key] = {
            'Номер': contacts_1[i+2],
            'Адрес': contacts_1[i+3].strip()
            }
    return first_dict
    
def dict_contacts_second():
    with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
        contacts_2 = f.readlines()
        for i in range(0, len(contacts_2) - 1, 2):
            total = contacts_2[i].strip().split(';')
            name = total[0]
            surname = total[1]
            key = (name, surname)     # ключ - кортеж имя+фамилия
            second_dict[key] = {
            'Номер': total[2],
            'Адрес': total[3].strip()}

    return second_dict
            
def print_data():
    print('Вывожу данные из 1 файла: \n')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as f: 
        # r - read чтение данных
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_list.append(''.join(data_first[j:i+1]))
                j=i
        print(''.join(data_first_list))

    print('Вывожу данные из 2 файла: \n')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as f: 
        data_second = f.readlines()
        print(*data_second)   # *- распаковка

def delete_data():
    colection_first = dict_contacts_first()
    colection_second = dict_contacts_second()
    name_del = input("Введите имя для удаления: ")
    surname_del = input("Введите фамилию для удаления: ")

    if (name_del, surname_del) in colection_first:
        del colection_first[(name_del, surname_del)]
        with open('data_first_variant.csv', 'w', encoding='utf-8') as f:
            for key, value in colection_first.items():
                f.write(f"{key[0]}\n{key[1]}\n{value['Номер']}{value['Адрес']}\n\n")
                        
        print(f"Контакт с именем или фамилией '{name_del, surname_del}' успешно удален из файла 'data_first_variant.csv'.")
    

    elif (name_del, surname_del) in colection_second:
        del colection_second[(name_del, surname_del)]
        with open('data_second_variant.csv', 'w', encoding='utf-8') as f:
            for key, value in colection_second.items():
                f.write(f"{key[0]};{key[1]};{value['Номер']};{value['Адрес']}\n\n")
        print(f"Контакт с именем или фамилией '{name_del, surname_del}' успешно удален из файла 'data_second_variant.csv'.")

    else: print("Такого контакта нет в записной книге!")
    
def update_data():
    colection_first = dict_contacts_first()
    colection_second = dict_contacts_second()
    name_updet = input("Введите имя записи, в которой необходимо внести изменения: ")
    surname_update = input("Введите фамилию записи, в которой необходимо внести изменения: ")

    if (name_updet, surname_update) in colection_first:
        del colection_first[(name_updet, surname_update)]
        phone = input("Укажите новый номер телефона: ")
        address = input("Укажите новый адрес: ")
        
        with open('data_first_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name_updet}\n{surname_update}\n{phone}\n{address}\n\n")
            print("Данные успешно записаны в файл в первом формате.")
    
    elif (name_updet, surname_update) in colection_second:
        del colection_second[(name_updet, surname_update)]
        phone = input("Укажите новый номер телефона: ")
        address = input("Укажите новый адрес: ")
        with open('data_second_variant.csv', 'w', encoding='utf-8') as f:
            for key, value in colection_second.items():
                f.write(f"{key[0]};{key[1]};{value['Номер']};{value['Адрес']}\n\n")
        with open('data_second_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name_updet};{surname_update};{phone};{address}\n\n")
            print("Данные успешно записаны в файл во втором формате.")

    else: print("Такого контакта нет в записной книге!")
    
    