age = int(input("Укажите возраст: "))
if age < 0:
    print("Возраст не может быть отрицательным")
elif age >= 0 and age <= 17:
    print("Несовершеннолетний")
elif age >= 18 and age <= 65:
    print("Взрослый")
elif age > 65:
    print("Пожилой")