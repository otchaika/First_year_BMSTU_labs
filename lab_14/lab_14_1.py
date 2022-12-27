# Силинг Екатерина 14 лабораторная
import os
import struct

file_selected = False
b_num = 60


def do_task(i):
    if i == 1:
        select_file()
    elif i == 2:
        inisialize_db()
    elif i == 3:
        if not file_selected:
            print('Файл не выбран')
        else:
            print_db(selected_file)
    elif i == 4:
        if not file_selected:
            print('Файл не выбран')
        else:
            append_db()
    elif i == 5:
        if not file_selected:
            select_file()
        else:
            while ValueError or AssertionError:
                try:
                    index1 = input('Введите номер строки (счет от 0), которую вы хотите удалить: ')
                    index = int(index1)
                    assert index > -1
                except ValueError:
                    print('Введите целое число')
                except AssertionError:
                    print('Значение должно быть больше или равно 0.')
                else:
                    break
            delete_db(selected_file, index)
    elif i == 6:
        if not file_selected:
            print('Файл не выбран')
        else:
            one_search()
    elif i == 7:
        if not file_selected:
            print('Файл не выбран')
        else:
            two_search()


def select_file():
    global file_selected
    global selected_file
    flag = False
    while IOError or AssertionError or FileNotFoundError:
        try:
            i = str(input('Введите путь до файла (заканчивается на .bin)'))
            f = open(i)
            assert i[-4:] == '.bin'
        except IOError:
            print('Такого файла не существует')
            flag = True
            break
        except AssertionError:
            print('Путь должен заканчиваться на .bin')
        else:
            break
    if not flag:
        i = os.path.abspath(i)
        print_db(i)
        selected_file = i
        file_selected = True


def print_db(file):
    f = open(file, 'rb')
    print('Файл:')
    print('{0:15s}|{1:14s}|{2:13s}|{3:12s}'.format('НАЗВАНИЕ', 'ДАТА', 'УЧАСТНИКИ', 'РЕЗУЛЬТАТ'))
    print('-' * 60)
    lenn = 0
    with open(file, 'rb') as f:
        a = f.read(1)
        g = a.decode('utf-8')
        print(g, end='')
        while a != b'':
            lenn += 1
            if lenn % b_num == 0:
                print()
            a = f.read(1)
            g = a.decode('utf-8')
            print(g, end='')


def inisialize_db():
    global selected_file
    global file_selected
    print('Выберите: (1) создать файл, (2) перезаписать существующий файл')
    while ValueError or AssertionError:
        try:
            i1 = str(input('Выберите действие: '))
            i = int(i1)
            assert 1 <= i and i <= 2
        except AssertionError:
            print('Введите число от 1 до 2')
        except ValueError:
            print('Введите целое число')
        else:
            break
    if i == 1:
        while IOError or AssertionError or FileNotFoundError:
            try:
                i = str(input('Введите путь до файла (заканчивается на .bin)'))
                f = open(i, 'wb')
                assert i[-4:] == '.bin'
            except IOError:
                print('Такого пути не существует')
            except AssertionError:
                print('Путь должен заканчиваться на .bin')
            else:
                break
        selected_file = i

    elif i == 2:
        if not file_selected:
            print('Вам необходимо выбрать файл для работы!')
            select_file()
    while ValueError or AssertionError:
        try:
            str_ii = input('Введите количество строк: ')
            str_i = int(str_ii)
            assert str_i > 0
        except ValueError:
            print('Введите целое число')
        except AssertionError:
            print('Значение должно быть больше 0.')
        else:
            break
    my_file = open(selected_file, "wb+")
    for i in range(str_i):
        my_file.write(fill_in())
    my_file.close()
    print_db(selected_file)
    file_selected = True


def fill_in():
    i1 = str(input('Введите название войны: '))
    while len(i1) > 15:
        i1 = str(input('Название должно занимать менее 15 символов. Введите снова: '))
    while ValueError or AssertionError:
        try:
            i21 = input('Введите дату войны: ')
            i2 = int(i21)
            assert len(str(i2)) <= 15
        except ValueError:
            print('Введите целое число')
        except AssertionError:
            print('Значение должно занимать менее 15 символов.')
        else:
            break
    i3 = str(input('Введите участников: '))
    while len(i3) > 15:
        i3 = str(input('Значение должно занимать менее 15 символов. Введите снова: '))
    i4 = str(input('Введите результат: '))
    while len(i4) > 15:
        i4 = str(input('Значение должно занимать менее 15 символов. Введите снова: '))
    i1 += ' ' * (15 - len(i1))
    i2 = str(i2) + ' ' * (15 - len(str(i2)))
    i3 += ' ' * (15 - len(i3))
    i4 += ' ' * (15 - len(i4))
    new_str = i1 + str(i2) + i3 + i4
    return new_str.encode('utf-8')


def adding(path, id, size):  # добавление
    f = open(path, 'rb+')
    f.seek(0, 0)
    lenn = size // b_num
    for i in range(id):  # сдвиг до нужного места
        f.seek(b_num, 1)
    if id <= lenn:
        cur = fill_in()
        temp = f.read(b_num)
        f.seek(-b_num, 1)
        while temp != b'':  # перезапись нужного количества строк
            f.write(cur)
            cur = temp
            temp = f.read(b_num)
            f.seek(-b_num, 1)
        if cur != b'':
            f.seek(b_num, 1)
            f.write(cur)
    else:
        print('Недостаточно строк. строк в файле ', lenn)
    f.close()


def append_db():
    if not file_selected:
        print('Вам необходимо выбрать файл для работы!')
        select_file()
    while ValueError or AssertionError:
        try:
            index1 = input('Введите номер строки (счет от 0), которую вы хотите добавить: ')
            index = int(index1)
            assert index > -1
        except ValueError:
            print('Введите целое число')
        except AssertionError:
            print('Значение должно быть больше или равно 0.')
        else:
            break
    adding(selected_file, index, len(open(selected_file).read()))


def delete_db(path, ind):
    global b_num
    f = open(path, 'rb+')
    b = f.read(b_num)
    lenn = 0
    while b != b'':
        b = f.read(b_num)
        lenn += 1

    if lenn <= ind:
        print('Строк не хватает')
    else:
        f.seek(b_num * (ind + 1), 0)
        for i in range(lenn - ind - 1):
            temp = f.read(b_num)
            print(i)
            f.seek(-2 * b_num, 1)
            f.write(temp)
            f.seek(b_num, 1)
        f.truncate((lenn - 1) * b_num)
        f.close()


def one_search():
    print('поиск производится по полю "ДАТА".')
    while ValueError:
        try:
            date1 = str(input('Введите дату для поиска: '))
            date = int(date1)
        except ValueError:
            print('Введите число')
        else:
            break
    f = open(selected_file, 'rb')
    b = f.read(b_num)
    flag = False
    while b != b'':
        b = b.decode('utf-8')
        a = b[15:30]
        a.strip()
        if int(a) == date:
            if not flag:
                print('{0:15s}|{1:14s}|{2:13s}|{3:12s}'.format('НАЗВАНИЕ', 'ДАТА', 'УЧАСТНИКИ', 'РЕЗУЛЬТАТ'))
                print('-' * 60)
            print(b)
            flag = True
        b = f.read(b_num)
    if not flag:
        print('Подходящих строк не нашлось.')


def two_search():
    print('поиск производится по полю "ДАТА" и э "НАЗВАНИЕ".')
    while ValueError:
        try:
            date1 = str(input('Введите дату для поиска: '))
            date = int(date1)
        except ValueError:
            print('Введите число')
        else:
            break
    while AssertionError:
        try:
            name = str(input('Введите название для поиска: '))
            assert name != ''
        except AssertionError:
            print('Введите не пустую строку')
        else:
            break
    f = open(selected_file, 'rb')
    b = f.read(b_num)
    flag = False
    while b != b'':
        b = b.decode('utf-8')
        a = b[15:30]
        a = a.strip()
        aa = b[:15]
        aa = aa.strip()
        if int(a) == date and aa == name:
            if not flag:
                print('{0:15s}|{1:14s}|{2:13s}|{3:12s}'.format('НАЗВАНИЕ', 'ДАТА', 'УЧАСТНИКИ', 'РЕЗУЛЬТАТ'))
                print('-' * 60)
            print(b)
            flag = True
        b = f.read(b_num)
    if not flag:
        print('Подходящих строк не нашлось.')


while True:
    print('Меню: ')
    print('1. Выбрать файл для работы')
    print('2. Инициализировать базу данных (создать либо перезаписать файл и заполнить его записями)')
    print('3. Вывести содержимое базы данных')
    print('4. Добавить запись')
    print('5. Удалить запись')
    print('6. Поиск по одному полю')
    print('7. Поиск по двум полям')
    print('8. Завершить программу')
    while ValueError or AssertionError:
        try:
            i1 = str(input('Выберите действие: '))
            i = int(i1)
            assert 1 <= i and i <= 8
        except AssertionError:
            print('Введите число от 1 до 8')
        except ValueError:
            print('Введите целое число')
        else:
            break
    if i == 8:
        raise SystemExit
    do_task(i)
