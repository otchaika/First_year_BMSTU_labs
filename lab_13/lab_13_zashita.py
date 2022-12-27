# вводится имя файла, в котором содержится целочисл матрица
# вводится имя выходного файла, в которое записать транспонированную матрицу
# считывать только одну строку за раз
import os
while IOError:
    try:
        path = input('Введите путь до файла')
        f = open(path)
    except IOError:
        print('Такого файла не существует. Введите другой путь')
    else:
        break
old = open(os.path.abspath(path), 'r')
new_file = input('введите название файла')+'.txt'
new = open(os.path.abspath(new_file), 'w')
str_num=0
col_num = 0
print(old)
for i in old:
    str_num+=1
    r = i.split(' ')
    col_num=len(r)
old = open(os.path.abspath(path))
for j in range(col_num):
    old = open(os.path.abspath(path))
    for i in old:
        r = i.split(' ')
        new.write(str(str(int(r[j]))+' '))
    new.write('\n')
new.close()
new = open(os.path.abspath(new_file), 'r')
for i in new:
    print(i, end='')
