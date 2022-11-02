# Силинг Екатерина. Защита 6 лабораторной. дан массив целых чисел, найти второе по величине значение
len_a = -1
while len_a < 0 or int(len_a) != len_a:
    len_a = float(input('Введите длину списка: '))
len_a = int(len_a)
a = [0] * len_a
for i in range(len_a):
    x = 0.5
    while x != int(x):
        x = float(input('Введите {} элемент: '.format(i + 1)))
    x = int(x)
    a[i] = x

max_1 = None
max_2 = None

for i in range(len(a)):
    if max_1 is None or a[i] > max_1:
        if max_1!=max_2 and max_1 is not None:
            max_2 = max_1
        max_1 = a[i]
    elif max_2 is None or a[i] > max_2:
        max_2 = a[i]
if max_2 is not None and max_2 != max_1:
    print('Второй наибольший элемент: ', max_2)
else:
    print('Такого элемента нет')



print(a)
