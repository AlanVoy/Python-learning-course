import sys
#
orders = ["A101", "A102", "A103", "A104", "A105", "A106"]
flag_exit = False
for index, order in enumerate(orders, start=1) :
    print(index, order)
order_number_enter = input("Укажите количество заказов для обработки(не может превышать количество текущих заказов): ")
order_number_enter = order_number_enter.strip()
if order_number_enter.isdigit() :
    order_number_enter = int(order_number_enter)
else :
    flag_exit = True
if not flag_exit and order_number_enter <= len(orders) and order_number_enter >= 1 :
    print(orders[:order_number_enter])
    del orders[:order_number_enter]
    orders.extend(["A107", "A108"])
    print(orders)
else:
    flag_exit = True
if flag_exit :
    print("Некорректное количество заказов")
    sys.exit()