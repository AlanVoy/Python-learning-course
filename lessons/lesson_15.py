posnum = 0
negnum = 0
num = int(input("Введите число: "))
while num != 0:
    if num > 0:
        posnum = posnum + 1
    elif num < 0:
        negnum = negnum + 1
    num = int(input("Введите число: "))
print("Положительных:", posnum)
print("Отрицательных:", negnum)