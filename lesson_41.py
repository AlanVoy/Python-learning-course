count_all = int(input("Введите количество(не менее 2): "))
if count_all < 2 :
    count_exit = 0
    while count_all < 2 :
        if count_exit == 3 :
            exit()
        else :
            print("Указано неверное количество")
            count_all = int(input("Введите количество(не менее 2): "))
            count_exit += 1
count = 1
num_stay = int()
num_max = 1
count_check = 1
while count <= count_all :
    num = int(input("Введите число: "))
    if count > 1 :
        if num_stay == num :
            count += 1
            count_check += 1
            if count_check > num_max :
                num_max = count_check
        else :
            count_check = 1
            num_stay = num
            count += 1
    else :
        count += 1
        num_stay = num
print(num_max)