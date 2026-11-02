num = int(input("Введите число:"))
minnum = num
ss = 0
while num != 0:
    ss = ss + 1
    if minnum > num:
        minnum = num
    num = int(input("Введите число:"))
if ss == 0:
    print("Числа не введены")
else:
    print("Минимум: ",minnum)
