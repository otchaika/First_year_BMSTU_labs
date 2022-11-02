# Силинг Екатерина. 6 лабораторная
# блок ввода
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

# 3 Найти значение K-го экстремума в списке.
a3 = a[:]
k = -1
while k <= 0:  # проверка K на положительность
    k = int(input('Введите значение К: '))
# основной блок
i = 1
count_ext = 0  # счетчик экстремум

while i < len(a3) - 1:
    if (a3[i] < a3[i + 1] and a3[i] < a3[i - 1]) or (
            a3[i] > a3[i + 1] and a3[i] > a3[i - 1]):  # если данный элемент - экстремум
        count_ext += 1
    if count_ext == k:  # если данная экстремума - искомая
        print(a3[i])
        break
    i += 1
if count_ext < k:  # Если в списке недостаточно экстремум, выводим текст, что нужного значения нет
    print('Такого значения нет')
