num = int(input("Введите число: "))
maxofnum = 0
if num != 0 :
    num = abs(num)
    while num != 0 :
        if (num % 10) > maxofnum :
            maxofnum = num % 10
        num = num // 10
    print("Максимальная цифра:",maxofnum)
else :
    print("Максимальная цифра:",maxofnum)