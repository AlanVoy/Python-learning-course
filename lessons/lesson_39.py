print("Вычисляем строгую последовательность")
count_quantity = int(input("Введите кол-во чисел последовательности(не менее 2): "))
count_check_quantity = 1
while count_quantity < 2 :
    if count_check_quantity == 3 :
        exit()
    else :
        print("Кол-во чисел не может быть меньше 2")
        count_quantity = int(input("Введите кол-во чисел последовательности(не менее 2): "))
        count_check_quantity += 1
num = int(input("Введите число: "))
count_input = 1
num_previous = num
count_large_sequence = 1
max_large_sequence =  1
while count_input <= count_quantity :
    if count_input > 1 :
        if num > num_previous :
            count_large_sequence += 1
            if count_large_sequence > max_large_sequence :
                max_large_sequence = count_large_sequence
        else :
            count_large_sequence = 1
    if count_input < count_quantity :
        num_previous = num
        num = int(input("Введите число: "))
    count_input += 1
print("Максимальная длина возрастающей последовательности: ", max_large_sequence)