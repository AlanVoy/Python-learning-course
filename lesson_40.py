count_all = int(input("Введите кол-во чисел: "))
count = 1
if count_all > 0 :
    flag = True
    while count <= count_all :
        num = int(input("введите число "))
        if count == 1 :
            num_1 = num
        if  count == 2 :
            while num == num_1 and count < count_all:
                num = int(input("введите число "))
                count += 1
            if num_1 > num :
                num_2 = num
            else :
                num_2 = num_1
                num_1 = num
        elif num > num_1 :
            num_2 = num_1
            num_1 = num
        elif (num < num_1 and num > num_2) :
            num_2 = num
        count += 1
if count_all <= 1 :
    print("Невозмонжо найти")
elif num_1 == num_2 :
    print("Невозмонжо найти")
else :
    print(num_2)