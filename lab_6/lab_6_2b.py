# Силинг Екатерина. 6 лабораторная

len_a = -1
while len_a < 0 or len_a != int(len_a):
    len_a = float(input('Введите длину списка: '))
len_a = int(len_a)
a = [0] * len_a
for i in range(len_a):
    x = 0.1
    while x != int(x):
        x = float(input('Введите {0} элемент: '.format(i + 1)))
    x = int(x)
    a[i] = x
# 2b Удалить элемент с заданным индексом алгоритмически

a2 = a[:]
index = -1
while index < 0 or index > len(a2) - 1:
    index = int(input('Введите индекс элемента, который нужно удалить: '))
deleted_el = a2[index]
i = index
for i in range(index, len(a2)-1):
    a2[i] = a2[i + 1]
a2.pop()
print('Список с удаленным элементом: ', *a2)
print('Удален элемент, равный {:}'.format(deleted_el))
