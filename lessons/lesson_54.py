import sys
#
products = [
    "Молоко",
    "Хлеб",
    "Молочный шоколад",
    "Сыр",
    "Молочный коктейль",
    "Масло"
]
for index, product in enumerate(products, start=1) :
    print(index, product)
name_product_find_enter = input("Введите название товара для поиска: ")
name_product_find_enter = name_product_find_enter.strip()
if name_product_find_enter == "" :
    print("Поисковый запрос не может быть пустым")
    sys.exit()
else :
    count_find = 0
    for index, product in enumerate(products, start=1) :
        if product.casefold().find(name_product_find_enter.casefold()) != -1 :
            print(index,product)
            count_find += 1
    if count_find == 0:
        print("Товары не найдены")