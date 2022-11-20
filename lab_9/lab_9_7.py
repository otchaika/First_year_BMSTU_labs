# Силинг Екатерина. 9 Лабораторная. 7 задание
# Ввести трёхмерный массив (массив матриц размера X*Y*Z),
# вывести из него i-й срез (матрицу - фрагмент трёхмерного массива) по второму индексу
# (нумерация индексов начинается с 1)
p = -1
while p != int(p) or p <=1:
    p = float(input('Введите Х: '))
p = int(p)
n = -1
while n != int(n) or n <=1:
    n = float(input('Введите Y: '))
n = int(n)
m = -1
while m != int(m) or m <=1:
    m = float(input('Введите Z: '))
m = int(m)
d = [[[0]*m for i in range(n)]for k in range(p)]
for k in range(p):
    for i in range(n):
        for j in range(m):
            d[k][i][j]=float(input('Введите элемент {0} матрицы {1} строки и {2} столбца: '.format(k+1, i+1, j+1)))
for k in range(p):
    print(k+1, 'матрица: ')
    for i in range(n):
        print('{:3}-я строка: '.format(i + 1), end='')
        for j in range(m):
            print('{:12g} '.format(d[k][i][j]), end='')
        print()
    print()
ind=-1
while ind !=int(ind) or ind <0 or ind > m:
    ind = float(input('Введите i: '))
ind=int(ind)
print('Получившийся срез: ')
for k in range(p):
    for j in range(m):
        print('{:12g} '.format(d[k][ind-1][j]), end='')  # по нужному индексу выводим строки всех матриц
    print()

