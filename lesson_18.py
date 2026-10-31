num = int(input("Введите число: "))
count = 0
total = 0
average = 0
while num != 0:
    count = count + 1
    total = total + num
    num = int(input("Введите число: "))
if count == 0:
    print("Числа не введены")
else:
    average = total / count
    print("Сумма:",total)
    print("Среднее:",average)