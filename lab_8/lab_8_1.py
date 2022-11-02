# Силинг Екатерина. Лабораторная 8, задание 1. Вариант 2.
# Найти строку с наибольшим количеством подряд идущих одинаковых элементов.
# блок ввода
n = -1
while n != int(n) or n <= 1:
    n = float(input('Введите количество строк: '))
n = int(n)
m = -1
while m != int(m) or m <= 1:
    m = float(input('Введите количество столбцов: '))
m = int(m)
a = [[0] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        a[i][j] = float(input('Введите элемент {0} строки и {1} столбца: '.format(i + 1, j + 1)))
print('Начальная матрица: : ')
for i in range(n):
    print('{:3}-я строка: '.format(i + 1), end='')
    for j in range(m):
        print('{:12g} '.format(a[i][j]), end='')
    print()
print()

# блок вычислений
max_count = 0
max_i = -1
count = 0  # счетчик элементов в последовательность
for i in range(n):
    count = 0
    for j in range(1, m):
        if count > max_count:
            max_count = count
            max_i = i
        if a[i][j - 1] == a[i][j]:  # если настоящий элемент равен предыдущему, добавляем 1 к счетчику
            count += 1
        else:
            count = 0
    if count > max_count:
        max_count = count
        max_i = i

# блок печати
if max_i > -1:
    print('Строка: ', end='')
    for j in range(m):
        print('{:12g}'.format(a[max_i][j]), end=' ')
else:
    print('Нет таких строк.')
