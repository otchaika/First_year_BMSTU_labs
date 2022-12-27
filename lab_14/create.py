def fill_in():
    i1 = str(input('Введите имя: '))
    while len(i1) > 15:
        i1 = str(input('Название должно занимать менее 15 символов. Введите снова: '))
    while ValueError or AssertionError:
        try:
            i21 = input('Введите рост: ')
            i2 = int(i21)
            assert len(str(i2)) <= 15
        except ValueError:
            print('Введите целое число')
        except AssertionError:
            print('Значение должно занимать менее 15 символов.')
        else:
            break
    i1 += ' ' * (15 - len(i1))
    i2 = str(i2) + ' ' * (15 - len(str(i2)))
    new_str = i1 + str(i2)
    return new_str.encode('utf-8')
my_file = open('zah2.bin', "wb+")
str_i=10
for i in range(str_i):
    my_file.write(fill_in())
my_file.close()
f = open('zah2.bin', 'rb+')
b = f.read(30)
while b!=b'':
    print(b)
    b = f.read(30)