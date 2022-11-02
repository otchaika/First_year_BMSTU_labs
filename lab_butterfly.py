# блок ввода
x = float(input('Введите x '))
y = float(input('Введите y '))
# так как бабочка симметрична относительно оси у, берем х под модуль, но не забываем учесть его знак при определении местоположения точки
if x < 0:
    left = True
else:
    left = False
x = abs(x)
place = ''
in_butterfly = False
# проверка на верхнее крыло
if y > 0 and x < 9 and x > 1 and y < -1 / 8 * (x - 9) ** 2 + 8:
    if (x >= 8 and y > 7 * (x - 8) ** 2 + 1) or (x < 8 and y > 1 / 49 * (x - 1) ** 2):
        in_butterfly = True
        if left == True:
            place = 'Верхнее левое крыло'
        else:
            place = 'Верхнее правое крыло'
# проверка на нижнее крыло
if y < 0 and x < 8 and x > 1 and y < -4 / 49 * (x - 1) ** 2:
    print('rrr')
    if (x >= 2 and y > 1 / 3 * (x - 5) ** 2 - 7) or (x < 2 and y > -2 * (x - 1) ** 2 - 2):
        in_butterfly = True
        if left == True:
            place = 'Нижнее левое крыло'
        else:
            place = 'Нижнее правое крыло'
# проверка на тельце
if x < 1 and y < 4 * x ** 2 + 2 and y > 4 * x ** 2 - 6:
    in_butterfly = True
    place = 'Тельце'

# блок вывода
if in_butterfly == True:
    print('Точка принадлежит бабочке. Расположение: ', place)
else:
    print('Точка не принадлежит бабочке')

