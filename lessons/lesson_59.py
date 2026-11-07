orders = [
    {"id": 101, "product": "Монитор", "price": 12000, "status": "Новый"},
    {"id": 102, "product": "Мышь", "price": 1500, "status": "Оплачен"},
    {"id": 103, "product": "Клавиатура", "price": 3000, "status": "Новый"},
    {"id": 104, "product": "Наушники", "price": 4500, "status": "Отменён"},
    {"id": 105, "product": "Веб-камера", "price": 3200, "status": "Оплачен"}
]
for order in orders :
    print(order["id"],order["product"],order["price"],order["status"])
id_enter = input("Укажите id заказа: ")
flag_id = False
id_enter = id_enter.strip()
if id_enter.isdigit() :
    id_enter = int(id_enter)
    if id_enter > 0 :
        flag_id = True
if not flag_id :
    print("Некорректный номер заказа")
else :
    count_id = 0
    flag_find = False
    for order in orders :
        if order["id"] == id_enter :
            print(order["id"],order["product"],order["price"],order["status"])
            flag_find = True
            break
        count_id += 1
    if not flag_find :
        print("Заказ не найден")
    if flag_find and orders[count_id]["status"] == "Новый" :
        orders[count_id]["status"] = "Оплачен"
total_price = 0
count_status = 0
for order in orders :
    if order["status"] == "Оплачен" :
        total_price += order["price"]
        count_status += 1
print("Количество оплаченных заказов:", count_status, "Общая сумма:", total_price)
for order in orders :
    print(order["id"],order["product"],order["price"],order["status"])