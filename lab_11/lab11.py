# fast sort
def partition(sort_nums, begin, end):
    part = begin
    for i in range(begin+1, end+1):
        if sort_nums[i] <= sort_nums[begin]:
            part += 1
            sort_nums[i], sort_nums[part] = sort_nums[part], sort_nums[i]
    sort_nums[part], sort_nums[begin] = sort_nums[begin], sort_nums[part]
    return part
def quick_sort(sort_nums, begin=0, end=None):
    if end is None:
        end = len(sort_nums) - 1
    def quick(sort_nums, begin, end):
        if begin >= end:
            return
        part = partition(sort_nums, begin, end)
        quick(sort_nums, begin, part-1)
        quick(sort_nums, part+1, end)
    return quick(sort_nums, begin, end)
nums = [54, 43, 3, 11, 0]
quick_sort(nums)
print(nums) # Выведет [0, 3, 11, 43, 54]

# sliyanie

def mergeSort(sort_nums):
    if len(sort_nums)>1:
        mid = len(sort_nums)//2
        lefthalf = sort_nums[:mid]
        righthalf = sort_nums[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=0
        j=0
        k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                sort_nums[k]=lefthalf[i]
                i=i+1
            else:
                sort_nums[k]=righthalf[j]
                j=j+1
            k=k+1
        while i<len(lefthalf):
            sort_nums[k]=lefthalf[i]
            i=i+1
            k=k+1
        while j<len(righthalf):
            sort_nums[k]=righthalf[j]
            j=j+1
            k=k+1
nums = [54, 43, 3, 11, 0]
mergeSort(nums)
print(nums) # Выведет [0, 3, 11, 43, 54]

#pyramid

def heapify(sort_nums, heap_size, root):
    l = root
    left = (2 * root) + 1
    right = (2 * root) + 2
    if left < heap_size and sort_nums[left] > sort_nums[l]:
        l = left
    if right < heap_size and sort_nums[right] > sort_nums[l]:
        l = right
    if l != root:
        sort_nums[root], sort_nums[l] = sort_nums[l], sort_nums[root]
        heapify(sort_nums, heap_size, l)
def heap(sort_nums):
    size = len(sort_nums)
    for i in range(size, -1, -1):
        heapify(sort_nums, size, i)
    for i in range(size - 1, 0, -1):
        sort_nums[i], sort_nums[0] = sort_nums[0], sort_nums[i]
        heapify(sort_nums, i, 0)
nums = [54, 43, 3, 11, 0]
heap(nums)
print(nums) # Выведет [0, 3, 11, 43, 54]

#vstavki

def insertion(list_nums):
    for i in range(1, len(list_nums)):
        item = list_nums[i]
        i2 = i - 1
        while i2 >= 0 and list_nums[i2] > item:
            list_nums[i2 + 1] = list_nums[i2]
            i2 -= 1
        list_nums[i2 + 1] = item
nums = [54, 43, 3, 11, 0]
insertion(nums)
print(nums) # Выведет [0, 3, 11, 43, 54]

def insertion_binary(data):
	for i in range(len(data)):
		key = data[i]
		lo, hi = 0, i - 1
		while lo < hi:
			mid = lo + (hi - lo) // 2
			if key < data[mid]:
				hi = mid
			else:
				lo = mid + 1
		for j in range(i, lo + 1, -1):
			data[j] = data[j - 1]
		data[lo] = key
	return data
def insertion_binary(data):
    for i in range(1, len(data) - 1):
        key = data[i]
        lo, hi = 0, i - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if key < data[mid]:
                hi = mid
            else:
                lo = mid + 1
        for j in range(i, lo + 1, -1):
            data[j] = data[j - 1]
        data[lo] = key
    return data
a = [5,6,4,8,3,9,2,0,2]
print(insertion_binary(a))

def bin_search(ls, el, bg, en):
   while bg <= en:
       tm = (bg + en) // 2
       if el > ls[tm]:
          bg = tm + 1
       else:
          en = tm - 1
   return bg


def sort_ins(lss):
   for i in range(0, len(lss)):
      kl = lss[i]
      j1, j2 = 0, i - 1
      ll = bin_search(ls, kl, j1, j2)
      for k in range(i, ll, -1):
         lss[k] = lss[k - 1]
      lss[ll] = kl
   return lss

def custom_sort(mass: list, n: int = None) -> (list, int):
    """
    Сортировка методом бинарных вставок
    :param mass: Массив для сортировки
    :param n: длинна массива
    :return: массив, количество перестановок, время выполнения
    """
    n = n or len(mass)
    p_count = 0
    for i in range(n):
        value = mass[i]
        left, right = 0, i - 1
        while left <= right:  # бинарный поиск
            middle = (right + left) // 2
            if value > mass[middle]:
                left = middle + 1
            else:
                right = middle - 1
        for j in range(i, left, -1):  # перестановки
            mass[j] = mass[j - 1]
            p_count += 1
        mass[left] = value
    return mass, p_count