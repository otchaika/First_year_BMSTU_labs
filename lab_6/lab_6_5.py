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

# 5 Вариант 9. Поменять местами первый чётный и максимальный положительный.
a5 = a[:]
index_chet = None  # индекс первого четного
index_max_pos = 0  # индекс максимального положительного
max_pos = None  # значение максимального положительного
for i in range(len(a5)):
    if max_pos is None or a5[i] > max_pos:  # нахождение максимального положительного
        max_pos = a5[i]
        index_max_pos = i
    if index_chet is None and a5[i] % 2 == 0:  # нахождение первого четного
        index_chet = i
if index_max_pos is not None and index_chet is not None and index_chet != index_max_pos:  # если нашлись оба значения,
    # меняем их местами и печатаем
    a5[index_chet], a5[index_max_pos] = a5[index_max_pos], a5[index_chet]
    print('Измененный список: ', *a5)
else:  # если хоть одно значение не найдено или они совпадают, список не меняется
    print('Список не изменится')
