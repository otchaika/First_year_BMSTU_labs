# Силинг Екатерина. 6 лабораторная

a = input('Введите элементы через пробел: ')
a = a.split(' ')
for i in range(len(a)):
    a[i] = int(a[i])
print(a)

# 1a
print('1а ЗАДАНИЕ. Добавить элемент в заданное место списка (по индексу)')
do_the_num=int(input('Выполнить 1a задание? '))
if do_the_num == 1:
    index = int(input('Введите индекс места, куда нужно добавить элемент: '))
    N = int(input('Введите значение элемента: '))
    a1=a[:]
    a1.insert(index, N)
    print(*a1)
# 1b
print('1b ЗАДАНИЕ. Добавить элемент в заданное место списка (по индексу) алгоритмически')
do_the_num=int(input('Выполнить 1b задание? '))
if do_the_num == 1:
    index=-1
    while index <0:
        index = int(input('Введите индекс места, куда нужно добавить элемент: '))
    N = int(input('Введите значение элемента: '))
    a1=a[:]
    a11=[0]*(len(a1)+1)
    a11[index]=N
    i=0
    while i < index:
        a11[i]=a1[i]
        i+=1
    i=index+1
    while i <= len(a11)-1:
        a11[i]=a1[i-1]
        i+=1
    print(*a11)
# 2a Удалить элемент с заданным индексом с использованием любых средств Python
print('2a ЗАДАНИЕ. Удалить элемент с заданным индексом')
do_the_num=int(input('Выполнить 2b задание? '))
if do_the_num == 1:
    a2 = a[:]
    index = -1
    while index < 0:
        index=int(input('Введите индекс элемента, который нужно удалить: '))
    deleted_el=a2[index]
    a2.pop(index)
    print('Список с удаленным элементом: ',*a2)
    print('Удален элемент, равный {:5g}'.format(deleted_el))
# 2b
print('2b ЗАДАНИЕ. Удалить элемент с заданным индексом алгоритмически')
do_the_num=int(input('Выполнить 2b задание? '))
if do_the_num == 1:
    a2 = a[:]
    index = -1
    while index < 0:
        index = int(input('Введите индекс элемента, который нужно удалить: '))
    deleted_el = a2[index]
    i = index
    while i < len(a2)-1:
        a2[i]=a2[i+1]
        i+=1
    a2.pop()
    print('Список с удаленным элементом: ', *a2)
    print('Удален элемент, равный {:5g}'.format(deleted_el))

# 3
print('3 ЗАДАНИЕ. Найти значение K-го экстремума в списке.')
do_the_num=int(input('Выполнить 3 задание? '))
if do_the_num == 1:
    a3=a[:]
    k = -1
    while k < 0:
        k=int(input('Введите К (номер экстремума: '))
    k=k%len(a3)
    a3.sort()
    a3 = list(set(a3))
    print(a3[k-1])

# 4 Вариант 7. Найти наиболее длинную непрерывную последовательность знакочередующихся нечётных чисел.
print('4 ЗАДАНИЕ. Найти наиболее длинную непрерывную последовательность знакочередующихся нечётных чисел.')
do_the_num=int(input('Выполнить 4 задание? '))
if do_the_num == 1:
    a4 = a[:]
    len_posl = 0
    max_len_posl = 0
    for i in range(1, len(a4)):
        if a4[i] % 2 !=0 and a4[i - 1] % 2 != 0 and a4[i - 1] * a4[i] < 0:
            len_posl += 1
        else:
            if len_posl > max_len_posl:
                max_len_posl = len_posl +1
            len_posl = 0
    print('Максимальная длина последовательности знакочередующихся нечетных чисел: ', max_len_posl)

# 5 Вариант 9. Поменять местами первый чётный и максимальный положительный.
print('5 ЗАДАНИЕ. Поменять местами первый чётный и максимальный положительный.')
do_the_num=int(input('Выполнить 5 задание? '))
if do_the_num:
    a5 = a[:]
    index_chet = None
    index_max_pos = 0
    max_pos = None
    for i in range(len(a5)):
        if max_pos is None or a5[i] > max_pos:
            max_pos = a5[i]
            index_max_pos = i
        if index_chet is None and a5[i] % 2 == 0:
            index_chet = i
    if index_max_pos is not None and index_chet is not None and index_chet!=index_max_pos:
        a5[index_chet], a5[index_max_pos] = a5[index_max_pos], a5[index_chet]
        print('Измененный список: ', *a5)
    else:
        print('Список не изменится')

