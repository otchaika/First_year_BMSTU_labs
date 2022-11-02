# Силинг Екатерина. Вариант 6. Поиск элемента в списке строк по варианту. Поиск элемента наибольшей длины,
# не содержащего английских гласных
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
max_el=0
max_len = 0  # максимальная длина
has_vowels = False  # показатель найденных гласных в строке
vowels = set('EYUIOAeyuioa')  # множество английских гласных букв, чтобы искать совпадения в строке с ним
for i in range(len(a)):
    for j in a[i]:
        if j in vowels:
            has_vowels = True  # если в строке есть гласные
    if has_vowels == False and len(a[i]) > max_len:  # если длина строки больше наибольшей предыдущей
        max_len = len(a[i])
        max_el=a[i]
    has_vowels = False
if max_len == 0:  # если нет ни одной подходящей строки в списке
    print('Нет таких элементов')
else:
    print(max_el)
