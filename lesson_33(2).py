num = int(input("Введите число: "))
flag = False
if (num < 10 and num >= 0) or (num > -10 and num < 0) :
    print("Число не меняется:",num)
    exit()
if num < 0 :
    num = abs(num)
    flag = True
num_new = int()
while num > 0 :
    num_new = num_new * 10 + (num % 10)
    num = num // 10
if flag :
    num_new = num_new * (-1)
print("Ваше число:",num_new)