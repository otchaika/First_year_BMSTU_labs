# Защита лабораторной 8
# Силинг Екатерина дана целочисленная матрица, найти максимальный элемент матрицы, обнулить строки и столбцы,
# на пересечении которых стоит значение, совпадающее с максимумом, сами элементы тоже обнулить
n = int(input('Введите количество строк: '))
m = int(input('Введите количество столбцов: '))
a = [[0]*m for i in range(n)]
for i in range(n):
    for j in range(m):
        a[i][j] = int(input('Введите элемент {0} строки {1} столбца: '.format(i+1,j+1)))

print('Начальная матрица: ')
for i in range(n):
    for j in range(m):
        print('{0:12g}'.format(a[i][j]), end=' ')
    print()
print()
max_arr=[[None, -1, -1]]
for i in range(n):
    for j in range(m):
        if max_arr[-1][0] is None or a[i][j]>max_arr[-1][0]:
            max_arr = [[None, -1, -1]]
            max_arr.append([a[i][j], i, j])
        elif a[i][j]==max_arr[-1][0]:
            max_arr.append([a[i][j], i, j])
for k in range(1,len(max_arr)):
    i = max_arr[k][1]
    j = max_arr[k][2]
    for jj in range(m):
        a[i][jj]=0
    for ii in range(n):
        a[ii][j]=0
print('Итоговая матрица: ')
for i in range(n):
    for j in range(m):
        print('{0:12g}'.format(a[i][j]), end=' ')
    print()
print()
