text_time = input("Введите время в 24-часовом формате (Пример: 09:35): ")
if (len(text_time) == 5 and (text_time[:2].isdigit() and text_time[3:].isdigit()) and text_time[2] == ":" and (int(text_time[:2]) >= 0 and int(text_time[:2]) <= 23) and (int(text_time[3:]) >= 0 and int(text_time[3:]) <= 59) ) :
    print("Корректное время")
else :
    print("Некорректное время")