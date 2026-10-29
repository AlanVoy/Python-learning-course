num = int(input("Введите число: "))
even_count = 0
odd_count = 0
while num != 0:
    if num % 2 == 0:
        even_count += 1
    else :
        odd_count += 1
    num = int(input("Введите число: "))
print("Чётных:",even_count,"Нечётных:",odd_count)