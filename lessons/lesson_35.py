num_1 = int(input("Введите первое число: "))
num_2 = int(input("Введите второе число: "))
flag = False
if num_2 == 0 or num_1 == 0 :
    count = max(abs(num_1),abs(num_2))
else :
    count = min(abs(num_1),abs(num_2))
nod = int()
if num_1 == 0 and num_2 == 0:
    print("Оба числа равны 0, поиск НОД невозможен")
    exit()
while not flag :
    if (num_1 % count) == 0 == (num_2 % count) :
        flag = True
        nod = count
    else :
        count = count - 1
print("Наибольший общий делитель (НОД):",nod)