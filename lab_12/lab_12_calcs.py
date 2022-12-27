text = open('/Users/admin/Desktop/питон/labsPython/lab_12/chekhov').readlines()

max_len = 0
for i in range(len(text)):
    if len(text[i]) > max_len:
        max_len = len(text[i])
print(max_len)


def is_num(w):
    nums = '1234567890.'
    for item in str(w):
        if item not in nums:
            return False
    return True


def count(text):
    i = 0
    t = text[:]
    next = 'num'
    opers = '*/'
    els = []
    operated = False
    while i < len(t):
        t[i] = t[i].split()
        j = 0
        while j < len(t[i]):
            if is_num(t[i][j]) and next == 'num':
                els.append(t[i][j])
                next = 'oper'
                if j + 1 > len(t[i]) - 1:
                    next_s = t[i + 1][0]
                elif i + 1 > len(t) - 1:
                    return t
                else:
                    next_s = t[i][j + 1]
                if not operated:
                    starti = i
                    startj = j
                print(t[i][j])
                if next_s not in opers and operated and next_s != ' ':
                    calced = calculate(els)
                    print(calced, 'calc')
                    operated = False
                    next = 'num'
                    t[starti][startj] = 'AAA'
                    i = starti
                    j = startj
                    print(els)
                    els = []
            elif t[i][j] in opers:
                els.append(t[i][j])
                print(els)
                operated = True
                next = 'num'

            j += 1
        i += 1


def calculate(els):
    i = 0
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


print(calculate(['2', '/', '4', '*', '5', '*', '654']))
print(count(text))
