num = int(input("Введите число: "))
count = 0
if num != 0 :
    count_seven = 0
while num != 0:
    if (num % 7) == 0:
        count_seven += 1
    count += 1
    num = int(input("Введите число: "))
if count == 0 or count_seven == 0:
    print("Число, кратное 7, не найдено")
else :
    print("Число, кратное 7, найдено")