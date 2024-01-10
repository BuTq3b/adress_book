from logger import print_data, input_data, delete_data, update_data


def interface():
    print("Добрый день! Это телефонный справочник! \n 1 - Запись данных \n 2 - Удаление данных \n 3 - Изменение данных \n 4 - Вывод данных")
    command = int(input("Введите число "))
    while command != 1 and command != 2 and command != 3 and command != 4:
        print("Неправильный ввод ")
        command = int(input("Введите число "))

    if command == 1:
        input_data()

    elif command == 2:
        delete_data()

    elif command == 3:
        update_data()

    elif command == 4:
        print_data()