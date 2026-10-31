num = int(input("Введите число: "))
num = abs(num)
count_even = 0
count_odd = 0
if num != 0 :
    while num > 0 :
        if ((num % 10) % 2) == 0 :
            count_even += 1
        else :
            count_odd += 1
        num = num // 10
else :
    count_even += 1
print("Четные цифры:", count_even)
print("Нечётные цифры:", count_odd)
if count_odd == count_even :
    print("Равно количество чётных и нечётных чифр")
elif count_even > count_odd :
    print("Чётных цифр больше")
else :
    print("Нечётных цифр больше")