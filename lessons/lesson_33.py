num = int(input("Введите число: "))

if num <=0 :
    print("Ошибка ввода")
else :
    total = 0
    count = num - 1
    while count > 0 :
        if num % count == 0 :
            total = total + count
        count -= 1
    if total == num:
        print("Число совершенное")
    else :
        print("Число не совершенное")