num = int(input("Введите число: "))
if num != 0 :
    if num < 0 :
        num = abs(num)
    count_even = 0
    count_odd = 0
    while num != 0 :
        if (num % 10) % 2 == 0 :
            count_even += 1
        else :
            count_odd += 1
        num = num // 10
    print("Чётных цифр:",count_even)
    print("Нечётных цифр:",count_odd)
else :
    count_even = 1
    print("указанное число - 0. Чётных чисел:",count_even,"Нечётных чисел нет.")
    