num = int(input("Введите число: "))
num = abs(num)
count = 0
if num != 0:
    while num != 0:
        num = num // 10
        count += 1
else:
    count += 1
print("Количество цифр:",count)