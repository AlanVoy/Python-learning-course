import sys
#
#
#
quantity = int(input("Укажите количество(не менее 1): "))
if quantity < 1 :
    count_check_quantity = 1
    while count_check_quantity < 3 and quantity < 1 :
        print("Указано неверное количество")
        quantity = int(input("Укажите количество(не менее 1): "))
        count_check_quantity += 1
    if count_check_quantity == 3 and quantity < 1 :
        print("Достигнут лимит попыток ввода")
        sys.exit()
position = int(input("Укажите позицию(не меньше 1 и не больше указанного количества): "))
if position < 1 or position > quantity :
    count_check_position = 1
    while count_check_position < 3 and (position < 1 or position > quantity) :
        print("Указано неверная позиция")
        position = int(input("Укажите позицию(не меньше 1 и не больше указанного количества): "))
        count_check_position += 1
    if count_check_position == 3 and (position < 1 or position > quantity) :
        print("Достигнут лимит попыток ввода")
        sys.exit()
if quantity > 0 and (position > 0 and position <= quantity) :
    count_enter = 0
    text_enter = ""
    while count_enter < quantity :
        text_enter += (input("Введите число: ") + " ")
        count_enter += 1
    count_orderly = 0
    text_save = text_enter
    text_orderly = ""
    while count_orderly < quantity :
        text_enter = text_save
        if count_orderly > 0 :
            num_find = (" " + text_enter).find(" " + str(num_min) + " ")
            space_enter = text_enter.find(" ",num_find)
            text_enter = text_enter[:num_find] + text_enter[space_enter + 1:]
            text_save = text_enter
        space = text_enter.find(" ")
        num = int(text_enter[:space])
        text_enter = text_enter[space + 1:]
        num_min = num
        while text_enter != "" :
            space = text_enter.find(" ")
            num = int(text_enter[:space])
            num_min = min(num, num_min)
            text_enter = text_enter[space + 1:]
        text_orderly += (str(num_min) + " ")
        count_orderly += 1
    text_for_position = text_orderly
    count_position = position
    while count_position > 1 :
        space_position = text_for_position.find(" ")
        text_for_position = text_for_position[space_position + 1:]
        count_position -= 1
    space_position = text_for_position.find(" ")
    print(text_orderly)
    print("Число на позиции",position,":",int(text_for_position[:space_position]))