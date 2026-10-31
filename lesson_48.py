quantity_num = int(input("Укажите количество(не менее 2): "))
if quantity_num < 2 :
    count_enter_quantity = 1
    while count_enter_quantity != 3 and quantity_num < 2 :
        print("Количество не может быть менее 2")
        quantity_num = int(input("Укажите количество(не менее 2): "))
        count_enter_quantity += 1
    if count_enter_quantity == 3 and quantity_num < 2:
        print("Количество неверных вводных данных привысило лимит. Автоматическое закрытие программы")
        exit()
if quantity_num > 1 :
    count_enter_num = 0
    count_change_sequence = 0
    while count_enter_num < quantity_num :
        if count_enter_num == 0 :
            num = int(input("Введите число: "))
            count_enter_num += 1
        elif count_enter_num == 1 :
            past_num = num
            num = int(input("Введите число: "))
            count_enter_num += 1
        else :
            while num >= past_num and count_enter_num < quantity_num :
                past_num = num
                num = int(input("Введите число: "))
                count_enter_num += 1
                if past_num > num :
                    count_change_sequence += 1
            while num <= past_num and count_enter_num < quantity_num :
                past_num = num
                num = int(input("Введите число: "))
                count_enter_num += 1
                if num > past_num :
                    count_change_sequence += 1
    print("Смен последовательности: ", count_change_sequence)