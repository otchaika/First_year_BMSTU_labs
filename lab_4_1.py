# Силинг Екатерина. Вариант 16. График 2-й функции. Этот код выводит таблицу значений двух функций при заданных начального аргумента, конечного аргумента и шага.
# печатает максимальное значение третьей функции и аргумент, при котором оно достигается
# далее для одной из функций программа выводит график значений при заданном количестве засечек

import math

# блок ввода
x1 = float(input('Введите первое значение аргумента: '))
xi = float(input('Введите последнее значение аргумента: '))
step = float(input('Введите шаг для разбиения: '))
# проверка корректности ввода
while x1 >= xi or step <= 0 or step > (xi - x1):
    print('Конечное значение должно быть больше начального, а шаг больше 0 и меньше промежутка')
    x1 = float(input('Введите корректно первое значение аргумента: '))
    xi = float(input('Введите корректно последнее значение аргумента: '))
    step = float(input('Введите корректно шаг для разбиения: '))

line_len = 160  # ширина графика
eps = 1e-8  # константа, хранящая значение эпсилон
n = int(input('Введите количество засечек: '))  # notches - константа хранящая количество
# засечек на оси ординат в графике функции.

# Ищем максимальное и минимальное значение функции y, на заданном отрезке и строим таблицу
y_max = None  # максимальное значение функции y, на заданном отрезке

y_min = None  # минимальное значение функции y, на заданном отрезке
x_max_len = 0  # максимальная длина числа x.
y3_max = None  # минимальное значение функции y3, на заданном отрезке
x3_max = None
cur_x = x1 -step # cur_х - переменная хранящая текущее значение аргумента.
# печать верхней части таблицы
print('-' * 43)
print('|    {0:7} '.format('x'), '|     {0:6} '.format('y1'), '|      {0:6} |'.format('y2'))
print('|', '-' * 41)

# подсчет значений функций при изменяющемся аргументе

while  cur_x +step<= xi+eps:
    cur_x += step
    if abs(cur_x) < eps:
        cur_x = 0.0
    y = 2 * (cur_x ** 3) + 3 * (cur_x ** 2) - 6 * cur_x + 1.5  # Вычисляем значение функции y, при x = cur_val.
    y1 = cur_x * (2 ** cur_x) - 1  # первая функция
    y1y2 = y * y1
    y3 = math.copysign(abs(y1y2) ** (1 / 3), y1y2)  # третья функция
    x = '{:.7g}'.format(cur_x)  # Приводим значение переменной cur_val к типу str, сохраняя только 7 значащих цифр, и
    # записываем полученное значение в переменную x.
    print('|{0:12.2}'.format(cur_x), '|{0:12.5g}'.format(y1), '|{0:12.5g} |'.format(y))  # печать одной строки таблицы
    # нахождение максимальных и минимальных значений функции, график которой мы выведем

    if y_max is None or y_max <= y:
        y_max = y  # Присваиваем y_max значение y, если y больше y_max, или если y_max имеет значение None.

    if y_min is None or y_min >= y:
        y_min = y  # Присваиваем y_min значение y, если y меньше y_max, или если y_max имеет значение None.
    if y3_max is None or y3_max <= y3:
        y3_max = y3
        x3_max = x
    x_max_len = max(x_max_len, len(x))  # сохраняем максимальную длину x
print(y3_max, x3_max)
print('-' * 43)
print('Максимальное значение третьей функции {0:.5}, оно достигается при аргументе {1:.5}'.format(y3_max, x3_max))
# Ищем дельту между засечками:
delta = .0  # delta - переменная хранящая дельту между засечками. По умолчанию равна 0.

# delta принимает значение разности максимального и минимального значений функции
# поделенного на количество засечек - 1.
if not (abs(y_max - y_min) <= eps):
    delta = abs(y_max - y_min) / (n - 1)
gr_col_wid = (line_len - len('{:.7g}'.format(y_max)) - x_max_len) // (
            n - 1)  # gr_col_wid - переменная, хранящая ширину засечки в графике фнукции.

print('График функции y = 2* x^3+3* x^2-6*x+1.5')
print(' ' * x_max_len, '|', sep='', end='')
# Выводим ось ординат:
i = 0  # i - переменная счетчик засечек.
while i < n - 1:
    cur_x = y_min + (delta * i)  # cur_x - переменная хранящая текущее значение функции.
    cur_x = '{:.7g}'.format(cur_x)  # Приводим значение переменной cur_x к типу str,
    # сохраняя только 7 значащих цифр.
    print(cur_x, ' ' * (gr_col_wid - len(cur_x)), sep='', end='')
    i += 1
print('{:.7g}'.format(y_max))

# Выводим ось абсцисс и сами точки
cur_x = x1 - step  # cur_x - переменная хранящая текущее значение аргумента.
while cur_x +step<= xi+eps:
    cur_x += step
    if abs(cur_x) < eps:
        cur_x = 0.0
    y = 2 * (cur_x ** 3) + 3 * (cur_x ** 2) - 6 * cur_x + 1.5  # Вычисляем значение функции y, при x = cur_x.
    x = '{:.7g}'.format(cur_x)  # Приводим значение переменной cur_x к типу str, сохраняя только 7 значащих цифр, и
    # записываем полученное значение в переменную x.
    print(x, ' ' * (x_max_len - len(x)), '|', sep='', end='')
    i = 0  # счетчик засечек
    n1 = y_min  # перменная храянящая значение текущей клетки
    ndelta = delta / gr_col_wid  # ndelta - дельта между клетками
    while i < n:
        j = 0  # i - переменная счетчик клеток в засечке
        while j < gr_col_wid:
            if n1 <= y < n1 + ndelta:
                print('*', sep='', end='')
            elif n1 <= 0 < n1 + ndelta:
                print('|', sep='', end='')
            else:
                print(' ', sep='', end='')
            n1 += ndelta
            if i == n - 1:
                break
            j += 1
        i += 1
    print()