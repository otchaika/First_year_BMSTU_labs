# 2 4
# Силинг Екатерина. Лабораторная 8, задание 2.
# Переставить местами строки с наибольшим и наименьшим количеством отрицательных элементов.
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

min_count_neg = None  # минимальное количество отрицательных
max_count_neg = 0  # максимальное количество отрицательных
neg_i = -1  # индекс строки с минимальным количеством отрицательных
pos_i = -1  # индекс строки с максимальным количеством отрицательных
for i in range(n):
    count_neg = 0  # количество отрицательных в строке
    for j in range(m):
        if a[i][j] < 0:
            count_neg += 1
    if min_count_neg is None or count_neg < min_count_neg:  # если в строке больше минимального кол-ва отрицательных
        min_count_neg = count_neg
        neg_i = i
    if count_neg > max_count_neg:  # если в строке больше максимального количества отрицательных значений
        max_count_neg = count_neg
        pos_i = i

if a[neg_i] != a[pos_i]:  # замена строк
    neg_str = a[neg_i]
    pos_str = a[pos_i]
    a[pos_i] = neg_str
    a[neg_i] = pos_str
    print('Итоговая матрица: ')
    for i in range(n):  # построчная печать
        print('{:3}-я строка: '.format(i + 1), end='')
        for j in range(m):
            print('{:12g} '.format(a[i][j]), end='')
        print()
else:
    print('Матрица не изменится.')
