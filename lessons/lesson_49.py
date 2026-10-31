quantity_num = int(input("Укажите количество вводных данных(не менее 2): "))
if quantity_num < 2:
    count_enter_quantity = 1
    while quantity_num < 2 and count_enter_quantity < 3 :
        print("Количество не может быть менее 2")
        quantity_num = int(input("Укажите количество вводных данных(не менее 2): "))
        count_enter_quantity += 1
    if count_enter_quantity == 3 and quantity_num < 2 :
        print("Количество неверных вводных данных привысило лимит. Автоматическое закрытие программы")
        exit()
if quantity_num > 1 :
    maximum_sequence_length = 1
    count_enter_num = 0
    count_sequence = 0
    while count_enter_num < quantity_num :
        if count_enter_num == 0 :
            num = int(input("Введите число: "))
            count_enter_num += 1
            count_sequence += 1
        if count_enter_num == 1 :
            num_prev = num
            num = int(input("Введите число: "))
            count_enter_num += 1
            if num > num_prev :
                count_sequence += 1
                if maximum_sequence_length < count_sequence :
                    maximum_sequence_length = count_sequence
        while num_prev >= num and count_enter_num < quantity_num :
            num_prev = num
            num = int(input("Введите число: "))
            count_enter_num += 1
            if num > num_prev :
                count_sequence += 1
                if maximum_sequence_length < count_sequence :
                    maximum_sequence_length = count_sequence
        while num_prev < num and count_enter_num < quantity_num :
            num_prev = num
            num = int(input("Введите число: "))
            count_enter_num += 1
            if num_prev < num :
                count_sequence += 1
                if maximum_sequence_length < count_sequence :
                    maximum_sequence_length = count_sequence
            else :
                count_sequence = 1
    print("Максимальная длина последовательности:",maximum_sequence_length)