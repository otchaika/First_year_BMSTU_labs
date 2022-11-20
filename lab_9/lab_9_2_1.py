# Силинг Екатерина. 9 лабораторная. задание 2
# Повернуть квадратную целочисленную матрицу на 90 градусов по часовой стрелке,
# затем на 90 градусов против часовой стрелки. Вывести исходную, промежуточную и итоговую матрицы.
# Дополнительных матриц и массивов не вводить. Транспонирование не применять.
n = -1
while n != int(n) or n <= 1:
    n = float(input('Введите количество строк, равное количеству столбцов: '))
n = int(n)
a = [[0] * n for i in range(n)]  # создаем матрицу, в которой в два раза больше строк, чем нужно
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
for i in range(0, n//2):
    for j in range(i, n-1):
        a[i][j], a[j][-i-1], a[-i-1][-j-1], a[-j-1][i]= a[-j-1][i], a[i][j], a[j][-i-1], a[-i-1][-j-1]

print('Повернутая на 90 градусов: ')
for i in range(n):
    print('{:3}-я строка: '.format(i + 1), end='')
    for j in range(n):
        print('{:12g} '.format(a[i][j]), end='')
    print()
print()
for i in range(0, n//2):
    for j in range(i, n-1):
        a[i][j], a[j][-i-1], a[-i-1][-j-1], a[-j-1][i]= a[j][-i-1], a[-i-1][-j-1], a[-j-1][i], a[i][j]
print('Повернутая на 90 градусов обратно: ')
for i in range(n):
    print('{:3}-я строка: '.format(i + 1), end='')
    for j in range(n):
        print('{:12g} '.format(a[i][j]), end='')
    print()
print()