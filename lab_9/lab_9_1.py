# Силинг Екатерина. 9 лабораторная. задание 1
import math as m

len_d = -1
while len_d < 0 or len_d != int(len_d):
    len_d = float(input('Введите длину массива d: '))
len_d = int(len_d)
d = [0] * len_d
for i in range(len_d):
    x = 0.1
    x = float(input('Введите {0} элемент: '.format(i + 1)))
    x = int(x)
    d[i] = x
len_d = -1
while len_d < 0 or len_d != int(len_d):
    len_d = float(input('Введите длину массива f: '))
len_d = int(len_d)
f = [0] * len_d
for i in range(len_d):
    x = 0.1
    x = float(input('Введите {0} элемент: '.format(i + 1)))
    x = int(x)
    f[i] = x
print('Массив d:')
for i in range(len(d)):
    print('{:12g}'.format(d[i]), end='')
print()
print('Массив f:')
for i in range(len(f)):
    print('{:12g}'.format(f[i]), end='')
print()

a = [[0] * len(f) for i in range(len(d))]

av = [0] * len(d)
l = [0] * len(d)
for i in range(len(d)):
    sum_stroki = 0  # сумма строки
    num_el = 0
    count = 0
    for j in range(len(f)):
        a[i][j] = m.sin(f[j] + d[i])  # записываем элемент в третью матрицу
        if a[i][j] > 0:
            sum_stroki += a[i][j]
            num_el += 1
    if num_el != 0:
        av[i] = sum_stroki / num_el  # считаем среднее арифметическое строки
    else:
        av[i] = 0
    for j in range(len(f)):
        if a[i][j] < av[i]:
            count += 1
    l[i] = count

# блок печати
print('Итоговая матрица: ')
for j in range(len(f)):
    print('{0:2}-й столбец'.format(j + 1), end=' ')
print('     av     ', end=' ')
print('     l      ')
print()
for i in range(len(d)):
    for j in range(len(f)):
        print('{:12g}'.format(a[i][j]), end=' ')
    if av[i] != 0:
        print('{:12g}'.format(av[i]), end='')
    elif av[i] == 0:
        print('      -     ', end='')
    print('{:12g}'.format(l[i]))
    print()
