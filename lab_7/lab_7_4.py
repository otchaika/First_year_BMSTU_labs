# Силинг Екатерина. Лабораторная 7. вариант 5. Изменение элемента в списке строк по варианту.
# Замена всех цифр на пробелы
# Блок ввода
len_a = -1
while len_a < 0 or len_a != int(len_a):
    len_a = float(input('Введите длину списка: '))
len_a = int(len_a)
a = [0] * len_a
for i in range(len_a):
    x = 0.1
    x = str(input('Введите {0} строку: '.format(i + 1)))
    a[i] = x

nums = set('1234567890')  # множество всех возможных цифр
for i in range(len(a)):
    for j in nums:
        a[i] = a[i].replace(j, ' ')  # если в списке есть элемент, равный цифре, заменяем его на пробел
    print(i + 1, '-я строка: |', a[i], '|')  # печать построчно с ограничителем '|'
if len(a)==0:
    print('Список пуст')