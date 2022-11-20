# Силинг Екатерина. 9 лабораторная. задание 2
# Повернуть квадратную целочисленную матрицу на 90 градусов по часовой стрелке,
# затем на 90 градусов против часовой стрелки. Вывести исходную, промежуточную и итоговую матрицы.
# Дополнительных матриц и массивов не вводить. Транспонирование не применять.
n = -1
while n != int(n) or n <= 1:
    n = float(input('Введите количество строк, равное количеству столбцов: '))
n = int(n)
a = [[0] * n for i in range(2 * n)]  # создаем матрицу, в которой в два раза больше строк, чем нужно
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
for i in range(n):
    for j in range(n):
        a[j + n][n - i - 1] = a[i][j]  # вниз матрицы на соответствующие места записываем элемент
for i in range(n):
    a.pop(0)
print('Повернутая на 90 градусов: ')
for i in range(n):
    print('{:3}-я строка: '.format(i + 1), end='')
    for j in range(n):
        print('{:12g} '.format(a[i][j]), end='')
    print()
print()
for i in range(n):
    a.append([0] * n)  # добавляем строки вниз
for i in range(n):
    for j in range(n):
        a[2 * n - j - 1][i] = a[i][j]  # совершаем обратное действие
for i in range(n):
    a.pop(0)
print('Повернутая на 90 градусов обратно: ')
for i in range(n):
    print('{:3}-я строка: '.format(i + 1), end='')
    for j in range(n):
        print('{:12g} '.format(a[i][j]), end='')
    print()
print()
