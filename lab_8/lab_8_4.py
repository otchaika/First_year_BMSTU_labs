# 2 4
# Силинг Екатерина. Лабораторная 8, задание 4.
# Переставить местами столбцы с максимальной и минимальной суммой элементов.
# блок ввода
n = -1
while n != int(n) or n <=1:
    n = float(input('Введите количество строк: '))
n = int(n)
m = -1
while m != int(m) or m <=1:
    m = float(input('Введите количество столбцов: '))
m = int(m)
a = [[0]*m for i in range(n)]
for i in range(n):
    for j in range(m):
        a[i][j]=float(input('Введите элемент {0} строки и {1} столбца: '.format(i+1, j+1)))

# блок вычислений
max_sum=0  # максимальная сумма
min_sum=None  # манимальная сумма
max_j=-1  # индекс столбца с максимальной суммой
min_j=-1  # индекс столбца с минимальной суммой
for j in range(m):
    sum_el=0  # обнуление суммы элементов для нового столбца
    for i in range(n):
        sum_el+=a[i][j]
    if sum_el>max_sum:  # если сумма элементов больше наибольшей, меняем значение наибольшей
        max_sum=sum_el
        max_j=j
    elif min_sum is None or sum_el < min_sum:  # если сумма элементов больше наименьшей, меняем значение наименьшей
        min_sum=sum_el
        min_j=j
print('Начальная матрица: : ')
for i in range(n):
    print('{:3}-я строка: '.format(i+1), end='')
    for j in range(m):
        print('{:12g} '.format(a[i][j]),end='')
    print()
print()
if min_sum!=max_sum:
    for i in range(n):  # изменение порядка столбцов
        max_st=a[i][max_j]
        min_st=a[i][min_j]
        a[i][max_j]=min_st
        a[i][min_j]=max_st
    print('Итоговая матрица: ')
    for i in range(n):
        print('{:3}-я строка: '.format(i+1), end='')
        for j in range(m):
            print('{:12g} '.format(a[i][j]),end='')
        print()
else:  # если максимальная сумма элементов равна минимальной
    print('Матрица не изменится.')

