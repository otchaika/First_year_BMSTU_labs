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

# 1a Добавить элемент в заданное место списка (по индексу)

index = int(input('Введите индекс места, куда нужно добавить элемент: '))
N = int(input('Введите значение элемента: '))
a.insert(index, N) # команда для добавления элемента в список по индексу
print(*a)