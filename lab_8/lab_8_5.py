# Силинг Екатерина. Лабораторная 8, задание 5.
# Найти максимальное значение в квадратной матрице над главной диагональю и минимальное - под побочной диагональю.
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
max_nad = -1  # максимальное значение над побочной диагональю
min_pod = None  # минимальное значение под этой диагональю
for i in range(n):
    for j in range(n):
        if i > n - j - 1:
            if min_pod is None or a[i][j] < min_pod:  # для элементов под побочной диагональю
                min_pod = a[i][j]
        if i < n - j - 1:
            if a[i][j] > max_nad:  # для элементов над побочной диагональю
                max_nad = a[i][j]

# блок вывода
print('Максимальное значение над побочной диагональю: {:12g}'.format(max_nad))
print('Минимальное значение под побочной диагональю: {:12g}'.format(min_pod))
