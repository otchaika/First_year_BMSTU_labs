# Силинг Екатерина
x1=float(input('Введите начальное значение аргумента: '))
xi=float(input('Введите конечное значение аргумента: '))
step=float(input('Введите шаг: '))
x=x1-step
import math as m
y_min=None
y_max=None
eps=1e-7
while x <=xi-step:
    x+=step
    if abs(x)<eps:
        x=0.0
    y=m.tan(x/2)
    if y_min==None or y <y_min:
        y_min=y
    if y_max==None or y > y_max:
        y_max=y
width=150

y_range=y_max-y_min
y_min='{:.7f}'.format(y_min)
print(' '*12,y_min, ' '* (width-13-len(y_min)), '{:.7f}'.format(y_max))
x=x1-step
while x <=xi-step:
    x+=step
    if abs(x)<eps:
        x=0.0
    i=0
    y=m.tan(x/2)
    n1=float(y_min)-eps
    ndelta=y_range/(width-12)
    print('{:12.7g}|'.format(x),end='')
    while i <=(width-12):
        if n1<=y<=n1+ndelta:
            print('*', sep='', end='')
        elif n1<0<=n1+ndelta:
            print('|', sep='', end='')
        else:
            print(' ', sep='', end='')
        n1+=ndelta
        i+=1
    print()