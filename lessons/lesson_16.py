num = int(input("Введите число: "))
maxnum = num
while num != 0:
    if num > maxnum:
        maxnum = num
    num = int(input("Введите число: "))
if maxnum == 0:
    print("Числа не введены")
else:
    print("Максимум:", maxnum)
