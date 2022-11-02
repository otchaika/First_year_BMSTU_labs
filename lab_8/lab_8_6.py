# Силинг Екатерина. Лабораторная 8, задание 6.
# Выполнить транспонирование квадратной матрицы.
# блок ввода
n = -1
while n != int(n) or n <= 1:
    n = float(input('Введите количество строк, равное количеству столбцов: '))
n = int(n)
a = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        a[i][j] = float(input('Введите элемент {0} строки и {1} столбца: '.format(i + 1, j + 1)))
print('Начальная матрица: ')
for i in range(n):
    print('{:3}-я строка: '.format(i + 1), end='')
    for j in range(n):
        print('{:12g} '.format(a[i][j]), end='')
    print()
print()

# блок вычислений
for i in range(n):
    for j in range(i + 1, n):
        a[i][j], a[j][i] = a[j][i], a[i][j]  # замена элемента на соответствующий

# блок печати
print('Транспонированная матрица: ')
for i in range(n):
    print('{:3}-я строка: '.format(i + 1), end='')
    for j in range(n):
        print('{:12g} '.format(a[i][j]), end='')
    print()
