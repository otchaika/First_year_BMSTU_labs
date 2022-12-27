# Силинг Екатерина. 12 лабораторная
# умножение и деление
# 7

# 1. Выровнять текст по левому краю.
# 2. Выровнять текст по правому краю.
# 3. Выровнять текст по ширине.
# 4. Удаление всех вхождений заданного слова.
# 5. Замена одного слова другим во всём тексте.
# 6. Вычисление арифметических выражений над целыми числами внутри текста
# (по варианту).
# 7. Найти (вывести на экран) и затем удалить слово или предложение по варианту.
text = ['Время шло к ночи. Дьячок Савелий Гыкин лежал у себя в церковной сторожке на громадной постели и не спал,',
        'хотя всегда имел обыкновение засыпать в одно время с курами. Из 5 одного края засаленного, сшитого из разноцветных',
        'ситцевых лоскутьев одеяла глядели его *2*3 рыжие, жесткие волосы, 5 из-под другого торчали большие, давно не мытые ноги. Он',
        'слушал. Его сторожка врезывалась в ограду, 4/5/7 *2 и единственное окно ее выходило в поле? А в поле была сущая',
        'война. Трудно было понять, кто кого 5*8 сживал со света и ради чьей погибели заварилась в природе каша, но, судя по ',
        'неумолкаемому зловещему гулу, кому-то приходилось очень круто. Какая-то победительная сила гонялась за кем-то по полю,',
        'бушевала в лесу и на церковной крыше, злобно стучала кулаками по окну, метала и рвала,',
        'а что-то побежденное выло и плакало... 100 /25/4*10.']


def do_task(text, i):  # код выполняет заданное действие
    if i == 1:
        left_side(text)
    elif i == 2:
        right_side(text)
    elif i == 3:
        width(text)
    elif i == 4:
        word = str(input('Введите слово, которое требуется удалить.'))
        delete_word(text, word)
    elif i == 5:
        while AssertionError:
            try:
                word = str(input('Введите слово, которое требуется заменить.'))
                assert word != '' and word !=' '
            except AssertionError:
                print('Введите не пустое слово')
            else:
                break
        while AssertionError:
            try:
                word1 = str(input('На какое слово его заменить? '))
                assert word1 != '' and word1 !=' '
            except AssertionError:
                print('Введите не пустое слово')
            else:
                break
        replace_word(text, word, word1)
    elif i == 6:
        calculate(text)
    elif i == 7:
        find_and_delete(text)


def left_side(text):  # выравнивает текст по левому краю (по факту просто добавляет пробелы до ровного текста)
    max_len = 0
    for i in range(len(text)):
        if len(text[i]) > max_len:
            max_len = len(text[i])
    t = text
    print('Результат: ')
    for i in range(len(t)):
        t[i] = t[i].replace('  ', ' ')
        t[i].strip('')
        print(t[i], end='\n')


def right_side(text):  # выравнивает текст по правому краю, добавляя в начало строки недостающие пробелы
    max_len = 0
    for i in range(len(text)):
        if len(text[i]) > max_len:
            max_len = len(text[i])
    t = text
    print('Результат: ')
    for i in range(len(t)):
        t[i] = t[i].strip(' ')
        for j in range(max_len//2):
            t[i] = t[i].replace(' '*2, ' ')
        print(' ' * (max_len - len(t[i])), t[i], end='\n')


def width(text):  # функция выравнивает текст по ширине
    t = text
    max_len = 0
    for i in range(len(text)):
        if len(text[i]) > max_len:
            max_len = len(text[i])
    print('Результат: ')
    for i in range(len(t) - 1):
        t[i] = t[i].strip(' ')
        probels = t[i].count(' ')  # количество пробелов в строке
        if probels!=0:
            free_spaces = max_len - len(t[i])  # количество незанятых мест
            n = 1 + int(free_spaces / probels)  # количество необходимых пробелов между словами
            left = free_spaces % probels  # оставшиеся пробелы (их будем добавлять к пробелам начиная с первого
            t[i] = t[i].replace(' ', ' '* n)
            t[i] = t[i].replace(' ' * n, ' ' * (n + 1), left)
        print(t[i], end='\n')
    print(t[-1])


def delete_word(text, word):  # удаляет заданное пользователем слово
    t = text
    w1 = word
    flag = False
    for i in range(len(t)):
        t[i] = t[i].split(' ')
        j = 0
        while j < len(t[i]) - 1:
            if is_word_similar(t[i][j], w1):  # если слово совпадает с заданным, удаляем
                t[i].pop(j)
                flag = True
            else:
                j += 1  # если нет, движемся дальше по тексту
        t[i]=' '.join(t[i])
    if flag:
        for i in range(len(t)):  # если нашлось хотя бы одно вхождение слова
            print(t[i])
    if not flag:
        print('Нет ни одного вхождения данного слова')  # если не нашлось ни одного вхождения слова


def is_word_similar(w, w1):  # функция провеняет, совпадают ли слова. Учитывает знаки препинания
    chars = "',./\"#:;!?*(){}[]"
    start_word = False
    i = 0
    w = w.lower()  # приводим оба слова к прописным буквам
    w1 = w1.lower()
    while not start_word and i < len(w):  # пока слово не началось (первое вхождение буквы
        is_sign = False
        for item in chars:
            if w[i] == item:
                is_sign = True  # символ является одним из знаков препинания
        if is_sign:
            i += 1
        else:
            start_word = True
    start = i  # индекс начала слова
    if i == len(w):  # если слово состоит только из знаком препинания (например, '-')
        return False
    else:
        end_word = False  # конец слова
        while not end_word:
            for item in chars:
                if w[i] == item:  # если это знак препинания, слово закончилось
                    end_word = True
                    i -= 1
            if i == len(w) - 1:  # если это последний символ, слово закончилось
                end_word = True
            i += 1
    end = i - 1  # индекс понца слова
    actual_word = w[start:end + 1]  # слово без окружающих знаков препинания
    if actual_word == w1:  # если оно равно искомому
        return True
    else:
        return False


def replace_word(text, w, w1):  # программа заменяет заданное слово другим
    t = text
    for i in range(len(t)):
        t[i] = t[i].split()
        for j in range(len(t[i])):
            word = t[i][j]
            if is_word_similar(word, w):  # если слова совпадают, перезаписывает слово, заменяя его
                word = word.lower()
                w = w.lower()
                word = word.replace(w, w1)
            t[i][j] = word
        t[i] = ' '.join(t[i])
    for i in range(len(t)):
        print(t[i])


def find_w_len(w):  # функция находит длину слова
    chars = "',./\"#:;!?*(){}[]"
    start_word = False
    i = 0

    while not start_word and i < len(w):
        is_sign = False
        for item in chars:
            if w[i] == item:
                is_sign = True
        if is_sign:
            i += 1
        else:
            start_word = True

    if i == len(w):
        return 0
    if is_num(w):
        return 0
    else:
        lenn = 0
        end_word = False
        while not end_word:
            lenn += 1
            for item in chars:
                if w[i] == item:
                    lenn -= 1
                    end_word = True
            if i == len(w) - 1:
                end_word = True
            i += 1
        return lenn


def find_and_delete(text):
    t = text
    pr = []
    max_pr = []
    max_len_w = 0
    start = [-1, -1]
    start1 = [-1, -1]
    max_len_w_in_pr = 0
    for i in range(len(t)):

        if t[i] !=[]:
            t[i] = t[i].split()
            for j in range(len(t[i])):
                pr.append(t[i][j])
                len_w = find_w_len(t[i][j])
                if len_w > max_len_w_in_pr:
                    max_len_w_in_pr = len_w
                if t[i][j][-1] == '.' or t[i][j][-1] == '?' or t[i][j][-1] == '!':
                    if max_len_w_in_pr > max_len_w:
                        max_len_w = max_len_w_in_pr
                        max_pr = pr[:]
                        start = start1
                        max_len_w_in_pr = 0
                    start1 = [i, j]
                    pr = []
    if start[1] > len(t[start[0]]) - 1:
        start[0] += 1
        start[1] = 0
    else:
        start[1] += 1
    i = start[0]
    j = start[1]
    count = 0
    if max_pr!=[]:
        print('Предложение с самым длинным словом: ')
        print(*max_pr)
        while count <= len(max_pr) - 1:
            if j < len(t[i]):
                if t[i] != []:
                    t[i].pop(j)
                else:
                    count -= 1
                count += 1
            if j >= len(t[i]):
                j = 0
                i += 1

        print('Измененный текст: ')
        i=0
        while i < len(t):
            t[i] = ' '.join(t[i])
            if t[i]==['']:
                t.pop(i)
            else:
                print(t[i])
                i+=1

    else:
        print('Такого предложения нет.')


def calculate(text):
    t = text
    opers = '*/'
    nums = '0123456789'
    for i in range(len(t)):
        if '*' in t[i] or '/' in t[i]:
            j = 0
            k = 0
            while j < len(t[i]):
                if t[i][j] in nums:
                    next = 'num'
                    cur_str = t[i][j]
                    k = j + 1
                    while k < len(t[i]) and (t[i][k] in opers or t[i][k] in nums or t[i][k] == ' '):
                        if cur_str[-1] in nums and t[i][k] == ' ':
                            next = 'oper'
                            cur_str += ' '
                        if t[i][k] in nums and next == 'oper':
                            break
                            # посчитать вычисление от жи до к

                        if t[i][k] in nums and (cur_str == '' or cur_str[-1] in nums):
                            cur_str += t[i][k]

                        elif t[i][k] in nums and next == 'num':
                            cur_str += t[i][k]
                        if cur_str != '' and t[i][k] in opers and (next == 'oper' or cur_str[-1] in nums):
                            cur_str += ' '
                            cur_str += t[i][k]
                            cur_str += ' '
                            next = 'num'
                        k += 1
                    calced = calcula(cur_str)
                    if calced != None:
                        if calced == int(calced):
                            calced = int(calced)
                        calced = str(calced)
                        lenn = len(calced)
                        spaces = k - j - lenn - 1
                        if cur_str[-1] == ' ':
                            k -= 1
                        t[i] = t[i][:j] + calced + ' ' * spaces + t[i][k:]
                j = k
                k += 1
    for i in range(len(t)):
        print(t[i])


def is_num(w):
    nums = '1234567890.'
    for item in str(w):
        if item not in nums:
            return False
    if w == '.':
        return False
    return True






def calcula(els):  # функция, выводящая результат вычисления из строки
    i = 0
    els = els.split()
    calced = None

    while i < len(els) - 2:
        if is_num(els[i]):
            if els[i + 1] == '*':
                calced = float(els[i]) * float(els[i + 2])
            elif els[i + 1] == '/':
                calced = float(els[i]) / float(els[i + 2])
        if i + 2 == len(els) - 1:
            return calced
        else:
            els.pop(0)
            els.pop(0)
            els[0] = calced
            i -= 1
        i += 1
    return calced

print()
active = True
while active:
    task = 0
    print()
    print('Меню действий: ')
    print('1. Выровнять текст по левому краю+')
    print('2. Выровнять текст по правому краю.')
    print('3. Выровнять текст по ширине.')
    print('4. Удаление всех вхождений заданного слова.')
    print('5. Замена одного слова другим во всём тексте.')
    print('6. Вычисление умножения и деления целых чисел внутри текста')
    print('7. Найти (вывести на экран) и затем удалить предложение предложение с самым длинным словом.')
    print('8. Завершить программу')
    while ValueError or AssertionError:
        try:
            task1 = str(input('Выберите одно из семи действий (введите число от 1 до 8): '))
            task = int(task1)
            assert 0 < task <= 8
        except AssertionError:
            print('Введите число от 0 до 8')
        except ValueError:
            print('Введите целое число')
        else:
            break
    do_task(text,task)
    if task == 8:
        print('Программа завершена')
        active = 0
        raise SystemExit
