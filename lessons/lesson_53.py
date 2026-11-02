import sys
#
#
#
quantity = int(input("Укажите количество вводных данных: "))
if quantity < 1 :
    count_check_quantity = 1
    while count_check_quantity < 3 and quantity < 1:
        print("Количество не может быть менее 1")
        quantity = int(input("Укажите количество вводных данных: "))
        count_check_quantity += 1
    if count_check_quantity == 3 and quantity < 1 :
        print("Превышен лимит попыток ввода")
        sys.exit()
    else :
        del count_check_quantity
if quantity >= 1 :
    text = ""
    count_enter = 0
    while count_enter < quantity :
        text = text + input("Введите число: ") + " "
        count_enter += 1
    del count_enter
    text_total = text
    text_control = text
    flag_num_one = False
    count_find = 0
    while text_control != "" and not flag_num_one:
        space_control = text_control.find(" ")
        num = int(text_control[:space_control])
        while text_total != "" and count_find < 2 :
            space_total = text_total.find(" ")
            if num == int(text_total[:space_total]) :
                count_find += 1
            text_total = text_total[space_total + 1:]
        if count_find < 2 :
            flag_num_one = True
            num_one = num
            continue
        count_find = 0
        text_total = text
        text_control = text_control[space_control + 1:]
    if not flag_num_one :
        print("Неповторяющихся чисел нет")
    else :
        print("Первое неповторяющееся число:", num_one)