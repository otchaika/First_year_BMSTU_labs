# Силинг Екатерина. Лабораторная 13

import os
file_selected = False

def do_task(i):
    if i == 1:
        select_file()
    elif i == 2:
        inisialize_db()
    elif i == 3:
        if file_selected:
            print_db(selected_file)
        else:
            print('Сначала выберите или создайте файл для работы')
    elif i == 4:
        append_db()
    elif i == 5:
        one_search()
    elif i == 6:
        two_search()


def select_file():
    while IOError or AssertionError or FileNotFoundError:
        try:
            i = str(input('Введите путь до файла (заканчивается на .txt)'))
            f = open(i)
            assert i[-4:]=='.txt'
        except IOError:
            print('Такого файла не существует')
        except AssertionError:
            print('Путь должен заканчиваться на .txt')
        else:
            break
    i = os.path.abspath(i)
    print_db(i)
    global selected_file
    selected_file=i
    global file_selected
    file_selected=True
def is_int(i):
    nums='0123456789'
    for j in range(len(str(i))):
        if i[j] not in nums:
            return False
    return True
def assert_good_db(file):
    f = open(file, 'r')
    for i in f:
        r = i.split(';')
        if len(r) != 6 or not is_int(r[2]):
            print('Структура файла не верна')
            return False
    return True
def print_db(file):
    f = open(file, 'r')
    if assert_good_db(file):
        print('Файл:')
        print('{0:^2s}|{1:^25s}|{2:^5s}|{3:^25s}|{4:^30s}'.format('id', 'НАЗВАНИЕ', 'ДАТА', 'УЧАСТНИКИ', 'результат'))
        print('-' * 91)
        for i in f:
            r = i.split(';')
            print('{0:^2s}|{1:^25s}|{2:^5s}|{3:^25s}|{4:^30s}'.format(r[0], r[1], r[2], r[3], r[4]))
            print('-' * 91)

def inisialize_db():
    global selected_file
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
        selected_file = str(input('Введите название файла: ')) + '.txt'
    elif i == 2:
        if not file_selected:
            print('Вам необходимо выбрать файл для работы!')
            select_file()
    while ValueError:
        try:
            str_i1 = int(input('Введите количество строк в этом файле: '))
            str_i = int(str_i1)
            assert str_i>0
        except ValueError:
            print('Введите целое число')
        except AssertionError:
            print('Введите число больше 0')
        else:
            break

    my_file = open(selected_file, "w+")
    fill_in(selected_file, str_i)
    my_file.close()
    print_db(selected_file)

def fill_in(file, str_i):
    lenn = len(open(file).readlines())
    file_name = open(file, 'a')
    for i in range(str_i):
        str1=str(i+lenn)+';'
        item = str(input('Введите название войны: '))
        str1+=str(item)
        str1+=';'
        while ValueError:
            try:
                item1 = str(input('Введите дату войны: '))
                item = int(item1)
            except ValueError:
                print('Введите целое число')
            else:
                break
        str1 += str(item)
        str1 += ';'
        item = str(input('Введите участника: '))
        str1 += item
        str1 += ';'
        item = str(input('Введите результат войны: '))
        str1 += item
        str1+=';'
        file_name.write(str1+'\n')


def append_db():
    if not file_selected:
        print('Вам необходимо выбрать файл для работы!')
        select_file()
    global selected_file
    print(selected_file)
    str_i = int(input('Введите количество строк в этом файле: '))
    my_file = open(selected_file, "r+")
    fill_in(selected_file, str_i)
    my_file.close()
    print_db(selected_file)

def one_search():
    if not file_selected:
        print('Вам необходимо выбрать файл для работы!')
        select_file()
    global selected_file
    print(selected_file)
    print('Выберите поле для поиска: ')
    print('(1) название (2) дата (3) участник (4) результат')
    while ValueError or AssertionError:
        try:
            i1 = str(input('Выберите поле: '))
            i = int(i1)
            assert 1 <= i and i <= 5
        except AssertionError:
            print('Введите число от 1 до 4')
        except ValueError:
            print('Введите целое число')
        else:
            break
    to_find = str(input('Записи с каким значением в этом поле вывести? '))
    f = open(selected_file, 'r')
    flag = False
    print('Найденные строки: ')
    for j in f:
        r = j.split(';')
        if r[i] == to_find:
            print('{0:^2s}|{1:^25s}|{2:^5s}|{3:^25s}|{4:^30s}'.format(r[0], r[1], r[2], r[3], r[4]))
            print('-' * 91)
            flag = True
    if flag == False:
        print('строки не найдены')


def two_search():
    if not file_selected:
        print('Вам необходимо выбрать файл для работы!')
        select_file()
    global selected_file
    print(selected_file)
    print('Выберите поле для поиска: ')
    print('(1) название (2) дата (3) участник (4) результат')
    while ValueError or AssertionError:
        try:
            i1 = str(input('Выберите поле: '))
            i = int(i1)
            assert 1 <= i and i <= 5
        except AssertionError:
            print('Введите число от 1 до 5')
        except ValueError:
            print('Введите целое число')
        else:
            break
    to_find = str(input('Записи с каким значением в этом поле вывести? '))
    print('Выберите поле для поиска: ')
    print('(1) название (2) дата (3) участник (4) результат')
    while ValueError or AssertionError:
        try:
            k1 = str(input('Выберите поле: '))
            k = int(k1)
            assert 1 <= k and k <= 4 and k != i
        except AssertionError:
            print('Введите число от 1 до 4, не равное значению первого поля')
        except ValueError:
            print('Введите целое число')
        else:
            break
    to_find1 = str(input('Записи с каким значением в этом поле вывести? '))
    f = open(selected_file, 'r')
    flag = False
    print('Найденные строки: ')
    for j in f:
        r = j.split(';')
        if r[i] == to_find and r[k] == to_find1:
            print('{0:^2s}|{1:^25s}|{2:^5s}|{3:^25s}|{4:^30s}'.format(r[0], r[1], r[2], r[3], r[4]))
            print('-' * 91)
            flag = True
    if flag == False:
        print('строки не найдены')


while True:
    print('Меню: ')
    print('1. Выбрать файл для работы')
    print('2. Инициализировать базу данных (создать либо перезаписать файл и заполнить его записями)')
    print('3. Вывести содержимое базы данных')
    print('4. Добавить запись в конец базы данных')
    print('5. Поиск по одному полю')
    print('6. Поиск по двум полям')
    print('7. Завершить программу')
    while ValueError or AssertionError:
        try:
            i1 = str(input('Выберите действие: '))
            i = int(i1)
            assert 1 <= i and i <= 7
        except AssertionError:
            print('Введите число от 1 до 7')
        except ValueError:
            print('Введите целое число')
        else:
            break
    if i == 7:
        raise SystemExit
    do_task(i)

