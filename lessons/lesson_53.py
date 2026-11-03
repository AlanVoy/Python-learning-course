import sys
#
products = ["Хлеб", "Молоко", "Сыр", "Масло"]
print(products)
number = input("Введите номер товара для замены(от 1 до 4 включительно): ")
if number.isdigit() :
    number = int(number)
    if number > 0 and number < 5 :
        number -= 1
        name_for_change = input("Введите новое название товара: ")
        name_for_change = name_for_change.strip()
        if name_for_change == "" :
            print("Название товара не может быть пустым")
            sys.exit()
        else :
            products[number] = name_for_change
        name_for_append = input("Введите название товара для добавления в список: ")
        name_for_append = name_for_append.strip()
        if name_for_append == "" :
            print("Название товара не может быть пустым")
            sys.exit()      
        else :
            products.append(name_for_append)
        products.pop(0)
        print("Итоговый список товаров:",products)
    else :
        print("Некорректный номер товара")
else:
    print("Некорректный номер товара")