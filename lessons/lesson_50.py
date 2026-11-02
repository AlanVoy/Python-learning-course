import sys
#
#
#
quantity = int(input("Укажите количество(нечётное и больше 0): "))
if quantity < 1 or (quantity % 2) == 0 :
    count_incorrect_enter = 1
    while count_incorrect_enter < 3 and (quantity < 1 or (quantity % 2) == 0) :
        print("Указано неверное количество")
        quantity = int(input("Укажите количество(нечётное и больше 0): "))
        count_incorrect_enter += 1
    if count_incorrect_enter == 3 and (quantity < 1 or (quantity % 2) == 0) :
        print("Превышен лимит попыток ввода")
        sys.exit()
if quantity > 0 and (quantity % 2) != 0 :
    count_enter = 0
    count_orderly = 0
    orderly_text = ""
    text_enter = ""
    while count_enter < quantity :
        text_enter += (input("Введите число: ") + " ")
        count_enter += 1
    text_1 = text_enter
    text_save = text_enter
    num_min = int()
    num = int()
    while count_orderly < quantity :
        text_1 = text_save
        if count_orderly > 0 :
            num_find = (" " + text_1).find(" " + str(num_min) + " ")
            space_find = text_1.find(" ", num_find)
            text_1 = text_1[:num_find] + text_1[space_find + 1:]
            text_save = text_1
        space_text_1 = text_1.find(" ")
        num = int(text_1[:space_text_1])
        text_1 = text_1[space_text_1 + 1:]
        num_min = num
        while text_1 != "" :
            space_text_1 = text_1.find(" ")
            num = int(text_1[:space_text_1])
            num_min = min(num_min,num)
            text_1 = text_1[space_text_1 + 1:]
        orderly_text += (str(num_min)  + " ")
        count_orderly += 1
    text_save = orderly_text
    count_find = 0
    while count_find < (quantity // 2) :
        space_save = text_save.find(" ")
        text_save = text_save[space_save + 1:]
        count_find += 1
    median_space = text_save.find(" ")
    median = int(text_save[:median_space])
    print(orderly_text)
    print("Медиана:", median)