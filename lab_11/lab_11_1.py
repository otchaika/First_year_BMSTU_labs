# Силинг Екатерина. Лабораторная 11Написать программу для демонстрации работы метода сортировки (по варианту)
# на примере массива целых чисел.
# сортировка методом простого выбора
import time
import random


def create_table_hat():  # функция печатает шапку итоговой таблицы
    print('╔{0}╦{1}╦{1}╦{1}╗'.format('═' * 35, '═' * 25))
    print('║ ', ' ' * 32, '║{:^25s}║'.format('N1'), '{:^24s}║'.format('N2'), '{:^24s}║'.format('N3'))
    print('║ {0}╠{1}╦{2}╬{1}╦{2}╬{1}╦{2}║'.format(' ' * 34, '═' * 15, '═' * 9))
    print('║', ' ' * 33, '║{:^15s}║'.format('t'), '{:^8s}║'.format('k'), end='')
    print('{:^15s}║'.format('t'), '{:^8s}║'.format('k'), end='')
    print('{:^15s}║'.format('t'), '{:^8s}║'.format('k'))
    print('╠{0}╬{1}╬{2}╬{1}╬{2}╬{1}╬{2}╣'.format('═' * 35, '═' * 15, '═' * 9))


def simple_sort(arr1):  # функция получает на ввод массив и его длину, выводит время обработки, перестановки и итог
    t1_1 = time.time()
    c = 0
    a = arr1[:]
    for i in range(len(a)):  # сортировка списка
        ind = None
        for j in range(i + 1, len(a)):
            if ind is None or a[j] < a[ind]:
                ind = j
        if ind is not None and a[ind] < a[i]:
            a[i], a[ind] = a[ind], a[i]
            c += 1
    t1_2 = time.time()
    t1 = t1_2 - t1_1
    return t1, c, a


def create_random(n):  # функция получает на ввод длину массива и выводит случайный массив из чисел от 0 до 9
    arr = []
    for i in range(n):
        arr.append(random.randint(0, 9))
    return arr


def create_sorted(n):  # функция получает на ввод дляну массива и выводит отсортированный массив
    arr = []
    for i in range(n):
        arr.append(i)
    return arr


def create_sorted_back(n):  # функция получает на ввод длину массива и выводит обратно отсортированный массив
    arr = []
    for i in range(n):
        arr.append(n - i)
    return arr


def calculate(n1, n2, n3):  # функция получает на ввод три длины массива, создает на каждую n по массиву каждого типа
    # и выводит в двухмерным массив t и k
    ns = [n1, n2, n3]
    results = []  # массив, содержащий t и k для каждого списка
    for i in range(len(ns)):
        n = ns[i]
        b = create_random(n)
        t1 = simple_sort(b)[0]
        k1 = simple_sort(b)[1]
        c = create_sorted(n)
        t2 = simple_sort(c)[0]
        k2 = simple_sort(c)[1]
        d = create_sorted_back(n)
        t3 = simple_sort(d)[0]
        k3 = simple_sort(d)[1]
        results.append([t1, k1])
        results.append([t2, k2])
        results.append([t3, k3])
    return results


# блок ввода со всеми проверками
while ValueError or AssertionError:
    try:
        N = str(input('Введите размерность списка: '))
        n = int(N)
        assert n > 0
    except AssertionError:
        print('Число должно быть больше 0')
    except ValueError:
        print('Введите целое число')
    else:
        break
a = []
for i in range(n):
    while ValueError:
        try:
            A = str(input('Введите {0}-й элемент списка: '.format(i + 1)))
            s = int(A)
        except ValueError:
            print('Введите целое число')
        else:
            break
    a.append(s)

a_sorted = simple_sort(a)
print('Отсортированный массив: ', *(a_sorted[2]))
print('Он вычислен за {0} секунд и за {1} перемещений'.format('{:7g}'.format(a_sorted[0]), a_sorted[1]))

while ValueError or AssertionError:
    try:
        N1 = str(input('Введите N1: '))
        n1 = int(N1)
        assert n1 > 0
    except AssertionError:
        print('Число должно быть больше 0')
    except ValueError:
        print('Введите число')
    else:
        break
while ValueError or AssertionError:
    try:
        N2 = str(input('Введите N2: '))
        n2 = int(N2)
        assert n2 > 0
    except AssertionError:
        print('Число должно быть больше 0')
    except ValueError:
        print('Введите число')
    else:
        break
while ValueError or AssertionError:
    try:
        N3 = str(input('Введите N3: '))
        n3 = int(N3)
        assert n3 > 0
    except AssertionError:
        print('Число должно быть больше 0')
    except ValueError:
        print('Введите число')
    else:
        break

arr = calculate(n1, n2, n3)  # подсчет нужного нам массива

# печать таблицы

create_table_hat()
print('║{:35s}║'.format('Cлучайный список'), end='')
print('{:^15s}║'.format('{:7g}'.format(arr[0][0])), '{:^8s}║'.format('{:7g}'.format(arr[0][1])), end='')
print('{:^15s}║'.format('{:7g}'.format(arr[3][0])), '{:^8s}║'.format('{:7g}'.format(arr[3][1])), end='')
print('{:^15s}║'.format('{:7g}'.format(arr[6][0])), '{:^8s}║'.format('{:7g}'.format(arr[6][1])))
print('╠{0}╬{1}╬{2}╬{1}╬{2}╬{1}╬{2}╣'.format('═' * 35, '═' * 15, '═' * 9))
print('║{:35s}║'.format('Упорядоченный список'), end='')
print('{:^15s}║'.format('{:7g}'.format(arr[1][0])), '{:^8s}║'.format('{:7g}'.format(arr[1][1])), end='')
print('{:^15s}║'.format('{:7g}'.format(arr[4][0])), '{:^8s}║'.format('{:7g}'.format(arr[4][1])), end='')
print('{:^15s}║'.format('{:7g}'.format(arr[7][0])), '{:^8s}║'.format('{:7g}'.format(arr[7][1])))
print('╠{0}╬{1}╬{2}╬{1}╬{2}╬{1}╬{2}╣'.format('═' * 35, '═' * 15, '═' * 9))
print('║{:35s}║'.format('Обратно отсортированный список'), end='')
print('{:^15s}║'.format('{:7g}'.format(arr[2][0])), '{:^8s}║'.format('{:7g}'.format(arr[2][1])), end='')
print('{:^15s}║'.format('{:7g}'.format(arr[5][0])), '{:^8s}║'.format('{:7g}'.format(arr[5][1])), end='')
print('{:^15s}║'.format('{:7g}'.format(arr[8][0])), '{:^8s}║'.format('{:7g}'.format(arr[8][1])))
print('╚{0}╩{1}╩{2}╩{1}╩{2}╩{1}╩{2}╝'.format('═' * 35, '═' * 15, '═' * 9))
