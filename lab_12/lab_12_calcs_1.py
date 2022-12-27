text = open('/Users/admin/Desktop/питон/labsPython/lab_12/chekhov').readlines()

max_len = 0
for i in range(len(text)):
    if len(text[i]) > max_len:
        max_len = len(text[i])


def calculate(text):
    t = text[:]
    opers = '*/'
    nums = '0123456789'
    chars = 'абвгдеёжзийклмнорпстуфхцчшщъыьэюя'
    for i in range(len(t)):
        if '*' in t[i] or '/' in t[i]:
            j = 0
            k = 0
            while j < len(t[i]):
                if t[i][j] in nums:
                    next='num'
                    cur_str=t[i][j]
                    k = j+1
                    while k <len(t[i]) and (t[i][k] in opers or t[i][k] in nums or t[i][k] == ' '):
                        if cur_str[-1] in nums and t[i][k] ==' ':
                            next='oper'
                            cur_str+=' '
                        if t[i][k] in nums and next == 'oper':

                            break
                            # посчитать вычисление от жи до к

                        if t[i][k] in nums and (cur_str=='' or cur_str[-1] in nums):
                            cur_str+=t[i][k]

                        elif t[i][k] in nums and next=='num':
                            cur_str+=t[i][k]
                        if cur_str!= '' and t[i][k] in opers and (next=='oper'or cur_str[-1] in nums):
                            cur_str+=' '
                            cur_str+=t[i][k]
                            cur_str+=' '
                            next = 'num'
                        k+=1
                    calced = calcula(cur_str)
                    if calced!=None:
                        if calced==int(calced):
                            calced = int(calced)
                        calced=str(calced)
                        lenn = len(calced)
                        spaces = k-j-lenn-1
                        if cur_str[-1]==' ':
                            k-=1
                        t[i] = t[i][:j] + calced +' '* spaces+ t[i][k:]

                j = k
                k+= 1
    for i in range(len(t)):
        print(t[i])




def is_num(w):
    nums='1234567890.'
    for item in str(w):
        if item not in nums:
            return False
    if w=='.':
        return False
    return True

def is_calc(w):
    i = 0
    st=0
    yes=True
    opers='*/'
    sep_calc=[]
    next='num'
    yup=False
    while yes:
        while is_num(w[st:i+1]) and i < len(w) and next=='num':
            i+=1
            yup=True
        if yup:
            next = 'oper'
            sep_calc.append(w[st:i])
        yup=False
        st=i+1
        if i+1 >= len(w) or w[i] not in opers:
            return sep_calc
        elif w[i] in opers and (next=='oper' or i ==0):
            sep_calc.append(w[i])
            next='num'
        elif w[i] in opers and next=='num':
            print(sep_calc)
            return sep_calc
        while w[i]==' ':
            i+=1

        i+=1
def calculat(calc):
    nums = '0123456789.'
    calc = calc.split(' ')
    i = 0
    while i < len(calc):
        if is_num(calc[i]):
            if calc[i] == '.':
                break
            else:
                break
def calcula(els):
    i=0
    els = els.split()

    print(els, 'els')
    calced = None

    while i < len(els)-2:
        if is_num(els[i]):
            if els[i+1]=='*':
                calced = float(els[i])*float(els[i+2])
            elif els[i+1]=='/':
                calced = float(els[i]) / float(els[i + 2])
        if i+2==len(els)-1:
            return calced
        else:
            els.pop(0)
            els.pop(0)
            els[0]=calced
            i-=1
        i+=1
    return calced

print(calculate(text))