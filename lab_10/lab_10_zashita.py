# Силинг Екатерина. Метод серединных прямоугольников
import math as m
def y(x):
    return m.sin(x)
def y1(x):
    return -(m.cos(x))
a = float(input('Введите начало отрезка: '))
b = float(input('Введите конец отрезка: '))
n = int(input('Введите количество участков разбиения: '))
def I(a, b, n):
    step = (b-a)/n
    x = a+step/2
    s = 0
    for i in range(n-1):
        s += y(x) * step
        x+=step
    return s
print('Интеграл, посчитанный методом серединных прямоугольников', I(a,b,n))

print('Интеграл от первообразной: ', y1(b)-y1(a))