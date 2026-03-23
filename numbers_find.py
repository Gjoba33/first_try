from random import randint

def find_rand():
    start = int(input("Ввдите начало диапазона:"))
    end = int(input("Ввдите конец диапазона:"))
    
    rand_number = randint(start, end)

    print(f"Загаданное число {rand_number}")
    
    cnt = 1
    t = int(input(f"Попытка {cnt} Введи число в промежутке от {start} до {end}:"))
    
    while t != rand_number:
        if t > end or t < start:
            print("Дурак что ли оно в не диапозона")
        if t > rand_number:
            print("Неверно слишком много")
        else:
            print("Неверно слишком мало")
        cnt += 1
        t = int(input(f"Попытка {cnt} Введи число в промежутке от  {start} до {end}:"))

    return "Молодец успешно запулил в гит"


print(find_rand())
