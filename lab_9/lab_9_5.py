# Силинг Екатерина. 9 лабораторная. задание 5
# Дана матрица символов. Заменить в ней все гласные английские буквы на точки.
# Напечатать матрицу до и после преобразования.
n = -1
while n != int(n) or n <= 1:
    n = float(input('Введите количество строк матрицы: '))
n = int(n)
m = -1
while m != int(m) or m <= 1:
    m = float(input('Введите количество столбцов матрицы: '))
m = int(m)
d = [[0] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        x = 'er'
        while len(x) > 1:
            x = input('Введите элемент {0} строки и {1} столбца: '.format(i + 1, j + 1))
        d[i][j] = x
print('Матрица D: ')
for i in range(n):
    print('{:3}-я строка: '.format(i + 1), end='')
    for j in range(m):
        print('{0} '.format(d[i][j]), end='')
    print()
print()
gl = 'EYUIOAeyuioa'
for i in range(n):
    for j in range(m):
        if d[i][j] in gl:  # если символ - гласная, заменяем его на точку
            d[i][j] = '.'
# блок печати
print('Матрица D: ')
for i in range(n):
    print('{:3}-я строка: '.format(i + 1), end='')
    for j in range(m):
        print('{0} '.format(d[i][j]), end='')
    print()
print()
