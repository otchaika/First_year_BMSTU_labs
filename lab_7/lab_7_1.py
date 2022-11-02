# Силинг Екатерина. Лабораторная 7. вариант 2. Удалить все элементы целочисленного списка, имеющие свойство по варианту,
# за один цикл.
# четные элементы

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

# 1 вариант решения
i=0
b = []
while i < len(a):
    if a[i]%2!=0:
        b.append(a[i]) # в новый список добавляем все нужные элементы
    i+=1
if len(b)==0:
    print('Список пустой')
else:
    print(*b)

# 2 вариант решения
i = 0
while i < len(a):
    if a[i]%2==0:
        a.pop(i) # из самого списка удаляем элементы по индексу
    else:
        i+=1
print(*a)
