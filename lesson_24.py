num = int(input("Введите число: "))
num = abs(num)
total = 0
if num != 0:
    while num != 0:
        total = total + (num % 10)
        num = num // 10
print("Сумма цифр:",total)