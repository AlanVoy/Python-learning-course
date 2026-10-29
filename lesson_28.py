num = int(input("Введите число: "))
flag = False
num = abs(num)
while num > 0 and not flag :
    if (num % 10) == 7 :
        flag = True
    else :
        num = num // 10
if flag :
    print("Цифра 7 найдена")
else :
    print("Цифра 7 не найдена")