# Силинг Екатерина. Эта программа по координатам вершин треугольника выводит длину высоты из наибольшего угла
from math import sqrt

# блок ввода

x1 = float(input('Введите Х координату первой точки: '))
y1 = float(input('Введите У координату первой точки: '))
x2 = float(input('Введите Х координату второй точки: '))
y2 = float(input('Введите У координату второй точки: '))
x3 = float(input('Введите Х координату третьей точки: '))
y3 = float(input('Введите У координату третьей точки: '))
# находим длины сторон и наибольшую
a = abs(sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))
b = abs(sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2))
c = abs(sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2))
max_side = max(a, b, c)
# вычисляем полупериметр и площадь
p = (a + b + c) / 2
S = sqrt(p * (p - a) * (p - b) * (p - c))
# уравнение длины высоты выводится через уравнение площади (s = 0.5*h*a)
hight = 2 * S / max_side
print('Высота из наибольшего угла равна: {0:.7f}'.format(hight))
