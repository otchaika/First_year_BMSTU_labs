# Силинг Екатерина. 9 лабораторная. задание 3
# Подсчитать в каждой строке матрицы D количество элементов,
# превышающих суммы элементов соответствующих строк матрицы Z.
# Разместить эти количества в массиве G, умножить матрицу D на максимальный элемент массива G.
# Напечатать матрицу Z, матрицу D до и после преобразования, а также массив G.
n = -1
while n != int(n) or n <= 1:
    n = float(input('Введите количество строк матрицы D и Z: '))
n = int(n)
nd=n
m = -1
while m != int(m) or m <= 1:
    m = float(input('Введите количество столбцов матрицы D: '))
m = int(m)
d = [[0] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        d[i][j] = float(input('Введите элемент {0} строки и {1} столбца: '.format(i + 1, j + 1)))
md = m
m = -1
nz=n
while m != int(m) or m <= 1:
    m = float(input('Введите количество столбцов матрицы Z: '))
m = int(m)

z = [[0] * m for i in range(n)]
for i in range(nz):
    for j in range(m):
        z[i][j] = float(input('Введите элемент {0} строки и {1} столбца: '.format(i + 1, j + 1)))
mz = m
nz = n
g = []
print('Матрица Z:')
for i in range(nz):
    print('{:3}-я строка: '.format(i + 1), end='')
    for j in range(mz):
        print('{:12g} '.format(z[i][j]), end='')
    print()
print()
print('Начальная матрица D:')
for i in range(nd):
    print('{:3}-я строка: '.format(i + 1), end='')
    for j in range(md):
        print('{:12g} '.format(d[i][j]), end='')
    print()
print()
max_count = -1
for i in range(nd):
    sum_str_z = 0
    count = 0
    for j in range(mz):
        if i <=nz:
            sum_str_z += z[i][j]  # записываем все элементы строки матрицы в сумму

    for j in range(md):
        if d[i][j] > sum_str_z:  # считаем котичество элементов больше суммы строки
            count += 1
    g.append(count)
    if count > max_count:
        max_count = count
if max_count != -1:
    for i in range(nd):
        for j in range(md):
            d[i][j] = max_count * d[i][j]  # перезаписываем матрицу
# блок печети
print('Итоговая матрица D:')
for i in range(nd):
    print('{:3}-я строка: '.format(i + 1), end='')
    for j in range(md):
        print('{:12g} '.format(d[i][j]), end='')
    print()
print()
print('Массив G:')
for i in range(len(g)):
    print('{:12g}'.format(g[i]), end='')
