num = int(input("Введите число - ограничитель: "))

if num < 2 :
    print("Ошибка ввода. Число должно быть больше 1")
else :
    print("2", end="")
    if num > 2 :
        count = 3
        while count <= num :
            flag = False
            count_check = 2
            while not flag and count_check <= count ** 0.5 :
                if count % count_check == 0 :
                    flag = True
                    break
                else :
                    count_check += 1
            if not flag :
                print(",", count, end="")
            count += 1