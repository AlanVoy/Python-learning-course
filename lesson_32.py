num = int(input("Введите число: "))
flag = False
if num > 9 :
    num_red = num
    count_all = 0
    while num_red > 9 :
        num_red = num_red // 10
        count_all += 1
    count_check = (count_all + 1) // 2
    flag = True
    num_red = num
    while count_check > 0 and flag:
        if ((num //(10 ** count_all)) % 10) == (num_red % 10 ):
            count_all = count_all - 1
            count_check = count_check - 1
            num_red = num_red // 10
        else :
            flag = False
if flag or (num < 10 and num >= 0):
    print("Число является палиндромом")
else : 
    print("Число не является палиндромом")