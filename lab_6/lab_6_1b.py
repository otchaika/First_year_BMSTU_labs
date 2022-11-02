# Силинг Екатерина. 6 лабораторная

len_a=-1
while len_a <0 or len_a!=int(len_a):
    len_a=float(input('Введите длину списка: '))
len_a=int(len_a)
a = [0]*len_a
for i in range(len_a):
    x=0.1
    while x != int(x):
        x = float(input('Введите {0} элемент: '.format(i+1)))
    x = int(x)
    a[i]=x
# 1b Добавить элемент в заданное место списка (по индексу) алгоритмически

index = -1
while index < 0 or index > len(a):
    index = int(input('Введите индекс места, куда нужно добавить элемент: '))
N = int(input('Введите значение элемента: '))
a1 = a[:]
a1.append(0) # добавляем элемент в конец списка
i = index + 1
i = len(a1) - 1
while i > index: # с конца начинаем сдвигать элементы вправо
    a1[i] = a1[i - 1]
    i -= 1
a1[index] = N # придаем нужному элементу по индексу заданное значение
print(*a1)
