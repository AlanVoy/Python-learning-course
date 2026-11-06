import sys
#
products = {
    "Хлеб": 50,
    "Молоко": 100,
    "Сыр": 250,
    "Масло": 180
}
for key, value in products.items() :
    print(key,value)
name_for_chenge_price = input("Введите название товара для изменения цены: ")
flag = False
flag_price = False
for name in products :
    if name.casefold() == name_for_chenge_price.casefold() :
        flag = True
        price_for_change_price = input("Введите цену товара для изменения: ")
        price_for_change_price = price_for_change_price.strip()
        if price_for_change_price.isdigit() :
            price_for_change_price = int(price_for_change_price)
            if price_for_change_price > 0 :
                flag_price = True
        if flag_price :
            products[name] = price_for_change_price
        else :
            print("Некорректная цена")
    if flag :
        break
if not flag :
    print("Товар не найден")
name_for_del = input("Введите название товара для удаления: ")
flag = False
for name in products :
    if name.casefold() == name_for_del.casefold() :
        flag = True
        name_for_del = name
    if flag :
        break
if flag :
    del products[name_for_del]
else :
    print("Товар не найден")
for name, price in products.items() :
    print(name,price)