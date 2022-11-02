# 2 4
# Силинг Екатерина. Лабораторная 8, задание 3. Вариант 4
# найти столбец с наибольшим количеством нулевых элементов.
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
print('Начальная матрица: ')
for i in range(n):
    print('{:3}-я строка: '.format(i + 1), end='')
    for j in range(m):
        print('{:12g} '.format(a[i][j]), end='')
    print()
print()

# блок вычислений
max_count = 0
max_j = -1
for j in range(m):
    count = 0
    for i in range(n):
        if a[i][j] == 0:  # подсчет нулевых элементов
            count += 1
    if count > max_count:
        max_count = count
        max_j = j

# блок вывода
if max_j != -1:
    print('Столбец с максимальным количеством нулевых элементов ({}-й столбец): '.format(max_j + 1))
    for i in range(n):
        print('{:12g}'.format(a[i][max_j]))
else:
    print('Подходящего столбца нет.')
