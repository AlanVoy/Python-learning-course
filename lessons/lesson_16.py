num = int(input("Введите число: "))
count = 0
if num != 0:
    maxnum = num
    minnum = num

while num != 0:
    if maxnum < num:
        maxnum = num
    if minnum > num:
        minnum = num
    count += 1
    num = int(input("Введите число: "))
if count == 0 :
    print("Числа не введены")
else :
    print("Максимум:",maxnum,"Минимум:",minnum)