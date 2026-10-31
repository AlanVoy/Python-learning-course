num = int(input("Введите число: "))
num = abs(num)
minofnum = num % 10
if num != 0 :
    while num != 0 :
        if (num % 10) < minofnum :
            minofnum = num % 10
        num = num // 10
    print("Минимальная цифра:",minofnum)
else :
    print("Минимальная цифра:",minofnum)