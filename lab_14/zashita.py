# удалить с ростом меньше 50
str_l=30
file = 'zah6.bin'
def pr():
    f = open(file, 'rb+')
    b = f.read(str_l)
    while b !=b'':
        a = b.decode()
        print(a)
        b = f.read(str_l)
def delete_small_people():
    count=0
    f = open(file, 'rb+')
    b = f.read(str_l)
    lenn=0
    c = []
    while b !=b'':
        a = b.decode()
        height = a[15:30]
        height = height.strip()
        if float(height)<50:
            count+=1
            c.append(lenn)
        lenn+=1
        b = f.read(str_l)
    f.close()
    f = open(file, 'rb+')
    for i in range(len(c)):
        f = open(file, 'rb+')
        f.seek(0, 0)
        num = c[i]-i
        f.seek(str_l*(num+1), 0)
        for j in range(lenn-num-1):
            temp = f.read(str_l)
            f.seek(-2*str_l, 1)
            f.write(temp)
            f.seek(str_l, 1)
        f.truncate(str_l*(lenn-1*(i+1)))
        f.close()
print('Исходный файл: ')
pr()
delete_small_people()
print('ИТОГ: ')
pr()

