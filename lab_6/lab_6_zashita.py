# Силинг Екатерина. найти сумму между К и К-1 экстремумом, не включая в эту сумму эти кстремумы и записать эту сумму
# вместо L-ного экстремума
a = input('Введите элементы через пробел: ')
a = a.split()
for i in range(len(a)):
    a[i] = int(a[i])
k = int(input('Введите К больше 1: '))
l = int(input('Введите L:'))
b = [0]
count_ext = 0
sum_active = False
sum_el = 0
k_found = False
index = -1
for i in range(len(a) - 2):
    if sum_active == True:
        sum_el += a[i + 1]

    if (a[i + 1] > a[i + 2] and a[i + 1] > a[i]) or (a[i + 1] < a[i + 2] and a[i + 1] < a[i]):
        count_ext += 1
        b.append(a[i + 1])

        if count_ext == k - 1:
            sum_active = True
            k_found = True
        elif count_ext == k and count_ext != l:
            sum_active = False
            sum_el -= a[i + 1]
        if count_ext == l:
            index = i + 1
if index != -1:
    a[index] = sum_el
else:
    print('L-го экстремума нет')
if k_found == False:
    print('невозможно вычислить сумму, поскольку нет k-1 экстремума')
elif k_found == True and i != -1:
    print(*a)
    print('Сумма: ', sum_el)
