
import struct
import numpy as np
selected_file = 'main_file.bin'

f = open('main_file.bin', 'wb')
f.write(bytes('fdsfgfds gfds', encoding='utf-8'))
f.close()
print(open('main_file.bin', 'r').read())

b_num=0
def append_db():
    global selected_file
    print(selected_file)
    index = int(input('Введите номер строки, куда вы хотите начать записывать новые данные: '))
    str_i = int(input('Введите количество записей, которые вы хотите добавить: '))
    my_file = open(selected_file, "wb+")
    my_file.seek(b_num*(index))
    print(my_file.read(0))
    cur_str=my_file
    print_db(selected_file)
def print_db(file):
    f = open(file, 'rb')
    print('Файл:')
    print('{0:15s}|{1:15s}|{2:15s}|{3:15s}'.format('НАЗВАНИЕ', 'ДАТА', 'УЧАСТНИКИ', 'результат'))
    print('-' * 91)
    with open(file, 'rb') as f:
        a = f.read(1)
        print(a)
        g = a.decode('utf-8')
        print(g,'helle', end='')
        lenn=1
        while a != b'':
            a = f.read(1)
            print(a)
            g = a.decode('utf-8')
            print(g,'hello', end='')
            lenn+=1
        print(lenn)

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
    i2 = str(i2)+ ' '* (15-len(str(i2)))
    i3 += ' ' * (15 - len(i3))
    i4 += ' ' * (15 - len(i4))
    string_to_add=struct.pack('15si15s15s', i1, i2, i3, i4)
    return string_to_add
print_db('main_file.bin')