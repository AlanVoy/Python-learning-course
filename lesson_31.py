num = abs(int(input("Введите число: ")))
find = int(input("Введите цифру от 0 до 9 для поиска: "))
count_exit = 0
count_find = 0
while find > 9 or find < 0:
    print("Ошибка, введите цифру от 0 до 9")
    find = int(input("Введите цифру от 0 до 9 для поиска: "))
    count_exit += 1
    if count_exit == 3 :
        exit()
if num == 0 and find == 0 :
    count_find += 1
while num > 0 :
    if find == (num % 10) :
        count_find += 1
    num = num // 10
if count_find == 0 :
    print("Цифра не найдена")
else :
    print("Цифра найдена. Количество",count_find)