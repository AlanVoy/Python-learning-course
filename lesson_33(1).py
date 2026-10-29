num = int(input("Введите число: "))
flag = False
if (num < 10 and num > -1) or (num < 0 and num > -10):
    print("Ничего не меняем:",num)
else:
    if num < 0 :
        num = abs(num)
        flag = True
    num_new = 0
    num_count = num
    count = 0
    while num_count > 0 :
        num_count = num_count // 10
        count += 1
    while num > 0 :
        num_new = num_new + ((num % 10) * (10 ** (count - 1)))
        num = num //10
        count -= 1
    if flag :
        num_new = num_new * (-1)
    print("Перевернули:",num_new)