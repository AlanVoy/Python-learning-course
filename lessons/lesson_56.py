import sys
#
warehouse = []
name_remains = []
count_remains = 0
total_price = 0
for product in warehouse :
    name, price, quantity = product
    print(name,f"Цена: {price}", f"Количество: {quantity}", f"Стоимость: {quantity * price}")
    if quantity < 5 :
        name_remains.append(name)
        count_remains += 1
    total_price += (quantity * price)
print("Общая стоимость товаров на складе:", total_price)
if not name_remains :
    print("Товаров по количеству меньше 5 не обнаружено")
else:
    print("Товаров по количеству меньше 5 на складе:", count_remains)
    print(name_remains)