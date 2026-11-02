num = int(input("Введите число для проверки: "))
if num < 0 :
    print("Ошибка ввода. Число не должно быть отрицательным.")
else :
    if num > 9 :
        num_check = num
        count = 0
        total = 0
        while num_check > 0 :
            num_check = num_check // 10
            count += 1
        num_check = num
        while num_check > 0 and total < num :
            total = total + ((num_check % 10) ** count)
            num_check = num_check // 10
    if num < 10 or total == num :
        print("Это число Армстронга")
    else :
        print("Это НЕ число Армстронга")