age = int(input("Введите ваш возраст: "))
if age < 18:
    print("Доступ запрещён")
elif age >= 18 and age <= 65:
    print("Доступ разрешён")
elif age > 65:
    print("Требуется дополнительная проверка")