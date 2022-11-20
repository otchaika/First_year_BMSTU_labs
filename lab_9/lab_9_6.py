# Силинг Екатерина. Лабораторная 8, задание 6.
# Сформировать матрицу C путём построчного перемножения матриц A и B одинаковой размерности
# (элементы в i-й строке матрицы A умножаются на соответствующие элементы в i-й строке матрицы B),
# потом сложить все элементы в столбцах матрицы C и записать их в массив V. Напечатать матрицы A, B, C и массив V.

n = -1
while n != int(n) or n <= 1:
    n = float(input('Введите количество строк матрицы: '))
n = int(n)
m = -1
while m != int(m) or m <= 1:
    m = float(input('Введите количество столбцов матрицы: '))
m = int(m)
a = [[0] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        a[i][j] = float(input('Введите элемент {0} строки и {1} столбца матрицы А: '.format(i + 1, j + 1)))
b = [[0] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        b[i][j] = float(input('Введите элемент {0} строки и {1} столбца матрицы B: '.format(i + 1, j + 1)))
c = [[0] * m for i in range(n)]
v = [0] * m
# вычисления
for j in range(m):
    sum_el = 0
    for i in range(n):
        c[i][j] = a[i][j] * b[i][j]  # считаем жлементы в матрице С
        sum_el += c[i][j]
    v[j] = sum_el  # записываем сумму элементов столбца в массив
# блок печати
print('Матрица A: ')
for i in range(n):
    print('{:3}-я строка: '.format(i + 1), end='')
    for j in range(m):
        print('{:12g} '.format(a[i][j]), end='')
    print()
print()
print('Матрица B: ')
for i in range(n):
    print('{:3}-я строка: '.format(i + 1), end='')
    for j in range(m):
        print('{:12g} '.format(b[i][j]), end='')
    print()
print()
print('Матрица C: ')
for i in range(n):
    print('{:3}-я строка: '.format(i + 1), end='')
    for j in range(m):
        print('{:12g} '.format(c[i][j]), end='')
    print()
print()
print('Массив V: ')
for i in range(len(v)):
    print('{:12g} '.format(v[i]), end='')
print()
