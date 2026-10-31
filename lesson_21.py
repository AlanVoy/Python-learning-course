num = int(input("Введите число:"))
count = 0
if num != 0:
    possum = 0
    negsum = 0
while  num != 0:
    if num > 0:
        possum = possum + num
    else:
        negsum = negsum + num
    count += 1
    num = int(input("Введите число:"))
if count == 0:
    print("Числа не введены")
else:
    print("Сумма положительных:",possum)
    print("Сумма отрицательных:",negsum)
