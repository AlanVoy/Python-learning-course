num = int(input("Введите число: "))
count = num - 1
flag = False
while count > 1  :
    if num % count == 0 :
        flag = True
        break 
    else :
        count = count - 1
if flag or num < 2:
    print("Число не простое")
else :
    print("Число простое")