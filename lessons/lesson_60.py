products = [
    {"id": 101, "name": "Монитор", "price": 12000, "quantity": 5},
    {"id": 102, "name": "Мышь", "price": 1500, "quantity": 12},
    {"id": 103, "name": "Клавиатура", "price": 3000, "quantity": 7},
    {"id": 104, "name": "Наушники", "price": 4500, "quantity": 3}
]
operations = [
    {"product_id": 101, "type": "sale", "quantity": 2},
    {"product_id": 102, "type": "arrival", "quantity": 5},
    {"product_id": 104, "type": "sale", "quantity": 4},
    {"product_id": 999, "type": "sale", "quantity": 1},
    {"product_id": 103, "type": "sale", "quantity": 3}
]
count_accept = 0
count_reject = 0
for operation in operations :
    flag_find = False
    if operation["quantity"] < 1 :
        print("Некорректное количество товара для операции")
        count_reject += 1
        continue
    for product in products :
        if operation["product_id"] == product["id"] :
            flag_find = True
            if operation["type"] == "sale" and product["quantity"] >= operation["quantity"] :
                print(product["id"],operation["type"],"Количество:",operation["quantity"])
                product["quantity"] = product["quantity"] - operation["quantity"]
                count_accept += 1
            elif operation["type"] == "arrival" :
                print(product["id"],operation["type"],"Количество:", operation["quantity"])
                product["quantity"] = product["quantity"] + operation["quantity"]
                count_accept += 1
            elif operation["type"] == "sale" and product["quantity"] < operation["quantity"] :
                print(product["id"],operation["type"],"Количество:", operation["quantity"])
                print("Недостаточно товара")
                count_reject += 1
            else:
                print("Неизвестный тип операции",operation["type"])
                count_reject += 1
    if not flag_find :
        print("Товар не найден")
        count_reject += 1
total_price = 0
for product in products :
    print(product["name"],"Остаток на складе",product["quantity"])
    total_price += (product["quantity"] * product["price"])
print("Успешных операций:",count_accept,)
print("Операций отклонено:",count_reject)
print("Общая стоимость оставшихся на складе товаров:",total_price)