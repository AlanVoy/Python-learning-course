count_pred = int(input("Количество чисел(не менее 2): "))
if count_pred < 2 :
    count_check_pred = 0
    while count_pred < 2 :
        if count_check_pred == 3 :
            exit()
        else :
            print("Число не менее 2")
            count_pred = int(input("Количество чисел(не менее 2): "))
            count_check_pred += 1
else :
    total = 0
    count_of_all = 1
    count_total = 0
    num = int(input("Введите число: "))
    while count_of_all < count_pred :
            total += num
            num = int(input("Введите число: "))
            if num == total :
                count_total += 1
            count_of_all += 1
    print("Количество чисел, удовлетворяющих условию: ", count_total)