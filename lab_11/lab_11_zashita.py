# Силинг Екатерина. Метод вставки с бинарным поиском

n = int(input('Введите длину массива: '))
a = []
for i in range(n):
    a.append(int(input('Введите {0}-й элемент массива: '.format(i+1))))

def bin_sort(a):
    arr = a[:]
    for i in range(len(arr)):
        cur = arr[i]
        first = 0
        last = i-1
        while first <=last:
            middle = (first+last)//2
            if cur > arr[middle]:
                first = middle+1
            else:
                last = middle-1
        for j in range(i,first, -1):
            arr[j]=arr[j-1]
        arr[first] = cur
    return arr
print('Отсортированный массив: ', *bin_sort(a))