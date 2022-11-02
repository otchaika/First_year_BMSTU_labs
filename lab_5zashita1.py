# Силинг Екатерина. Защита 5 лабораторной работы
# (-1)^n * (x + 1)^n / n!
x = float(input('Введите х: '))
eps = float(input('Введите точность: '))
n = 1
fact = 1
found = False
cur_y = -1 * (x + 1)
sum_y = cur_y
while abs(cur_y) > eps and not found:
    if abs(cur_y * (-1) * (x + 1) / n) < eps:
        found = True
        sum_y += cur_y
        break
    cur_y = cur_y * (-1) * (x + 1) / n
    n += 1
    sum_y += cur_y
    print(cur_y)
print('Последний член ряда: {0:5g}, сумма бесконечного ряда: {1:5g}'.format(cur_y, sum_y))
