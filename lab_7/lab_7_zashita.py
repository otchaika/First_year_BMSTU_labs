# Силинг Екатерина. Защита 7 лабораторной
# Дан список строк, требуется найти максимальную длину строки, где чередуются буквы и цифры
# 1-last was num, 0 - last was char
len_a = -1
while len_a <= 0:
    len_a = int(input('Введите длину списка: '))
a = [0] * len_a
for i in range(len_a):
    x = str(input('Введите {:}-й элемент: '.format(i + 1)))
    a[i] = x
nums = set('1234567890')
chars = set('QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm')
max_len = 0
max_el = 0
for i in range(len(a)):
    fits = True
    c = -1
    if len(a[i]) > max_len:
        if a[i][0] in nums:
            c = 0
        elif a[i][0] in chars:
            c = 1
        if c == -1:
            fits = False
            break
        for j in a[i]:
            if j in nums and c == 1:  # если прошлый и данный элемент оба цифры
                fits = False
                break
            elif j in chars and c == 0:  # если прошлый и данный элемент оба буквы
                fits = False
                break
            if j in nums and c == 0:  # если прошлый элемент буква, а данный - цифра
                c = 1
            elif j in chars and c == 1:  # если прошлый элемент число, а данный - буква
                c = 0
        if fits and len(a[i]) > max_len:
            max_len = len(a[i])
            max_el = a[i]
if max_len > 0:
    print('Подходящая строка с максимальной длиной: ', max_el)
    print('Ее длина - ', max_len)
elif max_len == 0:
    print('Такого элемента нет')
