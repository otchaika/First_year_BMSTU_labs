# Силинг Екатерина. 9 лабораторная. задание 4
# Задана матрица D и массив I, содержащий номера строк, для которых необходимо определить максимальный элемент.
# Значения максимальных элементов запомнить в массиве R.
# Определить среднее арифметическое вычисленных максимальных значений.
# Напечатать матрицу D, массивы I и R, среднее арифметическое значение.
n = -1
while n != int(n) or n <= 1:
    n = float(input('Введите количество строк матрицы D: '))
n = int(n)
m = -1
while m != int(m) or m <= 1:
    m = float(input('Введите количество столбцов матрицы D: '))
m = int(m)
d = [[0] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        d[i][j] = float(input('Введите элемент {0} строки и {1} столбца: '.format(i + 1, j + 1)))
len_i = -1
while len_i < 1 or len_i != int(len_i):
    len_i = float(input('Введите длину массива I:'))
len_i = int(len_i)
I = [0] * len_i
for i in range(len_i):
    x = -1
    while x < 1 or x != int(x):
        x = float(input('Введите {0} элемент: '.format(i + 1)))
    I[i] = int(x)
print('Матрица D: ')
for i in range(n):
    print('{:3}-я строка: '.format(i + 1), end='')
    for j in range(m):
        print('{:12g} '.format(d[i][j]), end='')
    print()
print()
print('Массив I: ')
for i in range(len_i):
    print('{:12g} '.format(I[i]), end='')
print()
r = []
sum_max = 0
for i in range(len_i):
    max_el = None
    if I[i] <= n:
        k = I[i]-1
        for j in range(m):
            if max_el is None or d[k][j] > max_el:
                max_el = d[k][j]
        r.append(max_el)
        sum_max += max_el  # прибавляем максимальное к сумме
av = sum_max / len(r)
print('Массив R: ')
for i in range(len(r)):
    print('{:12g} '.format(r[i]), end='')
print()
print('Среднее арифметическое: ', av)
