num = int(input("Введите число: "))
num = abs(num)
count = 0
while num > 0 :
    if (num % 10) == 5 :
        count += 1
    num = num // 10
if count > 0 :
    print("Количество цифр 5:",count)
else :
    print("Цифра 5 не найдена")