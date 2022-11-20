# правый прямоугольник
def y(x):  # основная функция
    return 2*x


def y1(x):  # первообразная функции
    return x**2


# алгоритм для создания таблицы значений
def table(i1, i2, i3, i4):
    print('-' * 68)
    print(' ' * 30, '|', ' ' * 6, 'N1', ' ' * 6, '|', ' ' * 6, 'N2')
    print('-' * 68)
    print('Методом правых прямоугольников |', '{:^15s}'.format('{:.7g}'.format((i1))), ' |', \
          '{:^15s}'.format('{:.7g}'.format((i2))), ' ')
    print('Методом трапеций ', ' ' * 12, '|', '{:^15s}'.format('{:.7g}'.format((i3))), ' |', \
          '{:^15s}'.format('{:.7g}'.format((i4))), ' ')
    print('-' * 68)
    print()


# рассчет интеграла методом правых прямоугольников
def I1(a, b, n):
    step = (b - a) / n
    x = a
    S1 = 0
    for i in range(n):
        if y(x) is None:
            return None
        else:
            x += step
            if y(x) is None:
                return None
            else:
                S1 += y(x) * step
    return S1


# рассчет интеграла методом трапеций
def I2(a, b, n):
    x = a
    S2 = 0
    step = (b - a) / n
    for i in range(n):
        if y(x) is None:
            return None
        else:
            f1 = y(x)
            x += step
            f2 = y(x)
            if y(x) is None:
                return None
            else:
                S2 += (f1 + f2) * step / 2
    return S2

# серия проверок на правильный ввод значений

while ValueError:
    try:
        a1 = str(input('Введите начало отрезка: '))
        a = float(a1)
    except ValueError:
        print('Ошибка! Введите числовое значение')
    else:
        break
while ValueError or AssertionError:
    try:
        b1 = str(input('Введите конец отрезка: '))
        b = float(b1)
        assert b1 > a1
    except ValueError:
        print('Ошибка! Введите числовое значение')
    except AssertionError:
        print('Ошибка! Конец должен быть больше начала. Введите число больше', a1)
    else:
        break
while ValueError or AssertionError:
    try:
        N1 = str(input('Введите N1 (количество участков разбиения): '))
        n1 = int(N1)
        assert n1 > 0
    except ValueError:
        print('Ошибка! Введите числовое значение')
    except AssertionError:
        print('Ошибка! Введите число больше 0')
    else:
        break
while ValueError or AssertionError:
    try:
        N2 = str(input('Введите N2 (количество участков разбиения): '))
        n2 = int(N2)
        assert n2 > 0
    except ValueError:
        print('Ошибка! Введите числовое значение')
    except AssertionError:
        print('Ошибка! Введите число больше 0')
    else:
        break
while ValueError:
    try:
        eps1 = str(input('Введите точность: '))
        eps = float(eps1)
    except ValueError:
        print('Ошибка! Введите числовое значение')
    else:
        break
if y1(b) is not None and y1(a) is not None:
    integral = y1(b) - y1(a)  # интеграл, посчитанный с помощью первообразной
else:
    integral = None
S1n1 = I1(a, b, n1)  # метод 1, n1
S1n2 = I1(a, b, n2)  # метод 1, n2
# трапеция
S2n1 = I2(a, b, n1)  # метод 2, n1
S2n2 = I2(a, b, n2)  # метод 2, n2
if isinstance(S1n1, complex) or isinstance(S1n2, complex) or isinstance(integral, complex):
    # если один из интегралов - комплексное число (то есть введен отрезок, не входящий в ОДЗ
    print('Значение интеграла - комплексное число.')
    raise SystemExit
if S1n1 is None or S1n2 is None or S2n1 is None or S2n2 is None or integral is None:  # проверка на деление на 0
    print('Произошло деление на 0, программа завершена.')
    raise SystemExit
table(S1n1, S1n2, S2n1, S2n2)  # печать таблицы интегралов
print('Вычисленный интеграл от первообразной: ', integral)
# подсчет абсолютных погрешностей
abs_1_1 = abs(integral - S1n1)
abs_1_2 = abs(integral - S1n2)
abs_2_1 = abs(integral - S2n1)
abs_2_2 = abs(integral - S2n2)
print('Таблица абсолютных погрешностей методов: ')
print()
table(abs_1_1, abs_1_2, abs_2_1, abs_2_2)  # печать таблицы абсолютных погрешностей
# подсчет относительных погрешностей
otn_1_1 = abs_1_1 / integral
otn_1_2 = abs_1_2 / integral
otn_2_1 = abs_2_1 / integral
otn_2_2 = abs_2_2 / integral
print('Таблица относительных погрешностей методов: ')
print()
table(otn_1_1, otn_1_2, otn_2_1, otn_2_2)  # печать таблицы относительных погрешностей
# находжение минимальных абсолютных погрешностей обоих методов
abs_1 = min(abs_1_1, abs_1_2)
abs_2 = min(abs_2_1, abs_2_2)
if abs_2 <= abs_1:  # если метод трапеций более точен, считаем методом прамоугольников
    n = 1
    print('Более точен метод трапеций')
    while abs(I1(a, b, n) - I1(a, b, 2 * n)) >= eps:
        n *= 2
if abs_2 > abs_1:  # если метод прямоугольников более точен, считаем методом трапеций
    n = 1
    print('Более точен метод правых прямоугольников')
    while abs(I2(a, b, n) - I2(a, b, 2 * n)) >= eps:
        n*=2
print('Точность', eps, 'можно достичь за', n, 'операций')