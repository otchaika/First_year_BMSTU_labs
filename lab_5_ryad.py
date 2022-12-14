# Силинг Екатерина. Вариант 24. Эта программа считает и выводит в таблицу элементы и текущую сумму бесконечного ряда, 
# пока не достигнута заданная точность. Далее печатает сумму бесконечного ряда при указанной точности

# блок ввода
y1 = 1
x = -1
eps = -1
it_num = int(input('Введите количество итераций: '))
while it_num < 2:
    it_num = int(input('Введите количество итераций больше 1: '))
while x <= 0:
    x = float(input('Введите значение аргумента больше 0: '))
shag = int(input('Введите шаг печати: '))
while shag >= it_num:
    shag = int(input('Введите шаг печати, меньший количества итераций и больший 0: '))
while eps < 0:
    eps = float(input('Введите точность больше 0: '))

# печать верхней части таблицы
print('-' * 46)
print('| ', '№ итерации ', '|', '     t      ', '|', '     s      ', '|')
print('|', '-' * 42, '|')
# подсчет значений
i = 1  # текущий номер итерации
tek_sum = 0  # текущая сумма
tek_y = 0  # текущий элемент
i_next = 1  # номер следующей итерации, которая будет печататься в таблице
found = False  # индикатор того, что точность достигнута
while not found and i <= it_num:
    tek_y = 1 / (i ** x)  # задаем текущий элемент
    if tek_y <= eps:  # если точность достигнута, прекращаем печать таблицы
        found = True  # делаем индикатор найденности True
        tek_sum += tek_y
        break
    tek_sum += tek_y
    if i == i_next:  # если эта итерация должна печататься (в зависимости от шага)
        print('|  ', '{0:10g}'.format(i), '|', '{0:12.5g}'.format(tek_y), '|', '{0:12.5g}'.format(tek_sum), '|')
        i_next += shag
    i += 1
print('-' * 46)

# Печать результата подсчета - если не получилось, альтернативный вывод
if found is False:
    print('За указанное число итераций необходимой точности достичь не удалось')
else:
    print('Сумма бесконечного ряда - {0:5f} вычислена за {1} итераций.'.format(tek_sum, i))
