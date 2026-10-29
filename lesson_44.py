sequence_length = int(input("Введите желаемое кол-во(не менее 2): "))
if sequence_length < 2 :
    count_check_sequence = 1
    while sequence_length < 2 and count_check_sequence < 3 :
        print("Кол-во не может быть менее 2")
        sequence_length = int(input("Введите желаемое кол-во(не менее 2): "))
        count_check_sequence += 1
else :
    count_lenght = 1
    while count_lenght <= sequence_length :
        if count_lenght < 2 :
            num = int(input("Введите число: "))
            changing_parity = 0
        else :
            num_previous = num
            num = int(input("Введите число: "))
            if (num % 2) != (num_previous % 2) :
                changing_parity += 1
        count_lenght += 1
    print("Кол-во переходов:", changing_parity)