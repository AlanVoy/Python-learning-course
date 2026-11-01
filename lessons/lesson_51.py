import sys
#
#
#
quantity_of_num = int(input("Укажите кол-во вводных: "))
if quantity_of_num < 1 :
    count_check_quantity = 1
    while count_check_quantity < 3 and quantity_of_num < 1 :
        print("Кол-во не меньше 1 !")
        quantity_of_num = int(input("Укажите кол-во вводных: "))
        count_check_quantity += 1
    if count_check_quantity == 3 and quantity_of_num < 1 :
        print("Кол-во попыток исчерпано")
        sys.exit()
if quantity_of_num > 0 :
    count_of_enter = 0
    text = str()
    num_max = int()
    count_max_num = 1
    num_max_in_line = 1
    flag = False
    while count_of_enter < quantity_of_num :
        text = text + input("Введите число: ") + " "
        count_of_enter += 1
    text_comparison = text
    while text_comparison != "" :
        space = text_comparison.find(" ")
        total_text = text
        num_comparison = int(text_comparison[:space])
        while total_text != "" :
            space_total = total_text.find(" ")
            num_total = int(total_text[:space_total])
            if num_comparison == num_total and text_comparison != total_text :
                flag = True
                count_max_num += 1
                if count_max_num > num_max_in_line :
                    num_max_in_line = count_max_num
                    num_max = num_comparison
            total_text = total_text[space_total + 1:]
        count_max_num = 1
        text_comparison = text_comparison[space + 1:]
    if not flag:
        num_max = int(text[:text.find(" ")])
    print("Число:", num_max)
    print("Количество повторений:",num_max_in_line)