import sys
#
#
#
qantity = int(input("Укажите количество вводных данных(не менее 1): "))
if qantity < 1 :
    count_enter_quantity = 1
    while count_enter_quantity < 3 and qantity < 1 :
        print("Количество не должно быть меньше 1")
        qantity = int(input("Укажите количество вводных данных(не менее 1): "))
        count_enter_quantity += 1
    if count_enter_quantity == 3 and qantity < 1 :
        print("Исчерпан лимит попыток. Завершение программы")
        sys.exit()
if qantity >= 1 :
    count_enter = 0
    text = str()
    text_total = ""
    count_actual_enter = 0
    while count_enter < qantity :
        num = input("Введите число: ")
        flag = False
        if text_total != "" :
            while text != "" and not flag :
                space = text.find(" ")
                if int(text[:space]) == int(num) :
                    flag = True
                    continue
                text = text[space + 1:]
            if not flag :
                text_total = text_total + num + " "
                count_actual_enter += 1
        else :
            text_total = text_total + num + " "
            count_actual_enter += 1
        text = text_total
        count_enter += 1
    while text_total != "" :
        space_enter = text_total.find(" ")
        print(text_total[:space_enter])
        text_total = text_total[space_enter + 1:]
    print("Количество различных чисел:", count_actual_enter)