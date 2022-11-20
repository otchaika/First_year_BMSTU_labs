# Силинг Екатерина. Защита 9. Дана квадратная целочисленная матрица. повернуть на 180 градусов
n = int(input('Введите размерность матрицы: '))
a = [[0]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        a[i][j]=int(input('Введите элемент {0} строки {1} столбца: '.format(i+1, j+1)))
print('Начальная матрица: ')
for i in range(n):
    for j in range(n):
        print('{:12g}'.format(a[i][j]), end='')
    print()
print()
for i in range(n//2):
    for j in range(n):
        a[i][j], a[n-i-1][n-j-1]=a[n-i-1][n-j-1], a[i][j]
print('Итоговая матрица: ')
for i in range(n):
    for j in range(n):
        print('{:12g}'.format(a[i][j]), end='')
    print()