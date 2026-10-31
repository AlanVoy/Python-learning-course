num = int(input("Введите число: "))
if num <= 0:
    print("Число должно быть больше нуля")
else num > 0:
    a = 1
    while a <= num:
        print(a)
        a = a + 1
