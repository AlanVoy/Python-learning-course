warehouse = {
    "Монитор": {
        "price": 12000,
        "quantity": 5
    },
    "Клавиатура": {
        "price": 2500,
        "quantity": 10
    },
    "Мышь": {
        "price": 1200,
        "quantity": 15
    },
    "Наушники": {
        "price": 4500,
        "quantity": 3
    }
}

for product,data in warehouse.items() :
    print(f"{product}:")
    for key, value in warehouse[product].items() :
        print (key, "|", value)
    print("--------------------")
name_for_quantity_change = input("Введите название товара для изменения остатка: ")
name_for_quantity_change =  name_for_quantity_change.strip()
flag_find = False
flag_change = False
for name in warehouse :
    if name_for_quantity_change.casefold() == name.casefold() :
        flag_find = True
        name_for_quantity_change = name
        break
if flag_find :
    quantity_new = input("Укажите новое количество: ")
    quantity_new = quantity_new.strip()
    if quantity_new.isdigit() :
        quantity_new = int(quantity_new)
        if quantity_new >= 0 :
            flag_change = True
    if flag_change :
        warehouse[name_for_quantity_change]["quantity"] = quantity_new
    else:
        print("Некорректное количество")
else :
    print("Товар не найден")

total_price = 0
for product in warehouse :
    print(f"{product}:")
    for key, value in warehouse[product].items() :
        print (key, "|", value)
    total_price += warehouse[product]["price"] * warehouse[product]["quantity"]
    print("--------------------")
print(f"Общая стоимость товаров на складе: {total_price}")